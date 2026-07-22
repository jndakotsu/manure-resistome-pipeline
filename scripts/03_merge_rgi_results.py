import pandas as pd
import glob
import os

rgi_dir = "rgi_results"
metadata_file = "sample_metadata.csv"

metadata = pd.read_csv(metadata_file).set_index("SRR")

sample_gene_counts = {}   # {SRR: {ARO Term: All Mapped Reads}}
gene_drug_class = {}      # {ARO Term: Drug Class}  (for later annotation)

for filepath in sorted(glob.glob(os.path.join(rgi_dir, "*.gene_mapping_data.txt"))):
    srr = os.path.basename(filepath).split(".")[0]
    df = pd.read_csv(filepath, sep="\t")

    # collapse in case a gene appears more than once per sample (sum reads)
    gene_reads = df.groupby("ARO Term")["All Mapped Reads"].sum()
    sample_gene_counts[srr] = gene_reads.to_dict()

    for _, row in df.iterrows():
        gene_drug_class[row["ARO Term"]] = row["Drug Class"]

# Build abundance matrix: rows = samples, columns = genes
abundance = pd.DataFrame(sample_gene_counts).T.fillna(0)
abundance.index.name = "SRR"

# Presence/absence version
presence = (abundance > 0).astype(int)

# Attach labels
abundance = abundance.join(metadata)
presence = presence.join(metadata)

# Save everything
abundance.to_csv("amr_abundance_matrix.csv")
presence.to_csv("amr_presence_absence_matrix.csv")

gene_annotation = pd.Series(gene_drug_class, name="Drug Class")
gene_annotation.index.name = "ARO Term"
gene_annotation.to_csv("gene_drug_class_lookup.csv")

print(f"Samples: {abundance.shape[0]}")
print(f"Unique genes detected across all samples: {abundance.shape[1] - 1}")  # -1 for label col
print()
print("Label distribution:")
print(metadata["label"].value_counts())
