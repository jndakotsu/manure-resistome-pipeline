import pandas as pd

stats_df = pd.read_csv("gene_mannwhitney_results.csv")
sig = stats_df[stats_df["p_adj_fdr"] < 0.05].copy()
sig["enriched_in"] = sig.apply(
    lambda r: "manure" if r["manure_mean"] > r["soil_mean"] else "soil", axis=1
)

print(f"Total FDR-significant genes: {len(sig)}")
print(sig["enriched_in"].value_counts())
print()
print(sig[["gene", "drug_class", "enriched_in", "manure_mean", "soil_mean", "p_adj_fdr"]]
      .sort_values("enriched_in")
      .to_string(index=False))

sig.to_csv("gene_mannwhitney_significant_only.csv", index=False)
