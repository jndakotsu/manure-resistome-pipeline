#!/usr/bin/env bash
set -euo pipefail

ACCESSION_LIST="${1:-accessions.txt}"

if [[ ! -f "$ACCESSION_LIST" ]]; then
  echo "Accession list not found: $ACCESSION_LIST"
  echo "Create it with one SRA accession per line (from SraRunTable.csv)."
  exit 1
fi

SUBSAMPLE_READS=500000
THREADS=4

RAW_DIR="raw_fastq"
TRIM_DIR="trimmed_fastq"
RGI_DIR="rgi_results"
LOG_DIR="logs"

mkdir -p "$RAW_DIR" "$TRIM_DIR" "$RGI_DIR" "$LOG_DIR"

while IFS= read -r SRR; do
  [[ -z "$SRR" ]] && continue
  echo "=== Processing $SRR ==="

  R1="$RAW_DIR/${SRR}_1.fastq.gz"
  R2="$RAW_DIR/${SRR}_2.fastq.gz"
  T1="$TRIM_DIR/${SRR}_1.trim.fastq.gz"
  T2="$TRIM_DIR/${SRR}_2.trim.fastq.gz"

  if [[ -f "$R1" && -f "$R2" ]]; then
    echo "Raw fastq already present for $SRR, skipping download."
  else
    if [[ -n "$SUBSAMPLE_READS" ]]; then
      fastq-dump --split-files --gzip -X "$SUBSAMPLE_READS" \
        -O "$RAW_DIR" "$SRR" > "$LOG_DIR/${SRR}_fastqdump.log" 2>&1
    else
      fastq-dump --split-files --gzip \
        -O "$RAW_DIR" "$SRR" > "$LOG_DIR/${SRR}_fastqdump.log" 2>&1
    fi
  fi

  if [[ -f "$T1" && -f "$T2" ]]; then
    echo "Trimmed fastq already present for $SRR, skipping trimming."
  else
    fastp \
      -i "$R1" -I "$R2" \
      -o "$T1" -O "$T2" \
      --thread "$THREADS" \
      --json "$LOG_DIR/${SRR}_fastp.json" \
      --html "$LOG_DIR/${SRR}_fastp.html" \
      > "$LOG_DIR/${SRR}_fastp.log" 2>&1
  fi

  if [[ -d "$RGI_DIR/${SRR}" || -f "$RGI_DIR/${SRR}.allele_mapping_data.txt" ]]; then
    echo "RGI output already present for $SRR, skipping."
  else
    rgi bwt \
      -1 "$T1" -2 "$T2" \
      -a kma \
      -o "$RGI_DIR/${SRR}" \
      --threads "$THREADS" \
      --clean \
      > "$LOG_DIR/${SRR}_rgi.log" 2>&1
  fi

  echo "=== Done: $SRR ==="
done < "$ACCESSION_LIST"

echo "All samples processed. Per-sample RGI output is in $RGI_DIR/"
