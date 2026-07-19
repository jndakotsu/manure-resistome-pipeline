# Results

## Sample overview

| Sample | SRA Accession | Read pairs (subsampled) | AMR genes detected | Reads mapped to CARD |
|---|---|---|---|---|
| Sample 1 | SRR12619551 | 476,930 | 47 | 294 (0.03%) |
| Sample 2 | SRR12619561 | 483,308 | 91 | (see overall_mapping_stats) |

## Top AMR genes — Sample 1 (SRR12619551)

| ARO Term                                                                      | AMR Gene Family                                                                  | Drug Class                                                                          | Resistance Mechanism                                        |   Completely Mapped Reads |
|:------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------|--------------------------:|
| rpoB2                                                                         | rifamycin-resistant beta-subunit of RNA polymerase (rpoB)                        | rifamycin antibiotic                                                                | antibiotic target alteration; antibiotic target replacement |                        57 |
| Bifidobacterium adolescentis rpoB mutants conferring resistance to rifampicin | rifamycin-resistant beta-subunit of RNA polymerase (rpoB)                        | rifamycin antibiotic                                                                | antibiotic target alteration; antibiotic target replacement |                        37 |
| HelR                                                                          | helicase-like RNA polymerase protection protein                                  | rifamycin antibiotic                                                                | antibiotic target protection                                |                        29 |
| MexF                                                                          | resistance-nodulation-cell division (RND) antibiotic efflux pump                 | fluoroquinolone antibiotic; diaminopyrimidine antibiotic; phenicol antibiotic       | antibiotic efflux                                           |                        14 |
| vanR gene in vanO cluster                                                     | glycopeptide resistance gene cluster; vanR                                       | glycopeptide antibiotic                                                             | antibiotic target alteration                                |                        13 |
| MuxB                                                                          | resistance-nodulation-cell division (RND) antibiotic efflux pump                 | macrolide antibiotic; monobactam; tetracycline antibiotic; aminocoumarin antibiotic | antibiotic efflux                                           |                        12 |
| vanS gene in vanO cluster                                                     | vanS; glycopeptide resistance gene cluster                                       | glycopeptide antibiotic                                                             | antibiotic target alteration                                |                         9 |
| oleB                                                                          | Miscellaneous ABC-F subfamily ATP-binding cassette ribosomal protection proteins | macrolide antibiotic                                                                | antibiotic target protection                                |                         8 |
| amrB                                                                          | resistance-nodulation-cell division (RND) antibiotic efflux pump                 | macrolide antibiotic; aminoglycoside antibiotic                                     | antibiotic efflux                                           |                         7 |
| novA                                                                          | ATP-binding cassette (ABC) antibiotic efflux pump                                | aminocoumarin antibiotic                                                            | antibiotic efflux                                           |                         7 |

## Top AMR genes — Sample 2 (SRR12619561)

| ARO Term                                               | AMR Gene Family                                     | Drug Class                                                                                                                     | Resistance Mechanism         |   Completely Mapped Reads |
|:-------------------------------------------------------|:----------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|:-----------------------------|--------------------------:|
| tet(M)                                                 | tetracycline-resistant ribosomal protection protein | tetracycline antibiotic                                                                                                        | antibiotic target protection |                       205 |
| tet(T)                                                 | tetracycline-resistant ribosomal protection protein | tetracycline antibiotic                                                                                                        | antibiotic target protection |                       198 |
| tet(36)                                                | tetracycline-resistant ribosomal protection protein | tetracycline antibiotic                                                                                                        | antibiotic target protection |                        83 |
| tet(44)                                                | tetracycline-resistant ribosomal protection protein | tetracycline antibiotic                                                                                                        | antibiotic target protection |                        70 |
| tet(Q)                                                 | tetracycline-resistant ribosomal protection protein | tetracycline antibiotic                                                                                                        | antibiotic target protection |                        65 |
| lsaE                                                   | lsa-type ABC-F protein                              | lincosamide antibiotic; streptogramin antibiotic; pleuromutilin antibiotic                                                     | antibiotic target protection |                        57 |
| EstT                                                   | macrolide esterase                                  | macrolide antibiotic                                                                                                           | antibiotic inactivation      |                        49 |
| lnuB                                                   | lincosamide nucleotidyltransferase (LNU)            | lincosamide antibiotic                                                                                                         | antibiotic inactivation      |                        47 |
| 23S rRNA (adenine(2058)-N(6))-methyltransferase Erm(A) | Erm 23S ribosomal RNA methyltransferase             | macrolide antibiotic; lincosamide antibiotic; streptogramin antibiotic                                                         | antibiotic target alteration |                        30 |
| ErmC                                                   | Erm 23S ribosomal RNA methyltransferase             | macrolide antibiotic; lincosamide antibiotic; streptogramin antibiotic; streptogramin A antibiotic; streptogramin B antibiotic | antibiotic target alteration |                        30 |

## Resistome overlap

- Genes unique to Sample 1: 40
- Genes unique to Sample 2: 84
- Shared genes: 7
- Shared gene list: Bifidobacterium adolescentis rpoB mutants conferring resistance to rifampicin, Bifidobacterium bifidum ileS conferring resistance to mupirocin, lnuB, lsaE, mdtB, smeE, tetA(P)

## Interpretation

Sample 1's resistome is dominated by rifamycin resistance (target alteration/protection/inactivation
mechanisms) and RND-family efflux pumps (MexF, MuxB/C, amrB), consistent with intrinsic/environmental
resistance mechanisms common in soil-associated Actinobacteria and Pseudomonas.

Sample 2's resistome is dominated by tetracycline resistance genes (tet(M), tet(T), tet(36), tet(44),
tet(Q)) and lincosamide/macrolide resistance (lnuB, lnuG, ErmC, mel), a pattern consistent with
antibiotic-driven selection from tetracycline use in animal production.

Only 7 of 131 total unique genes were shared between the two samples,
indicating the resistome composition is largely source/sample-specific rather than reflecting a
common "core" set across manure types.
