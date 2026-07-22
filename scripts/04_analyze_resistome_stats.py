import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu
from statsmodels.stats.multitest import multipletests
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load data -----------------------------------------------------------
abundance = pd.read_csv("results/amr_abundance_matrix.csv", index_col="SRR")
gene_cols = [c for c in abundance.columns if c != "label"]
labels = abundance["label"]

X = abundance[gene_cols]

# --- Mann-Whitney U test per gene ----------------------------------------
results = []
for gene in gene_cols:
    manure_vals = X.loc[labels == "manure", gene]
    soil_vals = X.loc[labels == "soil", gene]
    if manure_vals.nunique() == 1 and soil_vals.nunique() == 1 and manure_vals.iloc[0] == soil_vals.iloc[0]:
        continue
    try:
        stat, p = mannwhitneyu(manure_vals, soil_vals, alternative="two-sided")
    except ValueError:
        continue
    results.append({
        "gene": gene,
        "manure_mean": manure_vals.mean(),
        "soil_mean": soil_vals.mean(),
        "U_stat": stat,
        "p_value": p
    })

stats_df = pd.DataFrame(results).sort_values("p_value")
stats_df["p_adj_fdr"] = multipletests(stats_df["p_value"], method="fdr_bh")[1]

gene_drug_class = pd.read_csv("data/gene_drug_class_lookup.csv", index_col="ARO Term")["Drug Class"]
stats_df["drug_class"] = stats_df["gene"].map(gene_drug_class)

stats_df.to_csv("results/gene_mannwhitney_results.csv", index=False)
stats_df[stats_df["p_adj_fdr"] < 0.05].to_csv("results/gene_mannwhitney_significant_only.csv", index=False)

print(f"Genes tested: {len(stats_df)}")
print(f"Genes with raw p < 0.05: {(stats_df['p_value'] < 0.05).sum()}")
print(f"Genes with FDR-adjusted p < 0.05: {(stats_df['p_adj_fdr'] < 0.05).sum()}")
print()
print("Top 10 genes by raw p-value:")
print(stats_df[["gene", "drug_class", "manure_mean", "soil_mean", "p_value", "p_adj_fdr"]].head(10).to_string(index=False))

# --- PCA -------------------------------------------------------------------
X_scaled = StandardScaler().fit_transform(X)
pca = PCA(n_components=2)
pcs = pca.fit_transform(X_scaled)

plt.figure(figsize=(7, 6))
colors = {"manure": "#8B4513", "soil": "#556B2F"}
for lbl in ["manure", "soil"]:
    mask = labels == lbl
    plt.scatter(pcs[mask, 0], pcs[mask, 1], label=lbl, s=100, color=colors[lbl], edgecolor="black")
for i, srr in enumerate(X.index):
    plt.annotate(srr.replace("SRR126195", ""), (pcs[i, 0], pcs[i, 1]), fontsize=8, xytext=(5, 5), textcoords="offset points")
plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)")
plt.title("PCA of AMR Gene Abundance: Manure vs. Soil (n=6 each)")
plt.legend()
plt.tight_layout()
plt.savefig("figures/pca_manure_vs_soil.png", dpi=150)
plt.close()

# --- Heatmap of top differential genes --------------------------------------
top_genes = stats_df.head(30)["gene"].tolist()
heatmap_data = X[top_genes].T
heatmap_data.columns = [f"{s}\n({labels[s]})" for s in heatmap_data.columns]

plt.figure(figsize=(10, 10))
sns.heatmap(np.log1p(heatmap_data), cmap="YlOrRd", cbar_kws={"label": "log(reads+1)"})
plt.title("Top 30 Differentially Abundant AMR Genes (by raw p-value)")
plt.tight_layout()
plt.savefig("figures/heatmap_top_genes.png", dpi=150)
plt.close()

print()
print("Saved: results/gene_mannwhitney_results.csv, results/gene_mannwhitney_significant_only.csv, figures/pca_manure_vs_soil.png, figures/heatmap_top_genes.png")
