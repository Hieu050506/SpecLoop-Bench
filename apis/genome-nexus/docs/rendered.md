# Genome Nexus API — API Reference

This page shows how to use HTTP requests to access the Genome Nexus API. There are more high level clients available in Python, R, JavaScript, TypeScript and various other languages as well as a command line client to annotate MAF and VCF. See https://docs.genomenexus.org/api.

Aside from programmatic clients there are web based tools to annotate variants, see https://docs.genomenexus.org/tools.

 We currently only provide long-term support for the '/annotation' endpoint. The other endpoints might change.

**Version:** 2.0  
**Base URL:** `https://www.genomenexus.org`

## annotation-controller

Annotation Controller

### POST /annotation

**Retrieves VEP annotation for the provided list of variants**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `isoformOverrideSource` | query | string | No | Isoform override source. For example uniprot |
| `token` | query | string | No | Map of tokens. For example {"source1":"put-your-token1-here","source2":"put-your-token2-here"} |
| `fields` | query | array of string | No | Comma separated list of fields to include (case-sensitive!). For example: hotspots |

**Request body** (`application/json`, required)

List of variants. For example ["X:g.66937331T>A","17:g.41242962_41242963insGA"] (GRCh37) or ["1:g.182712A>C", "2:g.265023C>T", "3:g.319781del", "19:g.110753dup", "1:g.1385015_1387562del"] (GRCh38)

- Body type: array of string

**Responses**

- **200** — OK
  Body (`application/json`, array of object):
  - `allele_string` (string) — Allele string (e.g: A/T)
  - `annotationJSON` (string) — Annotation data as JSON string
  - `annotation_summary` (object)
    - `assemblyName` (string) — Assembly name
    - `canonicalTranscriptId` (string) — Canonical transcript id
    - `genomicLocation` (object)
      - `chromosome` (string, required) — Chromosome
      - `start` (integer (int32), required) — Start Position
      - `end` (integer (int32), required) — End Position
      - `referenceAllele` (string, required) — Reference Allele
      - `variantAllele` (string, required) — Variant Allele
    - `strandSign` (string) — Strand (- or +)
    - `transcriptConsequenceSummaries` (array of object, required) — All transcript consequence summaries
      - `aminoAcidAlt` (string) — Alt Amino Acid
      - `aminoAcidRef` (string) — Reference Amino Acid
      - `aminoAcids` (string) — Amino acids change
      - `codonChange` (string) — Codon change
      - `consequenceTerms` (string) — Consequence terms (comma separated)
      - `entrezGeneId` (string) — Entrez gene id
      - `exon` (string)
      - `hgvsc` (string) — HGVSc
      - `hgvsp` (string) — HGVSp
      - `hgvspShort` (string) — HGVSp short
      - `hugoGeneSymbol` (string) — Hugo gene symbol
      - `polyphenPrediction` (string) — Polyphen Prediction
      - `polyphenScore` (number (double)) — Polyphen Score
      - `proteinPosition` (object)
        - `end` (integer (int32))
        - `start` (integer (int32))
      - `refSeq` (string) — RefSeq id
      - `siftPrediction` (string) — Sift Prediction
      - `siftScore` (number (double)) — Sift Score
      - `transcriptId` (string, required) — Transcript id
      - `uniprotId` (string) — Uniprot ID
      - `variantClassification` (string) — Variant classification
    - `transcriptConsequenceSummary` (object, required)
      - `aminoAcidAlt` (string) — Alt Amino Acid
      - `aminoAcidRef` (string) — Reference Amino Acid
      - `aminoAcids` (string) — Amino acids change
      - `codonChange` (string) — Codon change
      - `consequenceTerms` (string) — Consequence terms (comma separated)
      - `entrezGeneId` (string) — Entrez gene id
      - `exon` (string)
      - `hgvsc` (string) — HGVSc
      - `hgvsp` (string) — HGVSp
      - `hgvspShort` (string) — HGVSp short
      - `hugoGeneSymbol` (string) — Hugo gene symbol
      - `polyphenPrediction` (string) — Polyphen Prediction
      - `polyphenScore` (number (double)) — Polyphen Score
      - `proteinPosition` (object)
        - `end` (integer (int32))
        - `start` (integer (int32))
      - `refSeq` (string) — RefSeq id
      - `siftPrediction` (string) — Sift Prediction
      - `siftScore` (number (double)) — Sift Score
      - `transcriptId` (string, required) — Transcript id
      - `uniprotId` (string) — Uniprot ID
      - `variantClassification` (string) — Variant classification
    - `transcriptConsequences` (array of object, required) — (Deprecated) Transcript consequence summaries (list of one when using annotation/, multiple when using annotation/summary/
      - `aminoAcidAlt` (string) — Alt Amino Acid
      - `aminoAcidRef` (string) — Reference Amino Acid
      - `aminoAcids` (string) — Amino acids change
      - `codonChange` (string) — Codon change
      - `consequenceTerms` (string) — Consequence terms (comma separated)
      - `entrezGeneId` (string) — Entrez gene id
      - `exon` (string)
      - `hgvsc` (string) — HGVSc
      - `hgvsp` (string) — HGVSp
      - `hgvspShort` (string) — HGVSp short
      - `hugoGeneSymbol` (string) — Hugo gene symbol
      - `polyphenPrediction` (string) — Polyphen Prediction
      - `polyphenScore` (number (double)) — Polyphen Score
      - `proteinPosition` (object)
        - `end` (integer (int32))
        - `start` (integer (int32))
      - `refSeq` (string) — RefSeq id
      - `siftPrediction` (string) — Sift Prediction
      - `siftScore` (number (double)) — Sift Score
      - `transcriptId` (string, required) — Transcript id
      - `uniprotId` (string) — Uniprot ID
      - `variantClassification` (string) — Variant classification
    - `variant` (string, required) — Variant key
    - `variantType` (string) — Variant type
  - `assembly_name` (string) — NCBI build number
  - `clinvar` (object)
    - `annotation` (object)
      - `alternateAllele` (string)
      - `chromosome` (string)
      - `clinicalSignificance` (string)
      - `clinvarId` (integer (int32))
      - `conflictingClinicalSignificance` (string)
      - `endPosition` (integer (int32))
      - `referenceAllele` (string)
      - `startPosition` (integer (int32))
  - `colocatedVariants` (array of object)
    - `dbSnpId` (string)
    - `gnomad_nfe_allele` (string, required) — GnomAD Non-Finnish European Allele
    - `gnomad_nfe_maf` (string, required) — GnomAD Non-Finnish European MAF
    - `gnomad_afr_allele` (string, required) — GnomAD African/African American Allele
    - `gnomad_afr_maf` (string, required) — GnomAD African/African American MAF
    - `gnomad_eas_allele` (string, required) — GnomAD East Asian Allele
    - `gnomad_eas_maf` (string, required) — GnomAD East Asian MAF
  - `end` (integer (int32)) — End position
  - `hgvsg` (string)
  - `hotspots` (object)
    - `annotation` (array of array of object)
      - `hugoSymbol` (string) — Hugo gene symbol
      - `inframeCount` (integer (int32)) — Inframe mutation count
      - `missenseCount` (integer (int32)) — Missense mutation count
      - `residue` (string) — Hotspot residue
      - `spliceCount` (integer (int32)) — Splice mutation count
      - `transcriptId` (string) — Ensembl Transcript Id
      - `truncatingCount` (integer (int32)) — Truncation mutation count
      - `tumorCount` (integer (int32)) — Tumor count
      - `type` (string) — Hotspot type
    - `license` (string)
  - `id` (string, required) — Variant id
  - `intergenic_consequences` (array of object, required) — intergenicConsequences
    - `impact` (string, required) — impact
    - `variantAllele` (string, required) — variant_allele
    - `consequenceTerms` (array of string, required) — consequence_terms
  - `most_severe_consequence` (string) — Most severe consequence
  - `mutation_assessor` (object)
    - `annotation` (object)
      - `codonStartPosition` (string) — Codon start position
      - `cosmicCount` (integer (int32)) — Number of mutations in COSMIC for this protein
      - `functionalImpact` (string) — Functional impact
      - `functionalImpactScore` (number (double)) — Functional impact score
      - `hgvs` (string)
      - `hugoSymbol` (string) — Hugo gene symbol
      - `input` (string, required) — User-input variants
      - `mappingIssue` (string) — Mapping issue info
      - `msaGaps` (number (double)) — Portion of gaps in variant position in multiple sequence alignment
      - `msaHeight` (integer (int32)) — Number of diverse sequences in multiple sequence alignment (identical or highly similar sequences filtered out)
      - `msaLink` (string) — Link to multiple sequence alignment
      - `pdbLink` (string) — Link to 3d structure browser
      - `referenceGenomeVariant` (string) — Reference genome variant
      - `referenceGenomeVariantType` (string) — Reference genome variant type
      - `refseqId` (string) — Refseq protein ID
      - `refseqPosition` (integer (int32)) — Variant position in Refseq protein, can be different from the one in Uniprot
      - `refseqResidue` (string) — Reference residue in Refseq protein, can be different from the one in Uniprot
      - `snpCount` (integer (int32)) — Number of SNPs in dbSNP for this protein
      - `uniprotId` (string) — Uniprot protein accession ID
      - `uniprotPosition` (integer (int32)) — Variant position in Uniprot protein, can be different from the one in Refseq
      - `uniprotResidue` (string) — Reference residue in Uniprot protein, can be different from the one in Refseq
      - `variant` (string) — Amino acid substitution
      - `variantConservationScore` (number (double)) — Variant conservation score
      - `variantSpecificityScore` (number (double)) — Variant specificity score
    - `license` (string)
  - `my_variant_info` (object)
    - `annotation` (object)
      - `clinVar` (object)
        - `alleleId` (integer (int32)) — allele_id
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `cytogenic` (string) — cytogenic
        - `gene` (object)
        - `hg19` (object)
        - `hg38` (object)
        - `hgvs` (object)
        - `license` (string) — license
        - `rcv` (array of object)
        - `variantId` (integer (int32)) — variant_id
      - `cosmic` (object)
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `cosmicId` (string) — cosmic_id
        - `hg19` (object)
        - `license` (string) — _license
        - `mutFreq` (number (double)) — mut_freq
        - `mutNt` (string) — mut_nt
        - `ref` (string) — ref
        - `tumorSite` (string) — tumor_site
      - `dbsnp` (object)
        - `_class` (string) — class
        - `alleleOrigin` (string) — allele_origin
        - `alleles` (array of object) — alleles
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `dbsnpBuild` (integer (int32)) — dbsnp_build
        - `flags` (array of string) — flags
        - `hg19` (object)
        - `license` (string) — _license
        - `ref` (string) — ref
        - `rsid` (string) — rsid
        - `validated` (boolean) — validated
        - `varSubtype` (string) — var_subtype
        - `vartype` (string) — vartype
      - `gnomadExome` (object)
        - `alleleCount` (object)
        - `alleleFrequency` (object)
        - `alleleNumber` (object)
        - `homozygotes` (object)
      - `gnomadGenome` (object)
        - `alleleCount` (object)
        - `alleleFrequency` (object)
        - `alleleNumber` (object)
        - `homozygotes` (object)
      - `hgvs` (string) — hgvs
      - `mutdb` (object)
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `cosmicId` (string) — cosmic_id
        - `hg19` (object)
        - `mutpredScore` (number (double)) — mutpred_score
        - `ref` (string) — ref
        - `rsid` (string) — rsid
        - `uniprotId` (string) — uniprot_id
      - `query` (string)
      - `snpeff` (object)
        - `license` (string) — license
      - `variant` (string) — variant
      - `vcf` (object)
        - `alt` (string) — alt
        - `position` (string) — position
        - `ref` (string) — ref
      - `version` (integer (int32)) — version
    - `license` (string)
  - `nucleotide_context` (object)
    - `annotation` (object)
      - `hgvs` (string)
      - `id` (string)
      - `molecule` (string)
      - `query` (string)
      - `seq` (string, required) — Nucleotide context sequence
    - `license` (string)
  - `oncokb` (object)
    - `annotation` (object)
      - `alleleExist` (boolean)
      - `dataVersion` (string)
      - `diagnosticImplications` (array of object)
        - `alterations` (array of string)
        - `description` (string)
        - `levelOfEvidence` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
        - `tumorType` (object) — OncoTree Detailed Cancer Type
      - `diagnosticSummary` (string)
      - `geneExist` (boolean)
      - `geneSummary` (string)
      - `highestDiagnosticImplicationLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `highestPrognosticImplicationLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `highestResistanceLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `highestSensitiveLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `hotspot` (boolean)
      - `lastUpdate` (string)
      - `mutationEffect` (object)
        - `citations` (object)
        - `description` (string)
        - `knownEffect` (string)
      - `oncogenic` (string)
      - `otherSignificantResistanceLevels` (array of string)
      - `otherSignificantSensitiveLevels` (array of string)
      - `prognosticImplications` (array of object)
        - `alterations` (array of string)
        - `description` (string)
        - `levelOfEvidence` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
        - `tumorType` (object) — OncoTree Detailed Cancer Type
      - `prognosticSummary` (string)
      - `query` (object)
        - `alteration` (string)
        - `alterationType` (string)
        - `consequence` (string)
        - `entrezGeneId` (integer (int32))
        - `hgvs` (string)
        - `hugoSymbol` (string)
        - `id` (string)
        - `proteinEnd` (integer (int32))
        - `proteinStart` (integer (int32))
        - `svType` (string) — Allowed values: `DELETION`, `TRANSLOCATION`, `DUPLICATION`, `INSERTION`, `INVERSION`, `FUSION`, `UNKNOWN`.
        - `tumorType` (string)
        - `type` (string)
      - `treatments` (array of object)
        - `abstracts` (array of object)
        - `alterations` (array of string)
        - `approvedIndications` (array of string)
        - `description` (string)
        - `drugs` (array of object)
        - `fdaApproved` (boolean)
        - `level` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
        - `levelAssociatedCancerType` (object) — OncoTree Detailed Cancer Type
        - `pmids` (array of string)
      - `tumorTypeSummary` (string)
      - `variantExist` (boolean)
      - `variantSummary` (string)
      - `vus` (boolean)
    - `license` (string)
  - `originalVariantQuery` (string, required) — Original variant query
  - `ptms` (object)
    - `annotation` (array of array of object)
      - `ensemblTranscriptIds` (array of string)
      - `position` (integer (int32))
      - `pubmedIds` (array of string)
      - `sequence` (string)
      - `type` (string)
      - `uniprotAccession` (string)
      - `uniprotEntry` (string)
    - `license` (string)
  - `seq_region_name` (string) — Chromosome
  - `signalAnnotation` (object)
    - `annotation` (array of object)
      - `biallelicCountsByTumorType` (array of object) — Biallelic Counts by Tumor Type
        - `tumorType` (string) — Tumor Type
        - `tumorTypeCount` (integer (int32)) — Sample count for Tumor Type
        - `variantCount` (integer (int32)) — Variant count for Tumor Type
      - `chromosome` (string) — Chromosome
      - `countsByTumorType` (array of object) — Counts by Tumor Type
        - `tumorType` (string) — Tumor Type
        - `tumorTypeCount` (integer (int32)) — Sample count for Tumor Type
        - `variantCount` (integer (int32)) — Variant count for Tumor Type
      - `endPosition` (integer (int64)) — End Position
      - `generalPopulationStats` (object)
        - `counts` (object)
        - `frequencies` (object)
      - `hugoGeneSymbol` (string) — Hugo Gene Symbol
      - `mskExperReview` (boolean) — Msk Expert Review
      - `mutationStatus` (string) — Mutation Status
      - `overallNumberOfGermlineHomozygous` (integer (int32))
      - `pathogenic` (string) — Pathogenic
      - `penetrance` (string) — Penetrance
      - `qcPassCountsByTumorType` (array of object) — QC Pass Counts by Tumor Type
        - `tumorType` (string) — Tumor Type
        - `tumorTypeCount` (integer (int32)) — Sample count for Tumor Type
        - `variantCount` (integer (int32)) — Variant count for Tumor Type
      - `referenceAllele` (string) — Reference Allele
      - `startPosition` (integer (int64)) — Start Position
      - `statsByTumorType` (array of object) — Stats By Tumor Type
        - `ageAtDx` (integer (int32)) — Median Age at Dx
        - `fBiallelic` (number (double)) — Frequency Of Biallelic
        - `fCancerTypeCount` (number (double)) — Frequency Of Cancer Type Count
        - `hrdScore` (object)
        - `msiScore` (number (double)) — Msi Score
        - `nCancerTypeCount` (integer (int32)) — Number Of Cancer Type Count
        - `numberOfGermlineHomozygous` (integer (int32)) — Number Of Germline Homozygous Per Tumor Type
        - `numberWithSig` (integer (int32)) — Number of Variants with Signature
        - `tmb` (number (double)) — Median TMB
        - `tumorType` (string) — Tumor Type
      - `variantAllele` (string) — Variant Allele
    - `license` (string)
  - `start` (integer (int32)) — Start position
  - `strand` (integer (int32)) — Strand (negative or positive)
  - `successfully_annotated` (boolean) — Status flag indicating whether variant was succesfully annotated
  - `transcript_consequences` (array of object) — List of transcripts
    - `amino_acids` (string) — Amino acids
    - `canonical` (string) — Canonical transcript indicator
    - `codons` (string) — Codons
    - `consequence_terms` (array of string) — List of consequence terms
    - `exon` (string)
    - `gene_id` (string) — Ensembl gene id
    - `gene_symbol` (string) — Hugo gene symbol
    - `hgnc_id` (string) — HGNC id
    - `hgvsc` (string) — HGVSc
    - `hgvsg` (string) — HGVSg
    - `hgvsp` (string) — HGVSp
    - `polyphen_prediction` (string) — Polyphen Prediction
    - `polyphen_score` (number (double)) — Polyphen Score
    - `protein_end` (integer (int32)) — Protein end position
    - `protein_id` (string) — Ensembl protein id
    - `protein_start` (integer (int32)) — Protein start position
    - `refseq_transcript_ids` (array of string) — List of RefSeq transcript ids
    - `sift_prediction` (string) — Sift Prediction
    - `sift_score` (number (double)) — Sift Score
    - `transcript_id` (string, required) — Ensembl transcript id
    - `uniprotId` (string)
    - `variant_allele` (string) — Variant allele
  - `variant` (string, required) — Variant key

### POST /annotation/dbsnp/

**Retrieves VEP annotation for the provided list of dbSNP ids**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `isoformOverrideSource` | query | string | No | Isoform override source. For example uniprot |
| `token` | query | string | No | Map of tokens. For example {"source1":"put-your-token1-here","source2":"put-your-token2-here"} |
| `fields` | query | array of string | No | Comma separated list of fields to include (case-sensitive!). For example: annotation_summary |

**Request body** (`application/json`, required)

List of variant IDs. For example ["rs116035550"]

- Body type: array of string

**Responses**

- **200** — OK
  Body (`application/json`, array of object):
  - `allele_string` (string) — Allele string (e.g: A/T)
  - `annotationJSON` (string) — Annotation data as JSON string
  - `annotation_summary` (object)
    - `assemblyName` (string) — Assembly name
    - `canonicalTranscriptId` (string) — Canonical transcript id
    - `genomicLocation` (object)
      - `chromosome` (string, required) — Chromosome
      - `start` (integer (int32), required) — Start Position
      - `end` (integer (int32), required) — End Position
      - `referenceAllele` (string, required) — Reference Allele
      - `variantAllele` (string, required) — Variant Allele
    - `strandSign` (string) — Strand (- or +)
    - `transcriptConsequenceSummaries` (array of object, required) — All transcript consequence summaries
      - `aminoAcidAlt` (string) — Alt Amino Acid
      - `aminoAcidRef` (string) — Reference Amino Acid
      - `aminoAcids` (string) — Amino acids change
      - `codonChange` (string) — Codon change
      - `consequenceTerms` (string) — Consequence terms (comma separated)
      - `entrezGeneId` (string) — Entrez gene id
      - `exon` (string)
      - `hgvsc` (string) — HGVSc
      - `hgvsp` (string) — HGVSp
      - `hgvspShort` (string) — HGVSp short
      - `hugoGeneSymbol` (string) — Hugo gene symbol
      - `polyphenPrediction` (string) — Polyphen Prediction
      - `polyphenScore` (number (double)) — Polyphen Score
      - `proteinPosition` (object)
        - `end` (integer (int32))
        - `start` (integer (int32))
      - `refSeq` (string) — RefSeq id
      - `siftPrediction` (string) — Sift Prediction
      - `siftScore` (number (double)) — Sift Score
      - `transcriptId` (string, required) — Transcript id
      - `uniprotId` (string) — Uniprot ID
      - `variantClassification` (string) — Variant classification
    - `transcriptConsequenceSummary` (object, required)
      - `aminoAcidAlt` (string) — Alt Amino Acid
      - `aminoAcidRef` (string) — Reference Amino Acid
      - `aminoAcids` (string) — Amino acids change
      - `codonChange` (string) — Codon change
      - `consequenceTerms` (string) — Consequence terms (comma separated)
      - `entrezGeneId` (string) — Entrez gene id
      - `exon` (string)
      - `hgvsc` (string) — HGVSc
      - `hgvsp` (string) — HGVSp
      - `hgvspShort` (string) — HGVSp short
      - `hugoGeneSymbol` (string) — Hugo gene symbol
      - `polyphenPrediction` (string) — Polyphen Prediction
      - `polyphenScore` (number (double)) — Polyphen Score
      - `proteinPosition` (object)
        - `end` (integer (int32))
        - `start` (integer (int32))
      - `refSeq` (string) — RefSeq id
      - `siftPrediction` (string) — Sift Prediction
      - `siftScore` (number (double)) — Sift Score
      - `transcriptId` (string, required) — Transcript id
      - `uniprotId` (string) — Uniprot ID
      - `variantClassification` (string) — Variant classification
    - `transcriptConsequences` (array of object, required) — (Deprecated) Transcript consequence summaries (list of one when using annotation/, multiple when using annotation/summary/
      - `aminoAcidAlt` (string) — Alt Amino Acid
      - `aminoAcidRef` (string) — Reference Amino Acid
      - `aminoAcids` (string) — Amino acids change
      - `codonChange` (string) — Codon change
      - `consequenceTerms` (string) — Consequence terms (comma separated)
      - `entrezGeneId` (string) — Entrez gene id
      - `exon` (string)
      - `hgvsc` (string) — HGVSc
      - `hgvsp` (string) — HGVSp
      - `hgvspShort` (string) — HGVSp short
      - `hugoGeneSymbol` (string) — Hugo gene symbol
      - `polyphenPrediction` (string) — Polyphen Prediction
      - `polyphenScore` (number (double)) — Polyphen Score
      - `proteinPosition` (object)
        - `end` (integer (int32))
        - `start` (integer (int32))
      - `refSeq` (string) — RefSeq id
      - `siftPrediction` (string) — Sift Prediction
      - `siftScore` (number (double)) — Sift Score
      - `transcriptId` (string, required) — Transcript id
      - `uniprotId` (string) — Uniprot ID
      - `variantClassification` (string) — Variant classification
    - `variant` (string, required) — Variant key
    - `variantType` (string) — Variant type
  - `assembly_name` (string) — NCBI build number
  - `clinvar` (object)
    - `annotation` (object)
      - `alternateAllele` (string)
      - `chromosome` (string)
      - `clinicalSignificance` (string)
      - `clinvarId` (integer (int32))
      - `conflictingClinicalSignificance` (string)
      - `endPosition` (integer (int32))
      - `referenceAllele` (string)
      - `startPosition` (integer (int32))
  - `colocatedVariants` (array of object)
    - `dbSnpId` (string)
    - `gnomad_nfe_allele` (string, required) — GnomAD Non-Finnish European Allele
    - `gnomad_nfe_maf` (string, required) — GnomAD Non-Finnish European MAF
    - `gnomad_afr_allele` (string, required) — GnomAD African/African American Allele
    - `gnomad_afr_maf` (string, required) — GnomAD African/African American MAF
    - `gnomad_eas_allele` (string, required) — GnomAD East Asian Allele
    - `gnomad_eas_maf` (string, required) — GnomAD East Asian MAF
  - `end` (integer (int32)) — End position
  - `hgvsg` (string)
  - `hotspots` (object)
    - `annotation` (array of array of object)
      - `hugoSymbol` (string) — Hugo gene symbol
      - `inframeCount` (integer (int32)) — Inframe mutation count
      - `missenseCount` (integer (int32)) — Missense mutation count
      - `residue` (string) — Hotspot residue
      - `spliceCount` (integer (int32)) — Splice mutation count
      - `transcriptId` (string) — Ensembl Transcript Id
      - `truncatingCount` (integer (int32)) — Truncation mutation count
      - `tumorCount` (integer (int32)) — Tumor count
      - `type` (string) — Hotspot type
    - `license` (string)
  - `id` (string, required) — Variant id
  - `intergenic_consequences` (array of object, required) — intergenicConsequences
    - `impact` (string, required) — impact
    - `variantAllele` (string, required) — variant_allele
    - `consequenceTerms` (array of string, required) — consequence_terms
  - `most_severe_consequence` (string) — Most severe consequence
  - `mutation_assessor` (object)
    - `annotation` (object)
      - `codonStartPosition` (string) — Codon start position
      - `cosmicCount` (integer (int32)) — Number of mutations in COSMIC for this protein
      - `functionalImpact` (string) — Functional impact
      - `functionalImpactScore` (number (double)) — Functional impact score
      - `hgvs` (string)
      - `hugoSymbol` (string) — Hugo gene symbol
      - `input` (string, required) — User-input variants
      - `mappingIssue` (string) — Mapping issue info
      - `msaGaps` (number (double)) — Portion of gaps in variant position in multiple sequence alignment
      - `msaHeight` (integer (int32)) — Number of diverse sequences in multiple sequence alignment (identical or highly similar sequences filtered out)
      - `msaLink` (string) — Link to multiple sequence alignment
      - `pdbLink` (string) — Link to 3d structure browser
      - `referenceGenomeVariant` (string) — Reference genome variant
      - `referenceGenomeVariantType` (string) — Reference genome variant type
      - `refseqId` (string) — Refseq protein ID
      - `refseqPosition` (integer (int32)) — Variant position in Refseq protein, can be different from the one in Uniprot
      - `refseqResidue` (string) — Reference residue in Refseq protein, can be different from the one in Uniprot
      - `snpCount` (integer (int32)) — Number of SNPs in dbSNP for this protein
      - `uniprotId` (string) — Uniprot protein accession ID
      - `uniprotPosition` (integer (int32)) — Variant position in Uniprot protein, can be different from the one in Refseq
      - `uniprotResidue` (string) — Reference residue in Uniprot protein, can be different from the one in Refseq
      - `variant` (string) — Amino acid substitution
      - `variantConservationScore` (number (double)) — Variant conservation score
      - `variantSpecificityScore` (number (double)) — Variant specificity score
    - `license` (string)
  - `my_variant_info` (object)
    - `annotation` (object)
      - `clinVar` (object)
        - `alleleId` (integer (int32)) — allele_id
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `cytogenic` (string) — cytogenic
        - `gene` (object)
        - `hg19` (object)
        - `hg38` (object)
        - `hgvs` (object)
        - `license` (string) — license
        - `rcv` (array of object)
        - `variantId` (integer (int32)) — variant_id
      - `cosmic` (object)
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `cosmicId` (string) — cosmic_id
        - `hg19` (object)
        - `license` (string) — _license
        - `mutFreq` (number (double)) — mut_freq
        - `mutNt` (string) — mut_nt
        - `ref` (string) — ref
        - `tumorSite` (string) — tumor_site
      - `dbsnp` (object)
        - `_class` (string) — class
        - `alleleOrigin` (string) — allele_origin
        - `alleles` (array of object) — alleles
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `dbsnpBuild` (integer (int32)) — dbsnp_build
        - `flags` (array of string) — flags
        - `hg19` (object)
        - `license` (string) — _license
        - `ref` (string) — ref
        - `rsid` (string) — rsid
        - `validated` (boolean) — validated
        - `varSubtype` (string) — var_subtype
        - `vartype` (string) — vartype
      - `gnomadExome` (object)
        - `alleleCount` (object)
        - `alleleFrequency` (object)
        - `alleleNumber` (object)
        - `homozygotes` (object)
      - `gnomadGenome` (object)
        - `alleleCount` (object)
        - `alleleFrequency` (object)
        - `alleleNumber` (object)
        - `homozygotes` (object)
      - `hgvs` (string) — hgvs
      - `mutdb` (object)
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `cosmicId` (string) — cosmic_id
        - `hg19` (object)
        - `mutpredScore` (number (double)) — mutpred_score
        - `ref` (string) — ref
        - `rsid` (string) — rsid
        - `uniprotId` (string) — uniprot_id
      - `query` (string)
      - `snpeff` (object)
        - `license` (string) — license
      - `variant` (string) — variant
      - `vcf` (object)
        - `alt` (string) — alt
        - `position` (string) — position
        - `ref` (string) — ref
      - `version` (integer (int32)) — version
    - `license` (string)
  - `nucleotide_context` (object)
    - `annotation` (object)
      - `hgvs` (string)
      - `id` (string)
      - `molecule` (string)
      - `query` (string)
      - `seq` (string, required) — Nucleotide context sequence
    - `license` (string)
  - `oncokb` (object)
    - `annotation` (object)
      - `alleleExist` (boolean)
      - `dataVersion` (string)
      - `diagnosticImplications` (array of object)
        - `alterations` (array of string)
        - `description` (string)
        - `levelOfEvidence` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
        - `tumorType` (object) — OncoTree Detailed Cancer Type
      - `diagnosticSummary` (string)
      - `geneExist` (boolean)
      - `geneSummary` (string)
      - `highestDiagnosticImplicationLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `highestPrognosticImplicationLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `highestResistanceLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `highestSensitiveLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `hotspot` (boolean)
      - `lastUpdate` (string)
      - `mutationEffect` (object)
        - `citations` (object)
        - `description` (string)
        - `knownEffect` (string)
      - `oncogenic` (string)
      - `otherSignificantResistanceLevels` (array of string)
      - `otherSignificantSensitiveLevels` (array of string)
      - `prognosticImplications` (array of object)
        - `alterations` (array of string)
        - `description` (string)
        - `levelOfEvidence` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
        - `tumorType` (object) — OncoTree Detailed Cancer Type
      - `prognosticSummary` (string)
      - `query` (object)
        - `alteration` (string)
        - `alterationType` (string)
        - `consequence` (string)
        - `entrezGeneId` (integer (int32))
        - `hgvs` (string)
        - `hugoSymbol` (string)
        - `id` (string)
        - `proteinEnd` (integer (int32))
        - `proteinStart` (integer (int32))
        - `svType` (string) — Allowed values: `DELETION`, `TRANSLOCATION`, `DUPLICATION`, `INSERTION`, `INVERSION`, `FUSION`, `UNKNOWN`.
        - `tumorType` (string)
        - `type` (string)
      - `treatments` (array of object)
        - `abstracts` (array of object)
        - `alterations` (array of string)
        - `approvedIndications` (array of string)
        - `description` (string)
        - `drugs` (array of object)
        - `fdaApproved` (boolean)
        - `level` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
        - `levelAssociatedCancerType` (object) — OncoTree Detailed Cancer Type
        - `pmids` (array of string)
      - `tumorTypeSummary` (string)
      - `variantExist` (boolean)
      - `variantSummary` (string)
      - `vus` (boolean)
    - `license` (string)
  - `originalVariantQuery` (string, required) — Original variant query
  - `ptms` (object)
    - `annotation` (array of array of object)
      - `ensemblTranscriptIds` (array of string)
      - `position` (integer (int32))
      - `pubmedIds` (array of string)
      - `sequence` (string)
      - `type` (string)
      - `uniprotAccession` (string)
      - `uniprotEntry` (string)
    - `license` (string)
  - `seq_region_name` (string) — Chromosome
  - `signalAnnotation` (object)
    - `annotation` (array of object)
      - `biallelicCountsByTumorType` (array of object) — Biallelic Counts by Tumor Type
        - `tumorType` (string) — Tumor Type
        - `tumorTypeCount` (integer (int32)) — Sample count for Tumor Type
        - `variantCount` (integer (int32)) — Variant count for Tumor Type
      - `chromosome` (string) — Chromosome
      - `countsByTumorType` (array of object) — Counts by Tumor Type
        - `tumorType` (string) — Tumor Type
        - `tumorTypeCount` (integer (int32)) — Sample count for Tumor Type
        - `variantCount` (integer (int32)) — Variant count for Tumor Type
      - `endPosition` (integer (int64)) — End Position
      - `generalPopulationStats` (object)
        - `counts` (object)
        - `frequencies` (object)
      - `hugoGeneSymbol` (string) — Hugo Gene Symbol
      - `mskExperReview` (boolean) — Msk Expert Review
      - `mutationStatus` (string) — Mutation Status
      - `overallNumberOfGermlineHomozygous` (integer (int32))
      - `pathogenic` (string) — Pathogenic
      - `penetrance` (string) — Penetrance
      - `qcPassCountsByTumorType` (array of object) — QC Pass Counts by Tumor Type
        - `tumorType` (string) — Tumor Type
        - `tumorTypeCount` (integer (int32)) — Sample count for Tumor Type
        - `variantCount` (integer (int32)) — Variant count for Tumor Type
      - `referenceAllele` (string) — Reference Allele
      - `startPosition` (integer (int64)) — Start Position
      - `statsByTumorType` (array of object) — Stats By Tumor Type
        - `ageAtDx` (integer (int32)) — Median Age at Dx
        - `fBiallelic` (number (double)) — Frequency Of Biallelic
        - `fCancerTypeCount` (number (double)) — Frequency Of Cancer Type Count
        - `hrdScore` (object)
        - `msiScore` (number (double)) — Msi Score
        - `nCancerTypeCount` (integer (int32)) — Number Of Cancer Type Count
        - `numberOfGermlineHomozygous` (integer (int32)) — Number Of Germline Homozygous Per Tumor Type
        - `numberWithSig` (integer (int32)) — Number of Variants with Signature
        - `tmb` (number (double)) — Median TMB
        - `tumorType` (string) — Tumor Type
      - `variantAllele` (string) — Variant Allele
    - `license` (string)
  - `start` (integer (int32)) — Start position
  - `strand` (integer (int32)) — Strand (negative or positive)
  - `successfully_annotated` (boolean) — Status flag indicating whether variant was succesfully annotated
  - `transcript_consequences` (array of object) — List of transcripts
    - `amino_acids` (string) — Amino acids
    - `canonical` (string) — Canonical transcript indicator
    - `codons` (string) — Codons
    - `consequence_terms` (array of string) — List of consequence terms
    - `exon` (string)
    - `gene_id` (string) — Ensembl gene id
    - `gene_symbol` (string) — Hugo gene symbol
    - `hgnc_id` (string) — HGNC id
    - `hgvsc` (string) — HGVSc
    - `hgvsg` (string) — HGVSg
    - `hgvsp` (string) — HGVSp
    - `polyphen_prediction` (string) — Polyphen Prediction
    - `polyphen_score` (number (double)) — Polyphen Score
    - `protein_end` (integer (int32)) — Protein end position
    - `protein_id` (string) — Ensembl protein id
    - `protein_start` (integer (int32)) — Protein start position
    - `refseq_transcript_ids` (array of string) — List of RefSeq transcript ids
    - `sift_prediction` (string) — Sift Prediction
    - `sift_score` (number (double)) — Sift Score
    - `transcript_id` (string, required) — Ensembl transcript id
    - `uniprotId` (string)
    - `variant_allele` (string) — Variant allele
  - `variant` (string, required) — Variant key

### GET /annotation/dbsnp/{variantId}

**Retrieves VEP annotation for the give dbSNP id**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `variantId` | path | string | Yes | dbSNP id. For example rs116035550. |
| `isoformOverrideSource` | query | string | No | Isoform override source. For example uniprot |
| `token` | query | string | No | Map of tokens. For example {"source1":"put-your-token1-here","source2":"put-your-token2-here"} |
| `fields` | query | array of string | No | Comma separated list of fields to include (case-sensitive!). For example: annotation_summary |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `allele_string` (string) — Allele string (e.g: A/T)
  - `annotationJSON` (string) — Annotation data as JSON string
  - `annotation_summary` (object)
    - `assemblyName` (string) — Assembly name
    - `canonicalTranscriptId` (string) — Canonical transcript id
    - `genomicLocation` (object)
      - `chromosome` (string, required) — Chromosome
      - `start` (integer (int32), required) — Start Position
      - `end` (integer (int32), required) — End Position
      - `referenceAllele` (string, required) — Reference Allele
      - `variantAllele` (string, required) — Variant Allele
    - `strandSign` (string) — Strand (- or +)
    - `transcriptConsequenceSummaries` (array of object, required) — All transcript consequence summaries
      - `aminoAcidAlt` (string) — Alt Amino Acid
      - `aminoAcidRef` (string) — Reference Amino Acid
      - `aminoAcids` (string) — Amino acids change
      - `codonChange` (string) — Codon change
      - `consequenceTerms` (string) — Consequence terms (comma separated)
      - `entrezGeneId` (string) — Entrez gene id
      - `exon` (string)
      - `hgvsc` (string) — HGVSc
      - `hgvsp` (string) — HGVSp
      - `hgvspShort` (string) — HGVSp short
      - `hugoGeneSymbol` (string) — Hugo gene symbol
      - `polyphenPrediction` (string) — Polyphen Prediction
      - `polyphenScore` (number (double)) — Polyphen Score
      - `proteinPosition` (object)
        - `end` (integer (int32))
        - `start` (integer (int32))
      - `refSeq` (string) — RefSeq id
      - `siftPrediction` (string) — Sift Prediction
      - `siftScore` (number (double)) — Sift Score
      - `transcriptId` (string, required) — Transcript id
      - `uniprotId` (string) — Uniprot ID
      - `variantClassification` (string) — Variant classification
    - `transcriptConsequenceSummary` (object, required)
      - `aminoAcidAlt` (string) — Alt Amino Acid
      - `aminoAcidRef` (string) — Reference Amino Acid
      - `aminoAcids` (string) — Amino acids change
      - `codonChange` (string) — Codon change
      - `consequenceTerms` (string) — Consequence terms (comma separated)
      - `entrezGeneId` (string) — Entrez gene id
      - `exon` (string)
      - `hgvsc` (string) — HGVSc
      - `hgvsp` (string) — HGVSp
      - `hgvspShort` (string) — HGVSp short
      - `hugoGeneSymbol` (string) — Hugo gene symbol
      - `polyphenPrediction` (string) — Polyphen Prediction
      - `polyphenScore` (number (double)) — Polyphen Score
      - `proteinPosition` (object)
        - `end` (integer (int32))
        - `start` (integer (int32))
      - `refSeq` (string) — RefSeq id
      - `siftPrediction` (string) — Sift Prediction
      - `siftScore` (number (double)) — Sift Score
      - `transcriptId` (string, required) — Transcript id
      - `uniprotId` (string) — Uniprot ID
      - `variantClassification` (string) — Variant classification
    - `transcriptConsequences` (array of object, required) — (Deprecated) Transcript consequence summaries (list of one when using annotation/, multiple when using annotation/summary/
      - `aminoAcidAlt` (string) — Alt Amino Acid
      - `aminoAcidRef` (string) — Reference Amino Acid
      - `aminoAcids` (string) — Amino acids change
      - `codonChange` (string) — Codon change
      - `consequenceTerms` (string) — Consequence terms (comma separated)
      - `entrezGeneId` (string) — Entrez gene id
      - `exon` (string)
      - `hgvsc` (string) — HGVSc
      - `hgvsp` (string) — HGVSp
      - `hgvspShort` (string) — HGVSp short
      - `hugoGeneSymbol` (string) — Hugo gene symbol
      - `polyphenPrediction` (string) — Polyphen Prediction
      - `polyphenScore` (number (double)) — Polyphen Score
      - `proteinPosition` (object)
        - `end` (integer (int32))
        - `start` (integer (int32))
      - `refSeq` (string) — RefSeq id
      - `siftPrediction` (string) — Sift Prediction
      - `siftScore` (number (double)) — Sift Score
      - `transcriptId` (string, required) — Transcript id
      - `uniprotId` (string) — Uniprot ID
      - `variantClassification` (string) — Variant classification
    - `variant` (string, required) — Variant key
    - `variantType` (string) — Variant type
  - `assembly_name` (string) — NCBI build number
  - `clinvar` (object)
    - `annotation` (object)
      - `alternateAllele` (string)
      - `chromosome` (string)
      - `clinicalSignificance` (string)
      - `clinvarId` (integer (int32))
      - `conflictingClinicalSignificance` (string)
      - `endPosition` (integer (int32))
      - `referenceAllele` (string)
      - `startPosition` (integer (int32))
  - `colocatedVariants` (array of object)
    - `dbSnpId` (string)
    - `gnomad_nfe_allele` (string, required) — GnomAD Non-Finnish European Allele
    - `gnomad_nfe_maf` (string, required) — GnomAD Non-Finnish European MAF
    - `gnomad_afr_allele` (string, required) — GnomAD African/African American Allele
    - `gnomad_afr_maf` (string, required) — GnomAD African/African American MAF
    - `gnomad_eas_allele` (string, required) — GnomAD East Asian Allele
    - `gnomad_eas_maf` (string, required) — GnomAD East Asian MAF
  - `end` (integer (int32)) — End position
  - `hgvsg` (string)
  - `hotspots` (object)
    - `annotation` (array of array of object)
      - `hugoSymbol` (string) — Hugo gene symbol
      - `inframeCount` (integer (int32)) — Inframe mutation count
      - `missenseCount` (integer (int32)) — Missense mutation count
      - `residue` (string) — Hotspot residue
      - `spliceCount` (integer (int32)) — Splice mutation count
      - `transcriptId` (string) — Ensembl Transcript Id
      - `truncatingCount` (integer (int32)) — Truncation mutation count
      - `tumorCount` (integer (int32)) — Tumor count
      - `type` (string) — Hotspot type
    - `license` (string)
  - `id` (string, required) — Variant id
  - `intergenic_consequences` (array of object, required) — intergenicConsequences
    - `impact` (string, required) — impact
    - `variantAllele` (string, required) — variant_allele
    - `consequenceTerms` (array of string, required) — consequence_terms
  - `most_severe_consequence` (string) — Most severe consequence
  - `mutation_assessor` (object)
    - `annotation` (object)
      - `codonStartPosition` (string) — Codon start position
      - `cosmicCount` (integer (int32)) — Number of mutations in COSMIC for this protein
      - `functionalImpact` (string) — Functional impact
      - `functionalImpactScore` (number (double)) — Functional impact score
      - `hgvs` (string)
      - `hugoSymbol` (string) — Hugo gene symbol
      - `input` (string, required) — User-input variants
      - `mappingIssue` (string) — Mapping issue info
      - `msaGaps` (number (double)) — Portion of gaps in variant position in multiple sequence alignment
      - `msaHeight` (integer (int32)) — Number of diverse sequences in multiple sequence alignment (identical or highly similar sequences filtered out)
      - `msaLink` (string) — Link to multiple sequence alignment
      - `pdbLink` (string) — Link to 3d structure browser
      - `referenceGenomeVariant` (string) — Reference genome variant
      - `referenceGenomeVariantType` (string) — Reference genome variant type
      - `refseqId` (string) — Refseq protein ID
      - `refseqPosition` (integer (int32)) — Variant position in Refseq protein, can be different from the one in Uniprot
      - `refseqResidue` (string) — Reference residue in Refseq protein, can be different from the one in Uniprot
      - `snpCount` (integer (int32)) — Number of SNPs in dbSNP for this protein
      - `uniprotId` (string) — Uniprot protein accession ID
      - `uniprotPosition` (integer (int32)) — Variant position in Uniprot protein, can be different from the one in Refseq
      - `uniprotResidue` (string) — Reference residue in Uniprot protein, can be different from the one in Refseq
      - `variant` (string) — Amino acid substitution
      - `variantConservationScore` (number (double)) — Variant conservation score
      - `variantSpecificityScore` (number (double)) — Variant specificity score
    - `license` (string)
  - `my_variant_info` (object)
    - `annotation` (object)
      - `clinVar` (object)
        - `alleleId` (integer (int32)) — allele_id
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `cytogenic` (string) — cytogenic
        - `gene` (object)
        - `hg19` (object)
        - `hg38` (object)
        - `hgvs` (object)
        - `license` (string) — license
        - `rcv` (array of object)
        - `variantId` (integer (int32)) — variant_id
      - `cosmic` (object)
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `cosmicId` (string) — cosmic_id
        - `hg19` (object)
        - `license` (string) — _license
        - `mutFreq` (number (double)) — mut_freq
        - `mutNt` (string) — mut_nt
        - `ref` (string) — ref
        - `tumorSite` (string) — tumor_site
      - `dbsnp` (object)
        - `_class` (string) — class
        - `alleleOrigin` (string) — allele_origin
        - `alleles` (array of object) — alleles
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `dbsnpBuild` (integer (int32)) — dbsnp_build
        - `flags` (array of string) — flags
        - `hg19` (object)
        - `license` (string) — _license
        - `ref` (string) — ref
        - `rsid` (string) — rsid
        - `validated` (boolean) — validated
        - `varSubtype` (string) — var_subtype
        - `vartype` (string) — vartype
      - `gnomadExome` (object)
        - `alleleCount` (object)
        - `alleleFrequency` (object)
        - `alleleNumber` (object)
        - `homozygotes` (object)
      - `gnomadGenome` (object)
        - `alleleCount` (object)
        - `alleleFrequency` (object)
        - `alleleNumber` (object)
        - `homozygotes` (object)
      - `hgvs` (string) — hgvs
      - `mutdb` (object)
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `cosmicId` (string) — cosmic_id
        - `hg19` (object)
        - `mutpredScore` (number (double)) — mutpred_score
        - `ref` (string) — ref
        - `rsid` (string) — rsid
        - `uniprotId` (string) — uniprot_id
      - `query` (string)
      - `snpeff` (object)
        - `license` (string) — license
      - `variant` (string) — variant
      - `vcf` (object)
        - `alt` (string) — alt
        - `position` (string) — position
        - `ref` (string) — ref
      - `version` (integer (int32)) — version
    - `license` (string)
  - `nucleotide_context` (object)
    - `annotation` (object)
      - `hgvs` (string)
      - `id` (string)
      - `molecule` (string)
      - `query` (string)
      - `seq` (string, required) — Nucleotide context sequence
    - `license` (string)
  - `oncokb` (object)
    - `annotation` (object)
      - `alleleExist` (boolean)
      - `dataVersion` (string)
      - `diagnosticImplications` (array of object)
        - `alterations` (array of string)
        - `description` (string)
        - `levelOfEvidence` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
        - `tumorType` (object) — OncoTree Detailed Cancer Type
      - `diagnosticSummary` (string)
      - `geneExist` (boolean)
      - `geneSummary` (string)
      - `highestDiagnosticImplicationLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `highestPrognosticImplicationLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `highestResistanceLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `highestSensitiveLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `hotspot` (boolean)
      - `lastUpdate` (string)
      - `mutationEffect` (object)
        - `citations` (object)
        - `description` (string)
        - `knownEffect` (string)
      - `oncogenic` (string)
      - `otherSignificantResistanceLevels` (array of string)
      - `otherSignificantSensitiveLevels` (array of string)
      - `prognosticImplications` (array of object)
        - `alterations` (array of string)
        - `description` (string)
        - `levelOfEvidence` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
        - `tumorType` (object) — OncoTree Detailed Cancer Type
      - `prognosticSummary` (string)
      - `query` (object)
        - `alteration` (string)
        - `alterationType` (string)
        - `consequence` (string)
        - `entrezGeneId` (integer (int32))
        - `hgvs` (string)
        - `hugoSymbol` (string)
        - `id` (string)
        - `proteinEnd` (integer (int32))
        - `proteinStart` (integer (int32))
        - `svType` (string) — Allowed values: `DELETION`, `TRANSLOCATION`, `DUPLICATION`, `INSERTION`, `INVERSION`, `FUSION`, `UNKNOWN`.
        - `tumorType` (string)
        - `type` (string)
      - `treatments` (array of object)
        - `abstracts` (array of object)
        - `alterations` (array of string)
        - `approvedIndications` (array of string)
        - `description` (string)
        - `drugs` (array of object)
        - `fdaApproved` (boolean)
        - `level` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
        - `levelAssociatedCancerType` (object) — OncoTree Detailed Cancer Type
        - `pmids` (array of string)
      - `tumorTypeSummary` (string)
      - `variantExist` (boolean)
      - `variantSummary` (string)
      - `vus` (boolean)
    - `license` (string)
  - `originalVariantQuery` (string, required) — Original variant query
  - `ptms` (object)
    - `annotation` (array of array of object)
      - `ensemblTranscriptIds` (array of string)
      - `position` (integer (int32))
      - `pubmedIds` (array of string)
      - `sequence` (string)
      - `type` (string)
      - `uniprotAccession` (string)
      - `uniprotEntry` (string)
    - `license` (string)
  - `seq_region_name` (string) — Chromosome
  - `signalAnnotation` (object)
    - `annotation` (array of object)
      - `biallelicCountsByTumorType` (array of object) — Biallelic Counts by Tumor Type
        - `tumorType` (string) — Tumor Type
        - `tumorTypeCount` (integer (int32)) — Sample count for Tumor Type
        - `variantCount` (integer (int32)) — Variant count for Tumor Type
      - `chromosome` (string) — Chromosome
      - `countsByTumorType` (array of object) — Counts by Tumor Type
        - `tumorType` (string) — Tumor Type
        - `tumorTypeCount` (integer (int32)) — Sample count for Tumor Type
        - `variantCount` (integer (int32)) — Variant count for Tumor Type
      - `endPosition` (integer (int64)) — End Position
      - `generalPopulationStats` (object)
        - `counts` (object)
        - `frequencies` (object)
      - `hugoGeneSymbol` (string) — Hugo Gene Symbol
      - `mskExperReview` (boolean) — Msk Expert Review
      - `mutationStatus` (string) — Mutation Status
      - `overallNumberOfGermlineHomozygous` (integer (int32))
      - `pathogenic` (string) — Pathogenic
      - `penetrance` (string) — Penetrance
      - `qcPassCountsByTumorType` (array of object) — QC Pass Counts by Tumor Type
        - `tumorType` (string) — Tumor Type
        - `tumorTypeCount` (integer (int32)) — Sample count for Tumor Type
        - `variantCount` (integer (int32)) — Variant count for Tumor Type
      - `referenceAllele` (string) — Reference Allele
      - `startPosition` (integer (int64)) — Start Position
      - `statsByTumorType` (array of object) — Stats By Tumor Type
        - `ageAtDx` (integer (int32)) — Median Age at Dx
        - `fBiallelic` (number (double)) — Frequency Of Biallelic
        - `fCancerTypeCount` (number (double)) — Frequency Of Cancer Type Count
        - `hrdScore` (object)
        - `msiScore` (number (double)) — Msi Score
        - `nCancerTypeCount` (integer (int32)) — Number Of Cancer Type Count
        - `numberOfGermlineHomozygous` (integer (int32)) — Number Of Germline Homozygous Per Tumor Type
        - `numberWithSig` (integer (int32)) — Number of Variants with Signature
        - `tmb` (number (double)) — Median TMB
        - `tumorType` (string) — Tumor Type
      - `variantAllele` (string) — Variant Allele
    - `license` (string)
  - `start` (integer (int32)) — Start position
  - `strand` (integer (int32)) — Strand (negative or positive)
  - `successfully_annotated` (boolean) — Status flag indicating whether variant was succesfully annotated
  - `transcript_consequences` (array of object) — List of transcripts
    - `amino_acids` (string) — Amino acids
    - `canonical` (string) — Canonical transcript indicator
    - `codons` (string) — Codons
    - `consequence_terms` (array of string) — List of consequence terms
    - `exon` (string)
    - `gene_id` (string) — Ensembl gene id
    - `gene_symbol` (string) — Hugo gene symbol
    - `hgnc_id` (string) — HGNC id
    - `hgvsc` (string) — HGVSc
    - `hgvsg` (string) — HGVSg
    - `hgvsp` (string) — HGVSp
    - `polyphen_prediction` (string) — Polyphen Prediction
    - `polyphen_score` (number (double)) — Polyphen Score
    - `protein_end` (integer (int32)) — Protein end position
    - `protein_id` (string) — Ensembl protein id
    - `protein_start` (integer (int32)) — Protein start position
    - `refseq_transcript_ids` (array of string) — List of RefSeq transcript ids
    - `sift_prediction` (string) — Sift Prediction
    - `sift_score` (number (double)) — Sift Score
    - `transcript_id` (string, required) — Ensembl transcript id
    - `uniprotId` (string)
    - `variant_allele` (string) — Variant allele
  - `variant` (string, required) — Variant key

### POST /annotation/genomic

**Retrieves VEP annotation for the provided list of genomic locations**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `isoformOverrideSource` | query | string | No | Isoform override source. For example uniprot |
| `token` | query | string | No | Map of tokens. For example {"source1":"put-your-token1-here","source2":"put-your-token2-here"} |
| `fields` | query | array of string | No | Comma separated list of fields to include (case-sensitive!). For example: hotspots |

**Request body** (`application/json`, required)

List of Genomic Locations

- `chromosome` (string, required) — Chromosome
- `start` (integer (int32), required) — Start Position
- `end` (integer (int32), required) — End Position
- `referenceAllele` (string, required) — Reference Allele
- `variantAllele` (string, required) — Variant Allele

**Responses**

- **200** — OK
  Body (`application/json`, array of object):
  - `allele_string` (string) — Allele string (e.g: A/T)
  - `annotationJSON` (string) — Annotation data as JSON string
  - `annotation_summary` (object)
    - `assemblyName` (string) — Assembly name
    - `canonicalTranscriptId` (string) — Canonical transcript id
    - `genomicLocation` (object)
      - `chromosome` (string, required) — Chromosome
      - `start` (integer (int32), required) — Start Position
      - `end` (integer (int32), required) — End Position
      - `referenceAllele` (string, required) — Reference Allele
      - `variantAllele` (string, required) — Variant Allele
    - `strandSign` (string) — Strand (- or +)
    - `transcriptConsequenceSummaries` (array of object, required) — All transcript consequence summaries
      - `aminoAcidAlt` (string) — Alt Amino Acid
      - `aminoAcidRef` (string) — Reference Amino Acid
      - `aminoAcids` (string) — Amino acids change
      - `codonChange` (string) — Codon change
      - `consequenceTerms` (string) — Consequence terms (comma separated)
      - `entrezGeneId` (string) — Entrez gene id
      - `exon` (string)
      - `hgvsc` (string) — HGVSc
      - `hgvsp` (string) — HGVSp
      - `hgvspShort` (string) — HGVSp short
      - `hugoGeneSymbol` (string) — Hugo gene symbol
      - `polyphenPrediction` (string) — Polyphen Prediction
      - `polyphenScore` (number (double)) — Polyphen Score
      - `proteinPosition` (object)
        - `end` (integer (int32))
        - `start` (integer (int32))
      - `refSeq` (string) — RefSeq id
      - `siftPrediction` (string) — Sift Prediction
      - `siftScore` (number (double)) — Sift Score
      - `transcriptId` (string, required) — Transcript id
      - `uniprotId` (string) — Uniprot ID
      - `variantClassification` (string) — Variant classification
    - `transcriptConsequenceSummary` (object, required)
      - `aminoAcidAlt` (string) — Alt Amino Acid
      - `aminoAcidRef` (string) — Reference Amino Acid
      - `aminoAcids` (string) — Amino acids change
      - `codonChange` (string) — Codon change
      - `consequenceTerms` (string) — Consequence terms (comma separated)
      - `entrezGeneId` (string) — Entrez gene id
      - `exon` (string)
      - `hgvsc` (string) — HGVSc
      - `hgvsp` (string) — HGVSp
      - `hgvspShort` (string) — HGVSp short
      - `hugoGeneSymbol` (string) — Hugo gene symbol
      - `polyphenPrediction` (string) — Polyphen Prediction
      - `polyphenScore` (number (double)) — Polyphen Score
      - `proteinPosition` (object)
        - `end` (integer (int32))
        - `start` (integer (int32))
      - `refSeq` (string) — RefSeq id
      - `siftPrediction` (string) — Sift Prediction
      - `siftScore` (number (double)) — Sift Score
      - `transcriptId` (string, required) — Transcript id
      - `uniprotId` (string) — Uniprot ID
      - `variantClassification` (string) — Variant classification
    - `transcriptConsequences` (array of object, required) — (Deprecated) Transcript consequence summaries (list of one when using annotation/, multiple when using annotation/summary/
      - `aminoAcidAlt` (string) — Alt Amino Acid
      - `aminoAcidRef` (string) — Reference Amino Acid
      - `aminoAcids` (string) — Amino acids change
      - `codonChange` (string) — Codon change
      - `consequenceTerms` (string) — Consequence terms (comma separated)
      - `entrezGeneId` (string) — Entrez gene id
      - `exon` (string)
      - `hgvsc` (string) — HGVSc
      - `hgvsp` (string) — HGVSp
      - `hgvspShort` (string) — HGVSp short
      - `hugoGeneSymbol` (string) — Hugo gene symbol
      - `polyphenPrediction` (string) — Polyphen Prediction
      - `polyphenScore` (number (double)) — Polyphen Score
      - `proteinPosition` (object)
        - `end` (integer (int32))
        - `start` (integer (int32))
      - `refSeq` (string) — RefSeq id
      - `siftPrediction` (string) — Sift Prediction
      - `siftScore` (number (double)) — Sift Score
      - `transcriptId` (string, required) — Transcript id
      - `uniprotId` (string) — Uniprot ID
      - `variantClassification` (string) — Variant classification
    - `variant` (string, required) — Variant key
    - `variantType` (string) — Variant type
  - `assembly_name` (string) — NCBI build number
  - `clinvar` (object)
    - `annotation` (object)
      - `alternateAllele` (string)
      - `chromosome` (string)
      - `clinicalSignificance` (string)
      - `clinvarId` (integer (int32))
      - `conflictingClinicalSignificance` (string)
      - `endPosition` (integer (int32))
      - `referenceAllele` (string)
      - `startPosition` (integer (int32))
  - `colocatedVariants` (array of object)
    - `dbSnpId` (string)
    - `gnomad_nfe_allele` (string, required) — GnomAD Non-Finnish European Allele
    - `gnomad_nfe_maf` (string, required) — GnomAD Non-Finnish European MAF
    - `gnomad_afr_allele` (string, required) — GnomAD African/African American Allele
    - `gnomad_afr_maf` (string, required) — GnomAD African/African American MAF
    - `gnomad_eas_allele` (string, required) — GnomAD East Asian Allele
    - `gnomad_eas_maf` (string, required) — GnomAD East Asian MAF
  - `end` (integer (int32)) — End position
  - `hgvsg` (string)
  - `hotspots` (object)
    - `annotation` (array of array of object)
      - `hugoSymbol` (string) — Hugo gene symbol
      - `inframeCount` (integer (int32)) — Inframe mutation count
      - `missenseCount` (integer (int32)) — Missense mutation count
      - `residue` (string) — Hotspot residue
      - `spliceCount` (integer (int32)) — Splice mutation count
      - `transcriptId` (string) — Ensembl Transcript Id
      - `truncatingCount` (integer (int32)) — Truncation mutation count
      - `tumorCount` (integer (int32)) — Tumor count
      - `type` (string) — Hotspot type
    - `license` (string)
  - `id` (string, required) — Variant id
  - `intergenic_consequences` (array of object, required) — intergenicConsequences
    - `impact` (string, required) — impact
    - `variantAllele` (string, required) — variant_allele
    - `consequenceTerms` (array of string, required) — consequence_terms
  - `most_severe_consequence` (string) — Most severe consequence
  - `mutation_assessor` (object)
    - `annotation` (object)
      - `codonStartPosition` (string) — Codon start position
      - `cosmicCount` (integer (int32)) — Number of mutations in COSMIC for this protein
      - `functionalImpact` (string) — Functional impact
      - `functionalImpactScore` (number (double)) — Functional impact score
      - `hgvs` (string)
      - `hugoSymbol` (string) — Hugo gene symbol
      - `input` (string, required) — User-input variants
      - `mappingIssue` (string) — Mapping issue info
      - `msaGaps` (number (double)) — Portion of gaps in variant position in multiple sequence alignment
      - `msaHeight` (integer (int32)) — Number of diverse sequences in multiple sequence alignment (identical or highly similar sequences filtered out)
      - `msaLink` (string) — Link to multiple sequence alignment
      - `pdbLink` (string) — Link to 3d structure browser
      - `referenceGenomeVariant` (string) — Reference genome variant
      - `referenceGenomeVariantType` (string) — Reference genome variant type
      - `refseqId` (string) — Refseq protein ID
      - `refseqPosition` (integer (int32)) — Variant position in Refseq protein, can be different from the one in Uniprot
      - `refseqResidue` (string) — Reference residue in Refseq protein, can be different from the one in Uniprot
      - `snpCount` (integer (int32)) — Number of SNPs in dbSNP for this protein
      - `uniprotId` (string) — Uniprot protein accession ID
      - `uniprotPosition` (integer (int32)) — Variant position in Uniprot protein, can be different from the one in Refseq
      - `uniprotResidue` (string) — Reference residue in Uniprot protein, can be different from the one in Refseq
      - `variant` (string) — Amino acid substitution
      - `variantConservationScore` (number (double)) — Variant conservation score
      - `variantSpecificityScore` (number (double)) — Variant specificity score
    - `license` (string)
  - `my_variant_info` (object)
    - `annotation` (object)
      - `clinVar` (object)
        - `alleleId` (integer (int32)) — allele_id
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `cytogenic` (string) — cytogenic
        - `gene` (object)
        - `hg19` (object)
        - `hg38` (object)
        - `hgvs` (object)
        - `license` (string) — license
        - `rcv` (array of object)
        - `variantId` (integer (int32)) — variant_id
      - `cosmic` (object)
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `cosmicId` (string) — cosmic_id
        - `hg19` (object)
        - `license` (string) — _license
        - `mutFreq` (number (double)) — mut_freq
        - `mutNt` (string) — mut_nt
        - `ref` (string) — ref
        - `tumorSite` (string) — tumor_site
      - `dbsnp` (object)
        - `_class` (string) — class
        - `alleleOrigin` (string) — allele_origin
        - `alleles` (array of object) — alleles
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `dbsnpBuild` (integer (int32)) — dbsnp_build
        - `flags` (array of string) — flags
        - `hg19` (object)
        - `license` (string) — _license
        - `ref` (string) — ref
        - `rsid` (string) — rsid
        - `validated` (boolean) — validated
        - `varSubtype` (string) — var_subtype
        - `vartype` (string) — vartype
      - `gnomadExome` (object)
        - `alleleCount` (object)
        - `alleleFrequency` (object)
        - `alleleNumber` (object)
        - `homozygotes` (object)
      - `gnomadGenome` (object)
        - `alleleCount` (object)
        - `alleleFrequency` (object)
        - `alleleNumber` (object)
        - `homozygotes` (object)
      - `hgvs` (string) — hgvs
      - `mutdb` (object)
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `cosmicId` (string) — cosmic_id
        - `hg19` (object)
        - `mutpredScore` (number (double)) — mutpred_score
        - `ref` (string) — ref
        - `rsid` (string) — rsid
        - `uniprotId` (string) — uniprot_id
      - `query` (string)
      - `snpeff` (object)
        - `license` (string) — license
      - `variant` (string) — variant
      - `vcf` (object)
        - `alt` (string) — alt
        - `position` (string) — position
        - `ref` (string) — ref
      - `version` (integer (int32)) — version
    - `license` (string)
  - `nucleotide_context` (object)
    - `annotation` (object)
      - `hgvs` (string)
      - `id` (string)
      - `molecule` (string)
      - `query` (string)
      - `seq` (string, required) — Nucleotide context sequence
    - `license` (string)
  - `oncokb` (object)
    - `annotation` (object)
      - `alleleExist` (boolean)
      - `dataVersion` (string)
      - `diagnosticImplications` (array of object)
        - `alterations` (array of string)
        - `description` (string)
        - `levelOfEvidence` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
        - `tumorType` (object) — OncoTree Detailed Cancer Type
      - `diagnosticSummary` (string)
      - `geneExist` (boolean)
      - `geneSummary` (string)
      - `highestDiagnosticImplicationLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `highestPrognosticImplicationLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `highestResistanceLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `highestSensitiveLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `hotspot` (boolean)
      - `lastUpdate` (string)
      - `mutationEffect` (object)
        - `citations` (object)
        - `description` (string)
        - `knownEffect` (string)
      - `oncogenic` (string)
      - `otherSignificantResistanceLevels` (array of string)
      - `otherSignificantSensitiveLevels` (array of string)
      - `prognosticImplications` (array of object)
        - `alterations` (array of string)
        - `description` (string)
        - `levelOfEvidence` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
        - `tumorType` (object) — OncoTree Detailed Cancer Type
      - `prognosticSummary` (string)
      - `query` (object)
        - `alteration` (string)
        - `alterationType` (string)
        - `consequence` (string)
        - `entrezGeneId` (integer (int32))
        - `hgvs` (string)
        - `hugoSymbol` (string)
        - `id` (string)
        - `proteinEnd` (integer (int32))
        - `proteinStart` (integer (int32))
        - `svType` (string) — Allowed values: `DELETION`, `TRANSLOCATION`, `DUPLICATION`, `INSERTION`, `INVERSION`, `FUSION`, `UNKNOWN`.
        - `tumorType` (string)
        - `type` (string)
      - `treatments` (array of object)
        - `abstracts` (array of object)
        - `alterations` (array of string)
        - `approvedIndications` (array of string)
        - `description` (string)
        - `drugs` (array of object)
        - `fdaApproved` (boolean)
        - `level` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
        - `levelAssociatedCancerType` (object) — OncoTree Detailed Cancer Type
        - `pmids` (array of string)
      - `tumorTypeSummary` (string)
      - `variantExist` (boolean)
      - `variantSummary` (string)
      - `vus` (boolean)
    - `license` (string)
  - `originalVariantQuery` (string, required) — Original variant query
  - `ptms` (object)
    - `annotation` (array of array of object)
      - `ensemblTranscriptIds` (array of string)
      - `position` (integer (int32))
      - `pubmedIds` (array of string)
      - `sequence` (string)
      - `type` (string)
      - `uniprotAccession` (string)
      - `uniprotEntry` (string)
    - `license` (string)
  - `seq_region_name` (string) — Chromosome
  - `signalAnnotation` (object)
    - `annotation` (array of object)
      - `biallelicCountsByTumorType` (array of object) — Biallelic Counts by Tumor Type
        - `tumorType` (string) — Tumor Type
        - `tumorTypeCount` (integer (int32)) — Sample count for Tumor Type
        - `variantCount` (integer (int32)) — Variant count for Tumor Type
      - `chromosome` (string) — Chromosome
      - `countsByTumorType` (array of object) — Counts by Tumor Type
        - `tumorType` (string) — Tumor Type
        - `tumorTypeCount` (integer (int32)) — Sample count for Tumor Type
        - `variantCount` (integer (int32)) — Variant count for Tumor Type
      - `endPosition` (integer (int64)) — End Position
      - `generalPopulationStats` (object)
        - `counts` (object)
        - `frequencies` (object)
      - `hugoGeneSymbol` (string) — Hugo Gene Symbol
      - `mskExperReview` (boolean) — Msk Expert Review
      - `mutationStatus` (string) — Mutation Status
      - `overallNumberOfGermlineHomozygous` (integer (int32))
      - `pathogenic` (string) — Pathogenic
      - `penetrance` (string) — Penetrance
      - `qcPassCountsByTumorType` (array of object) — QC Pass Counts by Tumor Type
        - `tumorType` (string) — Tumor Type
        - `tumorTypeCount` (integer (int32)) — Sample count for Tumor Type
        - `variantCount` (integer (int32)) — Variant count for Tumor Type
      - `referenceAllele` (string) — Reference Allele
      - `startPosition` (integer (int64)) — Start Position
      - `statsByTumorType` (array of object) — Stats By Tumor Type
        - `ageAtDx` (integer (int32)) — Median Age at Dx
        - `fBiallelic` (number (double)) — Frequency Of Biallelic
        - `fCancerTypeCount` (number (double)) — Frequency Of Cancer Type Count
        - `hrdScore` (object)
        - `msiScore` (number (double)) — Msi Score
        - `nCancerTypeCount` (integer (int32)) — Number Of Cancer Type Count
        - `numberOfGermlineHomozygous` (integer (int32)) — Number Of Germline Homozygous Per Tumor Type
        - `numberWithSig` (integer (int32)) — Number of Variants with Signature
        - `tmb` (number (double)) — Median TMB
        - `tumorType` (string) — Tumor Type
      - `variantAllele` (string) — Variant Allele
    - `license` (string)
  - `start` (integer (int32)) — Start position
  - `strand` (integer (int32)) — Strand (negative or positive)
  - `successfully_annotated` (boolean) — Status flag indicating whether variant was succesfully annotated
  - `transcript_consequences` (array of object) — List of transcripts
    - `amino_acids` (string) — Amino acids
    - `canonical` (string) — Canonical transcript indicator
    - `codons` (string) — Codons
    - `consequence_terms` (array of string) — List of consequence terms
    - `exon` (string)
    - `gene_id` (string) — Ensembl gene id
    - `gene_symbol` (string) — Hugo gene symbol
    - `hgnc_id` (string) — HGNC id
    - `hgvsc` (string) — HGVSc
    - `hgvsg` (string) — HGVSg
    - `hgvsp` (string) — HGVSp
    - `polyphen_prediction` (string) — Polyphen Prediction
    - `polyphen_score` (number (double)) — Polyphen Score
    - `protein_end` (integer (int32)) — Protein end position
    - `protein_id` (string) — Ensembl protein id
    - `protein_start` (integer (int32)) — Protein start position
    - `refseq_transcript_ids` (array of string) — List of RefSeq transcript ids
    - `sift_prediction` (string) — Sift Prediction
    - `sift_score` (number (double)) — Sift Score
    - `transcript_id` (string, required) — Ensembl transcript id
    - `uniprotId` (string)
    - `variant_allele` (string) — Variant allele
  - `variant` (string, required) — Variant key

### GET /annotation/genomic/{genomicLocation}

**Retrieves VEP annotation for the provided genomic location**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `genomicLocation` | path | string | Yes | A genomic location. For example 7,140453136,140453136,A,T |
| `isoformOverrideSource` | query | string | No | Isoform override source. For example uniprot |
| `token` | query | string | No | Map of tokens. For example {"source1":"put-your-token1-here","source2":"put-your-token2-here"} |
| `fields` | query | array of string | No | Comma separated list of fields to include (case-sensitive!). For example: hotspots |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `allele_string` (string) — Allele string (e.g: A/T)
  - `annotationJSON` (string) — Annotation data as JSON string
  - `annotation_summary` (object)
    - `assemblyName` (string) — Assembly name
    - `canonicalTranscriptId` (string) — Canonical transcript id
    - `genomicLocation` (object)
      - `chromosome` (string, required) — Chromosome
      - `start` (integer (int32), required) — Start Position
      - `end` (integer (int32), required) — End Position
      - `referenceAllele` (string, required) — Reference Allele
      - `variantAllele` (string, required) — Variant Allele
    - `strandSign` (string) — Strand (- or +)
    - `transcriptConsequenceSummaries` (array of object, required) — All transcript consequence summaries
      - `aminoAcidAlt` (string) — Alt Amino Acid
      - `aminoAcidRef` (string) — Reference Amino Acid
      - `aminoAcids` (string) — Amino acids change
      - `codonChange` (string) — Codon change
      - `consequenceTerms` (string) — Consequence terms (comma separated)
      - `entrezGeneId` (string) — Entrez gene id
      - `exon` (string)
      - `hgvsc` (string) — HGVSc
      - `hgvsp` (string) — HGVSp
      - `hgvspShort` (string) — HGVSp short
      - `hugoGeneSymbol` (string) — Hugo gene symbol
      - `polyphenPrediction` (string) — Polyphen Prediction
      - `polyphenScore` (number (double)) — Polyphen Score
      - `proteinPosition` (object)
        - `end` (integer (int32))
        - `start` (integer (int32))
      - `refSeq` (string) — RefSeq id
      - `siftPrediction` (string) — Sift Prediction
      - `siftScore` (number (double)) — Sift Score
      - `transcriptId` (string, required) — Transcript id
      - `uniprotId` (string) — Uniprot ID
      - `variantClassification` (string) — Variant classification
    - `transcriptConsequenceSummary` (object, required)
      - `aminoAcidAlt` (string) — Alt Amino Acid
      - `aminoAcidRef` (string) — Reference Amino Acid
      - `aminoAcids` (string) — Amino acids change
      - `codonChange` (string) — Codon change
      - `consequenceTerms` (string) — Consequence terms (comma separated)
      - `entrezGeneId` (string) — Entrez gene id
      - `exon` (string)
      - `hgvsc` (string) — HGVSc
      - `hgvsp` (string) — HGVSp
      - `hgvspShort` (string) — HGVSp short
      - `hugoGeneSymbol` (string) — Hugo gene symbol
      - `polyphenPrediction` (string) — Polyphen Prediction
      - `polyphenScore` (number (double)) — Polyphen Score
      - `proteinPosition` (object)
        - `end` (integer (int32))
        - `start` (integer (int32))
      - `refSeq` (string) — RefSeq id
      - `siftPrediction` (string) — Sift Prediction
      - `siftScore` (number (double)) — Sift Score
      - `transcriptId` (string, required) — Transcript id
      - `uniprotId` (string) — Uniprot ID
      - `variantClassification` (string) — Variant classification
    - `transcriptConsequences` (array of object, required) — (Deprecated) Transcript consequence summaries (list of one when using annotation/, multiple when using annotation/summary/
      - `aminoAcidAlt` (string) — Alt Amino Acid
      - `aminoAcidRef` (string) — Reference Amino Acid
      - `aminoAcids` (string) — Amino acids change
      - `codonChange` (string) — Codon change
      - `consequenceTerms` (string) — Consequence terms (comma separated)
      - `entrezGeneId` (string) — Entrez gene id
      - `exon` (string)
      - `hgvsc` (string) — HGVSc
      - `hgvsp` (string) — HGVSp
      - `hgvspShort` (string) — HGVSp short
      - `hugoGeneSymbol` (string) — Hugo gene symbol
      - `polyphenPrediction` (string) — Polyphen Prediction
      - `polyphenScore` (number (double)) — Polyphen Score
      - `proteinPosition` (object)
        - `end` (integer (int32))
        - `start` (integer (int32))
      - `refSeq` (string) — RefSeq id
      - `siftPrediction` (string) — Sift Prediction
      - `siftScore` (number (double)) — Sift Score
      - `transcriptId` (string, required) — Transcript id
      - `uniprotId` (string) — Uniprot ID
      - `variantClassification` (string) — Variant classification
    - `variant` (string, required) — Variant key
    - `variantType` (string) — Variant type
  - `assembly_name` (string) — NCBI build number
  - `clinvar` (object)
    - `annotation` (object)
      - `alternateAllele` (string)
      - `chromosome` (string)
      - `clinicalSignificance` (string)
      - `clinvarId` (integer (int32))
      - `conflictingClinicalSignificance` (string)
      - `endPosition` (integer (int32))
      - `referenceAllele` (string)
      - `startPosition` (integer (int32))
  - `colocatedVariants` (array of object)
    - `dbSnpId` (string)
    - `gnomad_nfe_allele` (string, required) — GnomAD Non-Finnish European Allele
    - `gnomad_nfe_maf` (string, required) — GnomAD Non-Finnish European MAF
    - `gnomad_afr_allele` (string, required) — GnomAD African/African American Allele
    - `gnomad_afr_maf` (string, required) — GnomAD African/African American MAF
    - `gnomad_eas_allele` (string, required) — GnomAD East Asian Allele
    - `gnomad_eas_maf` (string, required) — GnomAD East Asian MAF
  - `end` (integer (int32)) — End position
  - `hgvsg` (string)
  - `hotspots` (object)
    - `annotation` (array of array of object)
      - `hugoSymbol` (string) — Hugo gene symbol
      - `inframeCount` (integer (int32)) — Inframe mutation count
      - `missenseCount` (integer (int32)) — Missense mutation count
      - `residue` (string) — Hotspot residue
      - `spliceCount` (integer (int32)) — Splice mutation count
      - `transcriptId` (string) — Ensembl Transcript Id
      - `truncatingCount` (integer (int32)) — Truncation mutation count
      - `tumorCount` (integer (int32)) — Tumor count
      - `type` (string) — Hotspot type
    - `license` (string)
  - `id` (string, required) — Variant id
  - `intergenic_consequences` (array of object, required) — intergenicConsequences
    - `impact` (string, required) — impact
    - `variantAllele` (string, required) — variant_allele
    - `consequenceTerms` (array of string, required) — consequence_terms
  - `most_severe_consequence` (string) — Most severe consequence
  - `mutation_assessor` (object)
    - `annotation` (object)
      - `codonStartPosition` (string) — Codon start position
      - `cosmicCount` (integer (int32)) — Number of mutations in COSMIC for this protein
      - `functionalImpact` (string) — Functional impact
      - `functionalImpactScore` (number (double)) — Functional impact score
      - `hgvs` (string)
      - `hugoSymbol` (string) — Hugo gene symbol
      - `input` (string, required) — User-input variants
      - `mappingIssue` (string) — Mapping issue info
      - `msaGaps` (number (double)) — Portion of gaps in variant position in multiple sequence alignment
      - `msaHeight` (integer (int32)) — Number of diverse sequences in multiple sequence alignment (identical or highly similar sequences filtered out)
      - `msaLink` (string) — Link to multiple sequence alignment
      - `pdbLink` (string) — Link to 3d structure browser
      - `referenceGenomeVariant` (string) — Reference genome variant
      - `referenceGenomeVariantType` (string) — Reference genome variant type
      - `refseqId` (string) — Refseq protein ID
      - `refseqPosition` (integer (int32)) — Variant position in Refseq protein, can be different from the one in Uniprot
      - `refseqResidue` (string) — Reference residue in Refseq protein, can be different from the one in Uniprot
      - `snpCount` (integer (int32)) — Number of SNPs in dbSNP for this protein
      - `uniprotId` (string) — Uniprot protein accession ID
      - `uniprotPosition` (integer (int32)) — Variant position in Uniprot protein, can be different from the one in Refseq
      - `uniprotResidue` (string) — Reference residue in Uniprot protein, can be different from the one in Refseq
      - `variant` (string) — Amino acid substitution
      - `variantConservationScore` (number (double)) — Variant conservation score
      - `variantSpecificityScore` (number (double)) — Variant specificity score
    - `license` (string)
  - `my_variant_info` (object)
    - `annotation` (object)
      - `clinVar` (object)
        - `alleleId` (integer (int32)) — allele_id
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `cytogenic` (string) — cytogenic
        - `gene` (object)
        - `hg19` (object)
        - `hg38` (object)
        - `hgvs` (object)
        - `license` (string) — license
        - `rcv` (array of object)
        - `variantId` (integer (int32)) — variant_id
      - `cosmic` (object)
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `cosmicId` (string) — cosmic_id
        - `hg19` (object)
        - `license` (string) — _license
        - `mutFreq` (number (double)) — mut_freq
        - `mutNt` (string) — mut_nt
        - `ref` (string) — ref
        - `tumorSite` (string) — tumor_site
      - `dbsnp` (object)
        - `_class` (string) — class
        - `alleleOrigin` (string) — allele_origin
        - `alleles` (array of object) — alleles
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `dbsnpBuild` (integer (int32)) — dbsnp_build
        - `flags` (array of string) — flags
        - `hg19` (object)
        - `license` (string) — _license
        - `ref` (string) — ref
        - `rsid` (string) — rsid
        - `validated` (boolean) — validated
        - `varSubtype` (string) — var_subtype
        - `vartype` (string) — vartype
      - `gnomadExome` (object)
        - `alleleCount` (object)
        - `alleleFrequency` (object)
        - `alleleNumber` (object)
        - `homozygotes` (object)
      - `gnomadGenome` (object)
        - `alleleCount` (object)
        - `alleleFrequency` (object)
        - `alleleNumber` (object)
        - `homozygotes` (object)
      - `hgvs` (string) — hgvs
      - `mutdb` (object)
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `cosmicId` (string) — cosmic_id
        - `hg19` (object)
        - `mutpredScore` (number (double)) — mutpred_score
        - `ref` (string) — ref
        - `rsid` (string) — rsid
        - `uniprotId` (string) — uniprot_id
      - `query` (string)
      - `snpeff` (object)
        - `license` (string) — license
      - `variant` (string) — variant
      - `vcf` (object)
        - `alt` (string) — alt
        - `position` (string) — position
        - `ref` (string) — ref
      - `version` (integer (int32)) — version
    - `license` (string)
  - `nucleotide_context` (object)
    - `annotation` (object)
      - `hgvs` (string)
      - `id` (string)
      - `molecule` (string)
      - `query` (string)
      - `seq` (string, required) — Nucleotide context sequence
    - `license` (string)
  - `oncokb` (object)
    - `annotation` (object)
      - `alleleExist` (boolean)
      - `dataVersion` (string)
      - `diagnosticImplications` (array of object)
        - `alterations` (array of string)
        - `description` (string)
        - `levelOfEvidence` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
        - `tumorType` (object) — OncoTree Detailed Cancer Type
      - `diagnosticSummary` (string)
      - `geneExist` (boolean)
      - `geneSummary` (string)
      - `highestDiagnosticImplicationLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `highestPrognosticImplicationLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `highestResistanceLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `highestSensitiveLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `hotspot` (boolean)
      - `lastUpdate` (string)
      - `mutationEffect` (object)
        - `citations` (object)
        - `description` (string)
        - `knownEffect` (string)
      - `oncogenic` (string)
      - `otherSignificantResistanceLevels` (array of string)
      - `otherSignificantSensitiveLevels` (array of string)
      - `prognosticImplications` (array of object)
        - `alterations` (array of string)
        - `description` (string)
        - `levelOfEvidence` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
        - `tumorType` (object) — OncoTree Detailed Cancer Type
      - `prognosticSummary` (string)
      - `query` (object)
        - `alteration` (string)
        - `alterationType` (string)
        - `consequence` (string)
        - `entrezGeneId` (integer (int32))
        - `hgvs` (string)
        - `hugoSymbol` (string)
        - `id` (string)
        - `proteinEnd` (integer (int32))
        - `proteinStart` (integer (int32))
        - `svType` (string) — Allowed values: `DELETION`, `TRANSLOCATION`, `DUPLICATION`, `INSERTION`, `INVERSION`, `FUSION`, `UNKNOWN`.
        - `tumorType` (string)
        - `type` (string)
      - `treatments` (array of object)
        - `abstracts` (array of object)
        - `alterations` (array of string)
        - `approvedIndications` (array of string)
        - `description` (string)
        - `drugs` (array of object)
        - `fdaApproved` (boolean)
        - `level` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
        - `levelAssociatedCancerType` (object) — OncoTree Detailed Cancer Type
        - `pmids` (array of string)
      - `tumorTypeSummary` (string)
      - `variantExist` (boolean)
      - `variantSummary` (string)
      - `vus` (boolean)
    - `license` (string)
  - `originalVariantQuery` (string, required) — Original variant query
  - `ptms` (object)
    - `annotation` (array of array of object)
      - `ensemblTranscriptIds` (array of string)
      - `position` (integer (int32))
      - `pubmedIds` (array of string)
      - `sequence` (string)
      - `type` (string)
      - `uniprotAccession` (string)
      - `uniprotEntry` (string)
    - `license` (string)
  - `seq_region_name` (string) — Chromosome
  - `signalAnnotation` (object)
    - `annotation` (array of object)
      - `biallelicCountsByTumorType` (array of object) — Biallelic Counts by Tumor Type
        - `tumorType` (string) — Tumor Type
        - `tumorTypeCount` (integer (int32)) — Sample count for Tumor Type
        - `variantCount` (integer (int32)) — Variant count for Tumor Type
      - `chromosome` (string) — Chromosome
      - `countsByTumorType` (array of object) — Counts by Tumor Type
        - `tumorType` (string) — Tumor Type
        - `tumorTypeCount` (integer (int32)) — Sample count for Tumor Type
        - `variantCount` (integer (int32)) — Variant count for Tumor Type
      - `endPosition` (integer (int64)) — End Position
      - `generalPopulationStats` (object)
        - `counts` (object)
        - `frequencies` (object)
      - `hugoGeneSymbol` (string) — Hugo Gene Symbol
      - `mskExperReview` (boolean) — Msk Expert Review
      - `mutationStatus` (string) — Mutation Status
      - `overallNumberOfGermlineHomozygous` (integer (int32))
      - `pathogenic` (string) — Pathogenic
      - `penetrance` (string) — Penetrance
      - `qcPassCountsByTumorType` (array of object) — QC Pass Counts by Tumor Type
        - `tumorType` (string) — Tumor Type
        - `tumorTypeCount` (integer (int32)) — Sample count for Tumor Type
        - `variantCount` (integer (int32)) — Variant count for Tumor Type
      - `referenceAllele` (string) — Reference Allele
      - `startPosition` (integer (int64)) — Start Position
      - `statsByTumorType` (array of object) — Stats By Tumor Type
        - `ageAtDx` (integer (int32)) — Median Age at Dx
        - `fBiallelic` (number (double)) — Frequency Of Biallelic
        - `fCancerTypeCount` (number (double)) — Frequency Of Cancer Type Count
        - `hrdScore` (object)
        - `msiScore` (number (double)) — Msi Score
        - `nCancerTypeCount` (integer (int32)) — Number Of Cancer Type Count
        - `numberOfGermlineHomozygous` (integer (int32)) — Number Of Germline Homozygous Per Tumor Type
        - `numberWithSig` (integer (int32)) — Number of Variants with Signature
        - `tmb` (number (double)) — Median TMB
        - `tumorType` (string) — Tumor Type
      - `variantAllele` (string) — Variant Allele
    - `license` (string)
  - `start` (integer (int32)) — Start position
  - `strand` (integer (int32)) — Strand (negative or positive)
  - `successfully_annotated` (boolean) — Status flag indicating whether variant was succesfully annotated
  - `transcript_consequences` (array of object) — List of transcripts
    - `amino_acids` (string) — Amino acids
    - `canonical` (string) — Canonical transcript indicator
    - `codons` (string) — Codons
    - `consequence_terms` (array of string) — List of consequence terms
    - `exon` (string)
    - `gene_id` (string) — Ensembl gene id
    - `gene_symbol` (string) — Hugo gene symbol
    - `hgnc_id` (string) — HGNC id
    - `hgvsc` (string) — HGVSc
    - `hgvsg` (string) — HGVSg
    - `hgvsp` (string) — HGVSp
    - `polyphen_prediction` (string) — Polyphen Prediction
    - `polyphen_score` (number (double)) — Polyphen Score
    - `protein_end` (integer (int32)) — Protein end position
    - `protein_id` (string) — Ensembl protein id
    - `protein_start` (integer (int32)) — Protein start position
    - `refseq_transcript_ids` (array of string) — List of RefSeq transcript ids
    - `sift_prediction` (string) — Sift Prediction
    - `sift_score` (number (double)) — Sift Score
    - `transcript_id` (string, required) — Ensembl transcript id
    - `uniprotId` (string)
    - `variant_allele` (string) — Variant allele
  - `variant` (string, required) — Variant key

### GET /annotation/{variant}

**Retrieves VEP annotation for the provided variant**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `variant` | path | string | Yes | Variant. For example 17:g.41242962_41242963insGA |
| `isoformOverrideSource` | query | string | No | Isoform override source. For example uniprot |
| `token` | query | string | No | Map of tokens. For example {"source1":"put-your-token1-here","source2":"put-your-token2-here"} |
| `fields` | query | array of string | No | Comma separated list of fields to include (case-sensitive!). For example: hotspots |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `allele_string` (string) — Allele string (e.g: A/T)
  - `annotationJSON` (string) — Annotation data as JSON string
  - `annotation_summary` (object)
    - `assemblyName` (string) — Assembly name
    - `canonicalTranscriptId` (string) — Canonical transcript id
    - `genomicLocation` (object)
      - `chromosome` (string, required) — Chromosome
      - `start` (integer (int32), required) — Start Position
      - `end` (integer (int32), required) — End Position
      - `referenceAllele` (string, required) — Reference Allele
      - `variantAllele` (string, required) — Variant Allele
    - `strandSign` (string) — Strand (- or +)
    - `transcriptConsequenceSummaries` (array of object, required) — All transcript consequence summaries
      - `aminoAcidAlt` (string) — Alt Amino Acid
      - `aminoAcidRef` (string) — Reference Amino Acid
      - `aminoAcids` (string) — Amino acids change
      - `codonChange` (string) — Codon change
      - `consequenceTerms` (string) — Consequence terms (comma separated)
      - `entrezGeneId` (string) — Entrez gene id
      - `exon` (string)
      - `hgvsc` (string) — HGVSc
      - `hgvsp` (string) — HGVSp
      - `hgvspShort` (string) — HGVSp short
      - `hugoGeneSymbol` (string) — Hugo gene symbol
      - `polyphenPrediction` (string) — Polyphen Prediction
      - `polyphenScore` (number (double)) — Polyphen Score
      - `proteinPosition` (object)
        - `end` (integer (int32))
        - `start` (integer (int32))
      - `refSeq` (string) — RefSeq id
      - `siftPrediction` (string) — Sift Prediction
      - `siftScore` (number (double)) — Sift Score
      - `transcriptId` (string, required) — Transcript id
      - `uniprotId` (string) — Uniprot ID
      - `variantClassification` (string) — Variant classification
    - `transcriptConsequenceSummary` (object, required)
      - `aminoAcidAlt` (string) — Alt Amino Acid
      - `aminoAcidRef` (string) — Reference Amino Acid
      - `aminoAcids` (string) — Amino acids change
      - `codonChange` (string) — Codon change
      - `consequenceTerms` (string) — Consequence terms (comma separated)
      - `entrezGeneId` (string) — Entrez gene id
      - `exon` (string)
      - `hgvsc` (string) — HGVSc
      - `hgvsp` (string) — HGVSp
      - `hgvspShort` (string) — HGVSp short
      - `hugoGeneSymbol` (string) — Hugo gene symbol
      - `polyphenPrediction` (string) — Polyphen Prediction
      - `polyphenScore` (number (double)) — Polyphen Score
      - `proteinPosition` (object)
        - `end` (integer (int32))
        - `start` (integer (int32))
      - `refSeq` (string) — RefSeq id
      - `siftPrediction` (string) — Sift Prediction
      - `siftScore` (number (double)) — Sift Score
      - `transcriptId` (string, required) — Transcript id
      - `uniprotId` (string) — Uniprot ID
      - `variantClassification` (string) — Variant classification
    - `transcriptConsequences` (array of object, required) — (Deprecated) Transcript consequence summaries (list of one when using annotation/, multiple when using annotation/summary/
      - `aminoAcidAlt` (string) — Alt Amino Acid
      - `aminoAcidRef` (string) — Reference Amino Acid
      - `aminoAcids` (string) — Amino acids change
      - `codonChange` (string) — Codon change
      - `consequenceTerms` (string) — Consequence terms (comma separated)
      - `entrezGeneId` (string) — Entrez gene id
      - `exon` (string)
      - `hgvsc` (string) — HGVSc
      - `hgvsp` (string) — HGVSp
      - `hgvspShort` (string) — HGVSp short
      - `hugoGeneSymbol` (string) — Hugo gene symbol
      - `polyphenPrediction` (string) — Polyphen Prediction
      - `polyphenScore` (number (double)) — Polyphen Score
      - `proteinPosition` (object)
        - `end` (integer (int32))
        - `start` (integer (int32))
      - `refSeq` (string) — RefSeq id
      - `siftPrediction` (string) — Sift Prediction
      - `siftScore` (number (double)) — Sift Score
      - `transcriptId` (string, required) — Transcript id
      - `uniprotId` (string) — Uniprot ID
      - `variantClassification` (string) — Variant classification
    - `variant` (string, required) — Variant key
    - `variantType` (string) — Variant type
  - `assembly_name` (string) — NCBI build number
  - `clinvar` (object)
    - `annotation` (object)
      - `alternateAllele` (string)
      - `chromosome` (string)
      - `clinicalSignificance` (string)
      - `clinvarId` (integer (int32))
      - `conflictingClinicalSignificance` (string)
      - `endPosition` (integer (int32))
      - `referenceAllele` (string)
      - `startPosition` (integer (int32))
  - `colocatedVariants` (array of object)
    - `dbSnpId` (string)
    - `gnomad_nfe_allele` (string, required) — GnomAD Non-Finnish European Allele
    - `gnomad_nfe_maf` (string, required) — GnomAD Non-Finnish European MAF
    - `gnomad_afr_allele` (string, required) — GnomAD African/African American Allele
    - `gnomad_afr_maf` (string, required) — GnomAD African/African American MAF
    - `gnomad_eas_allele` (string, required) — GnomAD East Asian Allele
    - `gnomad_eas_maf` (string, required) — GnomAD East Asian MAF
  - `end` (integer (int32)) — End position
  - `hgvsg` (string)
  - `hotspots` (object)
    - `annotation` (array of array of object)
      - `hugoSymbol` (string) — Hugo gene symbol
      - `inframeCount` (integer (int32)) — Inframe mutation count
      - `missenseCount` (integer (int32)) — Missense mutation count
      - `residue` (string) — Hotspot residue
      - `spliceCount` (integer (int32)) — Splice mutation count
      - `transcriptId` (string) — Ensembl Transcript Id
      - `truncatingCount` (integer (int32)) — Truncation mutation count
      - `tumorCount` (integer (int32)) — Tumor count
      - `type` (string) — Hotspot type
    - `license` (string)
  - `id` (string, required) — Variant id
  - `intergenic_consequences` (array of object, required) — intergenicConsequences
    - `impact` (string, required) — impact
    - `variantAllele` (string, required) — variant_allele
    - `consequenceTerms` (array of string, required) — consequence_terms
  - `most_severe_consequence` (string) — Most severe consequence
  - `mutation_assessor` (object)
    - `annotation` (object)
      - `codonStartPosition` (string) — Codon start position
      - `cosmicCount` (integer (int32)) — Number of mutations in COSMIC for this protein
      - `functionalImpact` (string) — Functional impact
      - `functionalImpactScore` (number (double)) — Functional impact score
      - `hgvs` (string)
      - `hugoSymbol` (string) — Hugo gene symbol
      - `input` (string, required) — User-input variants
      - `mappingIssue` (string) — Mapping issue info
      - `msaGaps` (number (double)) — Portion of gaps in variant position in multiple sequence alignment
      - `msaHeight` (integer (int32)) — Number of diverse sequences in multiple sequence alignment (identical or highly similar sequences filtered out)
      - `msaLink` (string) — Link to multiple sequence alignment
      - `pdbLink` (string) — Link to 3d structure browser
      - `referenceGenomeVariant` (string) — Reference genome variant
      - `referenceGenomeVariantType` (string) — Reference genome variant type
      - `refseqId` (string) — Refseq protein ID
      - `refseqPosition` (integer (int32)) — Variant position in Refseq protein, can be different from the one in Uniprot
      - `refseqResidue` (string) — Reference residue in Refseq protein, can be different from the one in Uniprot
      - `snpCount` (integer (int32)) — Number of SNPs in dbSNP for this protein
      - `uniprotId` (string) — Uniprot protein accession ID
      - `uniprotPosition` (integer (int32)) — Variant position in Uniprot protein, can be different from the one in Refseq
      - `uniprotResidue` (string) — Reference residue in Uniprot protein, can be different from the one in Refseq
      - `variant` (string) — Amino acid substitution
      - `variantConservationScore` (number (double)) — Variant conservation score
      - `variantSpecificityScore` (number (double)) — Variant specificity score
    - `license` (string)
  - `my_variant_info` (object)
    - `annotation` (object)
      - `clinVar` (object)
        - `alleleId` (integer (int32)) — allele_id
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `cytogenic` (string) — cytogenic
        - `gene` (object)
        - `hg19` (object)
        - `hg38` (object)
        - `hgvs` (object)
        - `license` (string) — license
        - `rcv` (array of object)
        - `variantId` (integer (int32)) — variant_id
      - `cosmic` (object)
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `cosmicId` (string) — cosmic_id
        - `hg19` (object)
        - `license` (string) — _license
        - `mutFreq` (number (double)) — mut_freq
        - `mutNt` (string) — mut_nt
        - `ref` (string) — ref
        - `tumorSite` (string) — tumor_site
      - `dbsnp` (object)
        - `_class` (string) — class
        - `alleleOrigin` (string) — allele_origin
        - `alleles` (array of object) — alleles
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `dbsnpBuild` (integer (int32)) — dbsnp_build
        - `flags` (array of string) — flags
        - `hg19` (object)
        - `license` (string) — _license
        - `ref` (string) — ref
        - `rsid` (string) — rsid
        - `validated` (boolean) — validated
        - `varSubtype` (string) — var_subtype
        - `vartype` (string) — vartype
      - `gnomadExome` (object)
        - `alleleCount` (object)
        - `alleleFrequency` (object)
        - `alleleNumber` (object)
        - `homozygotes` (object)
      - `gnomadGenome` (object)
        - `alleleCount` (object)
        - `alleleFrequency` (object)
        - `alleleNumber` (object)
        - `homozygotes` (object)
      - `hgvs` (string) — hgvs
      - `mutdb` (object)
        - `alt` (string) — alt
        - `chrom` (string) — chrom
        - `cosmicId` (string) — cosmic_id
        - `hg19` (object)
        - `mutpredScore` (number (double)) — mutpred_score
        - `ref` (string) — ref
        - `rsid` (string) — rsid
        - `uniprotId` (string) — uniprot_id
      - `query` (string)
      - `snpeff` (object)
        - `license` (string) — license
      - `variant` (string) — variant
      - `vcf` (object)
        - `alt` (string) — alt
        - `position` (string) — position
        - `ref` (string) — ref
      - `version` (integer (int32)) — version
    - `license` (string)
  - `nucleotide_context` (object)
    - `annotation` (object)
      - `hgvs` (string)
      - `id` (string)
      - `molecule` (string)
      - `query` (string)
      - `seq` (string, required) — Nucleotide context sequence
    - `license` (string)
  - `oncokb` (object)
    - `annotation` (object)
      - `alleleExist` (boolean)
      - `dataVersion` (string)
      - `diagnosticImplications` (array of object)
        - `alterations` (array of string)
        - `description` (string)
        - `levelOfEvidence` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
        - `tumorType` (object) — OncoTree Detailed Cancer Type
      - `diagnosticSummary` (string)
      - `geneExist` (boolean)
      - `geneSummary` (string)
      - `highestDiagnosticImplicationLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `highestPrognosticImplicationLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `highestResistanceLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `highestSensitiveLevel` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
      - `hotspot` (boolean)
      - `lastUpdate` (string)
      - `mutationEffect` (object)
        - `citations` (object)
        - `description` (string)
        - `knownEffect` (string)
      - `oncogenic` (string)
      - `otherSignificantResistanceLevels` (array of string)
      - `otherSignificantSensitiveLevels` (array of string)
      - `prognosticImplications` (array of object)
        - `alterations` (array of string)
        - `description` (string)
        - `levelOfEvidence` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
        - `tumorType` (object) — OncoTree Detailed Cancer Type
      - `prognosticSummary` (string)
      - `query` (object)
        - `alteration` (string)
        - `alterationType` (string)
        - `consequence` (string)
        - `entrezGeneId` (integer (int32))
        - `hgvs` (string)
        - `hugoSymbol` (string)
        - `id` (string)
        - `proteinEnd` (integer (int32))
        - `proteinStart` (integer (int32))
        - `svType` (string) — Allowed values: `DELETION`, `TRANSLOCATION`, `DUPLICATION`, `INSERTION`, `INVERSION`, `FUSION`, `UNKNOWN`.
        - `tumorType` (string)
        - `type` (string)
      - `treatments` (array of object)
        - `abstracts` (array of object)
        - `alterations` (array of string)
        - `approvedIndications` (array of string)
        - `description` (string)
        - `drugs` (array of object)
        - `fdaApproved` (boolean)
        - `level` (string) — Allowed values: `LEVEL_0`, `LEVEL_1`, `LEVEL_2`, `LEVEL_2A`, `LEVEL_2B`, `LEVEL_3A`, `LEVEL_3B`, `LEVEL_4`, `LEVEL_R1`, `LEVEL_R2`, `LEVEL_R3`, `LEVEL_Px1`, `LEVEL_Px2`, `LEVEL_Px3`, `LEVEL_Dx1`, `LEVEL_Dx2`, `LEVEL_Dx3`, `false`.
        - `levelAssociatedCancerType` (object) — OncoTree Detailed Cancer Type
        - `pmids` (array of string)
      - `tumorTypeSummary` (string)
      - `variantExist` (boolean)
      - `variantSummary` (string)
      - `vus` (boolean)
    - `license` (string)
  - `originalVariantQuery` (string, required) — Original variant query
  - `ptms` (object)
    - `annotation` (array of array of object)
      - `ensemblTranscriptIds` (array of string)
      - `position` (integer (int32))
      - `pubmedIds` (array of string)
      - `sequence` (string)
      - `type` (string)
      - `uniprotAccession` (string)
      - `uniprotEntry` (string)
    - `license` (string)
  - `seq_region_name` (string) — Chromosome
  - `signalAnnotation` (object)
    - `annotation` (array of object)
      - `biallelicCountsByTumorType` (array of object) — Biallelic Counts by Tumor Type
        - `tumorType` (string) — Tumor Type
        - `tumorTypeCount` (integer (int32)) — Sample count for Tumor Type
        - `variantCount` (integer (int32)) — Variant count for Tumor Type
      - `chromosome` (string) — Chromosome
      - `countsByTumorType` (array of object) — Counts by Tumor Type
        - `tumorType` (string) — Tumor Type
        - `tumorTypeCount` (integer (int32)) — Sample count for Tumor Type
        - `variantCount` (integer (int32)) — Variant count for Tumor Type
      - `endPosition` (integer (int64)) — End Position
      - `generalPopulationStats` (object)
        - `counts` (object)
        - `frequencies` (object)
      - `hugoGeneSymbol` (string) — Hugo Gene Symbol
      - `mskExperReview` (boolean) — Msk Expert Review
      - `mutationStatus` (string) — Mutation Status
      - `overallNumberOfGermlineHomozygous` (integer (int32))
      - `pathogenic` (string) — Pathogenic
      - `penetrance` (string) — Penetrance
      - `qcPassCountsByTumorType` (array of object) — QC Pass Counts by Tumor Type
        - `tumorType` (string) — Tumor Type
        - `tumorTypeCount` (integer (int32)) — Sample count for Tumor Type
        - `variantCount` (integer (int32)) — Variant count for Tumor Type
      - `referenceAllele` (string) — Reference Allele
      - `startPosition` (integer (int64)) — Start Position
      - `statsByTumorType` (array of object) — Stats By Tumor Type
        - `ageAtDx` (integer (int32)) — Median Age at Dx
        - `fBiallelic` (number (double)) — Frequency Of Biallelic
        - `fCancerTypeCount` (number (double)) — Frequency Of Cancer Type Count
        - `hrdScore` (object)
        - `msiScore` (number (double)) — Msi Score
        - `nCancerTypeCount` (integer (int32)) — Number Of Cancer Type Count
        - `numberOfGermlineHomozygous` (integer (int32)) — Number Of Germline Homozygous Per Tumor Type
        - `numberWithSig` (integer (int32)) — Number of Variants with Signature
        - `tmb` (number (double)) — Median TMB
        - `tumorType` (string) — Tumor Type
      - `variantAllele` (string) — Variant Allele
    - `license` (string)
  - `start` (integer (int32)) — Start position
  - `strand` (integer (int32)) — Strand (negative or positive)
  - `successfully_annotated` (boolean) — Status flag indicating whether variant was succesfully annotated
  - `transcript_consequences` (array of object) — List of transcripts
    - `amino_acids` (string) — Amino acids
    - `canonical` (string) — Canonical transcript indicator
    - `codons` (string) — Codons
    - `consequence_terms` (array of string) — List of consequence terms
    - `exon` (string)
    - `gene_id` (string) — Ensembl gene id
    - `gene_symbol` (string) — Hugo gene symbol
    - `hgnc_id` (string) — HGNC id
    - `hgvsc` (string) — HGVSc
    - `hgvsg` (string) — HGVSg
    - `hgvsp` (string) — HGVSp
    - `polyphen_prediction` (string) — Polyphen Prediction
    - `polyphen_score` (number (double)) — Polyphen Score
    - `protein_end` (integer (int32)) — Protein end position
    - `protein_id` (string) — Ensembl protein id
    - `protein_start` (integer (int32)) — Protein start position
    - `refseq_transcript_ids` (array of string) — List of RefSeq transcript ids
    - `sift_prediction` (string) — Sift Prediction
    - `sift_score` (number (double)) — Sift Score
    - `transcript_id` (string, required) — Ensembl transcript id
    - `uniprotId` (string)
    - `variant_allele` (string) — Variant allele
  - `variant` (string, required) — Variant key

## ensembl-controller

Ensembl Controller

### POST /ensembl/canonical-gene/entrez

**Retrieves canonical Ensembl Gene ID by Entrez Gene Ids**

**Request body** (`application/json`, required)

List of Entrez Gene Ids. For example ["23140","26009","100131879"]

- Body type: array of string

**Responses**

- **200** — OK
  Body (`application/json`, array of object):
  - `geneId` (string, required) — Ensembl gene id
  - `hugoSymbol` (string, required) — Approved Hugo symbol
  - `synonyms` (array of string) — Hugo symbol synonyms
  - `previousSymbols` (array of string) — Previous Hugo symbols
  - `entrezGeneId` (string) — Entrez Gene Id

### GET /ensembl/canonical-gene/entrez/{entrezGeneId}

**Retrieves Ensembl canonical gene id by Entrez Gene Id**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `entrezGeneId` | path | string | Yes | An Entrez Gene Id. For example 23140 |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `geneId` (string, required) — Ensembl gene id
  - `hugoSymbol` (string, required) — Approved Hugo symbol
  - `synonyms` (array of string) — Hugo symbol synonyms
  - `previousSymbols` (array of string) — Previous Hugo symbols
  - `entrezGeneId` (string) — Entrez Gene Id

### POST /ensembl/canonical-gene/hgnc

**Retrieves canonical Ensembl Gene ID by Hugo Symbols**

**Request body** (`application/json`, required)

List of Hugo Symbols. For example ["TP53","PIK3CA","BRCA1"]

- Body type: array of string

**Responses**

- **200** — OK
  Body (`application/json`, array of object):
  - `geneId` (string, required) — Ensembl gene id
  - `hugoSymbol` (string, required) — Approved Hugo symbol
  - `synonyms` (array of string) — Hugo symbol synonyms
  - `previousSymbols` (array of string) — Previous Hugo symbols
  - `entrezGeneId` (string) — Entrez Gene Id

### GET /ensembl/canonical-gene/hgnc/{hugoSymbol}

**Retrieves Ensembl canonical gene id by Hugo Symbol**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `hugoSymbol` | path | string | Yes | A Hugo Symbol. For example TP53 |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `geneId` (string, required) — Ensembl gene id
  - `hugoSymbol` (string, required) — Approved Hugo symbol
  - `synonyms` (array of string) — Hugo symbol synonyms
  - `previousSymbols` (array of string) — Previous Hugo symbols
  - `entrezGeneId` (string) — Entrez Gene Id

### POST /ensembl/canonical-transcript/hgnc

**Retrieves Ensembl canonical transcripts by Hugo Symbols**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `isoformOverrideSource` | query | string | No | Isoform override source. For example uniprot. Default: `uniprot`. |

**Request body** (`application/json`, required)

List of Hugo Symbols. For example ["TP53","PIK3CA","BRCA1"]

- Body type: array of string

**Responses**

- **200** — OK
  Body (`application/json`, array of object):
  - `uniprotId` (string)
  - `transcriptId` (string, required) — Ensembl transcript id
  - `geneId` (string, required) — Ensembl gene id
  - `proteinId` (string, required) — Ensembl protein id
  - `proteinLength` (integer (int32)) — Length of protein
  - `pfamDomains` (array of object) — Pfam domains
    - `pfamDomainId` (string, required) — Pfam domain id
    - `pfamDomainStart` (integer (int32), required) — Pfam domain start amino acid
    - `pfamDomainEnd` (integer (int32), required) — Pfam domain end amino acid
  - `hugoSymbols` (array of string) — Hugo symbols
  - `refseqMrnaId` (string) — RefSeq mRNA ID
  - `ccdsId` (string) — Consensus CDS (CCDS) ID
  - `exons` (array of object) — Exon information
    - `exonId` (string, required) — Exon id
    - `exonStart` (integer (int32), required) — Start position of exon
    - `exonEnd` (integer (int32), required) — End position of exon
    - `rank` (integer (int32), required) — Number of exon in transcript
    - `strand` (integer (int32), required) — Strand exon is on, -1 for - and 1 for +
    - `version` (integer (int32), required) — Exon version
  - `utrs` (array of object) — UTR information
    - `type` (string, required) — UTR Type
    - `start` (integer (int32), required) — Start position of UTR
    - `end` (integer (int32), required) — End position of UTR
    - `strand` (integer (int32), required) — Strand UTR is on, -1 for - and 1 for +

### GET /ensembl/canonical-transcript/hgnc/{hugoSymbol}

**Retrieves Ensembl canonical transcript by Hugo Symbol**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `hugoSymbol` | path | string | Yes | A Hugo Symbol. For example TP53 |
| `isoformOverrideSource` | query | string | No | Isoform override source. For example uniprot. Default: `uniprot`. |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `uniprotId` (string)
  - `transcriptId` (string, required) — Ensembl transcript id
  - `geneId` (string, required) — Ensembl gene id
  - `proteinId` (string, required) — Ensembl protein id
  - `proteinLength` (integer (int32)) — Length of protein
  - `pfamDomains` (array of object) — Pfam domains
    - `pfamDomainId` (string, required) — Pfam domain id
    - `pfamDomainStart` (integer (int32), required) — Pfam domain start amino acid
    - `pfamDomainEnd` (integer (int32), required) — Pfam domain end amino acid
  - `hugoSymbols` (array of string) — Hugo symbols
  - `refseqMrnaId` (string) — RefSeq mRNA ID
  - `ccdsId` (string) — Consensus CDS (CCDS) ID
  - `exons` (array of object) — Exon information
    - `exonId` (string, required) — Exon id
    - `exonStart` (integer (int32), required) — Start position of exon
    - `exonEnd` (integer (int32), required) — End position of exon
    - `rank` (integer (int32), required) — Number of exon in transcript
    - `strand` (integer (int32), required) — Strand exon is on, -1 for - and 1 for +
    - `version` (integer (int32), required) — Exon version
  - `utrs` (array of object) — UTR information
    - `type` (string, required) — UTR Type
    - `start` (integer (int32), required) — Start position of UTR
    - `end` (integer (int32), required) — End position of UTR
    - `strand` (integer (int32), required) — Strand UTR is on, -1 for - and 1 for +

### GET /ensembl/transcript

**Retrieves Ensembl Transcripts by protein ID, and gene ID. Retrieves all transcripts in case no query parameter provided**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `geneId` | query | string | No | An Ensembl gene ID. For example ENSG00000136999 |
| `proteinId` | query | string | No | An Ensembl protein ID. For example ENSP00000439985 |
| `hugoSymbol` | query | string | No | A Hugo Symbol For example ARF5 |

**Responses**

- **200** — OK
  Body (`application/json`, array of object):
  - `uniprotId` (string)
  - `transcriptId` (string, required) — Ensembl transcript id
  - `geneId` (string, required) — Ensembl gene id
  - `proteinId` (string, required) — Ensembl protein id
  - `proteinLength` (integer (int32)) — Length of protein
  - `pfamDomains` (array of object) — Pfam domains
    - `pfamDomainId` (string, required) — Pfam domain id
    - `pfamDomainStart` (integer (int32), required) — Pfam domain start amino acid
    - `pfamDomainEnd` (integer (int32), required) — Pfam domain end amino acid
  - `hugoSymbols` (array of string) — Hugo symbols
  - `refseqMrnaId` (string) — RefSeq mRNA ID
  - `ccdsId` (string) — Consensus CDS (CCDS) ID
  - `exons` (array of object) — Exon information
    - `exonId` (string, required) — Exon id
    - `exonStart` (integer (int32), required) — Start position of exon
    - `exonEnd` (integer (int32), required) — End position of exon
    - `rank` (integer (int32), required) — Number of exon in transcript
    - `strand` (integer (int32), required) — Strand exon is on, -1 for - and 1 for +
    - `version` (integer (int32), required) — Exon version
  - `utrs` (array of object) — UTR information
    - `type` (string, required) — UTR Type
    - `start` (integer (int32), required) — Start position of UTR
    - `end` (integer (int32), required) — End position of UTR
    - `strand` (integer (int32), required) — Strand UTR is on, -1 for - and 1 for +

### POST /ensembl/transcript

**Retrieves Ensembl Transcripts by Ensembl transcript IDs, hugo Symbols, protein IDs, or gene IDs**

**Request body** (`application/json`, required)

List of Ensembl transcript IDs. For example ["ENST00000361390", "ENST00000361453", "ENST00000361624"]<br>OR<br>List of Hugo Symbols. For example ["TP53", "PIK3CA", "BRCA1"]<br>OR<br>List of Ensembl protein IDs. For example ["ENSP00000439985", "ENSP00000478460", "ENSP00000346196"]<br>OR<br>List of Ensembl gene IDs. For example ["ENSG00000136999", "ENSG00000272398", "ENSG00000198695"]

- `geneIds` (array of string) — List of Ensembl gene IDs. For example ["ENSG00000136999", "ENSG00000272398", "ENSG00000198695"]
- `hugoSymbols` (array of string) — List of Hugo Symbols. For example ["TP53", "PIK3CA", "BRCA1"]
- `proteinIds` (array of string) — List of Ensembl protein IDs. For example ["ENSP00000439985", "ENSP00000478460", "ENSP00000346196"]
- `transcriptIds` (array of string) — List of Ensembl transcript IDs. For example ["ENST00000361390", "ENST00000361453", "ENST00000361624"]

**Responses**

- **200** — OK
  Body (`application/json`, array of object):
  - `uniprotId` (string)
  - `transcriptId` (string, required) — Ensembl transcript id
  - `geneId` (string, required) — Ensembl gene id
  - `proteinId` (string, required) — Ensembl protein id
  - `proteinLength` (integer (int32)) — Length of protein
  - `pfamDomains` (array of object) — Pfam domains
    - `pfamDomainId` (string, required) — Pfam domain id
    - `pfamDomainStart` (integer (int32), required) — Pfam domain start amino acid
    - `pfamDomainEnd` (integer (int32), required) — Pfam domain end amino acid
  - `hugoSymbols` (array of string) — Hugo symbols
  - `refseqMrnaId` (string) — RefSeq mRNA ID
  - `ccdsId` (string) — Consensus CDS (CCDS) ID
  - `exons` (array of object) — Exon information
    - `exonId` (string, required) — Exon id
    - `exonStart` (integer (int32), required) — Start position of exon
    - `exonEnd` (integer (int32), required) — End position of exon
    - `rank` (integer (int32), required) — Number of exon in transcript
    - `strand` (integer (int32), required) — Strand exon is on, -1 for - and 1 for +
    - `version` (integer (int32), required) — Exon version
  - `utrs` (array of object) — UTR information
    - `type` (string, required) — UTR Type
    - `start` (integer (int32), required) — Start position of UTR
    - `end` (integer (int32), required) — End position of UTR
    - `strand` (integer (int32), required) — Strand UTR is on, -1 for - and 1 for +

### GET /ensembl/transcript/{transcriptId}

**Retrieves the transcript by an Ensembl transcript ID**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `transcriptId` | path | string | Yes | An Ensembl transcript ID. For example ENST00000361390 |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `uniprotId` (string)
  - `transcriptId` (string, required) — Ensembl transcript id
  - `geneId` (string, required) — Ensembl gene id
  - `proteinId` (string, required) — Ensembl protein id
  - `proteinLength` (integer (int32)) — Length of protein
  - `pfamDomains` (array of object) — Pfam domains
    - `pfamDomainId` (string, required) — Pfam domain id
    - `pfamDomainStart` (integer (int32), required) — Pfam domain start amino acid
    - `pfamDomainEnd` (integer (int32), required) — Pfam domain end amino acid
  - `hugoSymbols` (array of string) — Hugo symbols
  - `refseqMrnaId` (string) — RefSeq mRNA ID
  - `ccdsId` (string) — Consensus CDS (CCDS) ID
  - `exons` (array of object) — Exon information
    - `exonId` (string, required) — Exon id
    - `exonStart` (integer (int32), required) — Start position of exon
    - `exonEnd` (integer (int32), required) — End position of exon
    - `rank` (integer (int32), required) — Number of exon in transcript
    - `strand` (integer (int32), required) — Strand exon is on, -1 for - and 1 for +
    - `version` (integer (int32), required) — Exon version
  - `utrs` (array of object) — UTR information
    - `type` (string, required) — UTR Type
    - `start` (integer (int32), required) — Start position of UTR
    - `end` (integer (int32), required) — End position of UTR
    - `strand` (integer (int32), required) — Strand UTR is on, -1 for - and 1 for +

### GET /ensembl/xrefs

**Perform lookups of Ensembl identifiers and retrieve their external references in other databases**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `accession` | query | string | Yes | Ensembl gene accession. For example ENSG00000169083 |

**Responses**

- **200** — OK
  Body (`application/json`, array of object):
  - `db_display_name` (string, required) — Database display name
  - `dbname` (string, required) — Database name
  - `description` (string, required) — Description
  - `display_id` (string, required) — Display id
  - `ensemblGeneId` (string)
  - `info_text` (string) — Database info text
  - `info_types` (string) — Database info type
  - `primary_id` (string, required) — Primary id
  - `synonyms` (array of string) — Synonyms
  - `version` (string, required) — Version

## pdb-controller

PDB Controller

### POST /pdb/header

**Retrieves PDB header info by a PDB id**

**Request body** (`application/json`, required)

List of pdb ids, for example ["1a37","1a4o"]

- Body type: array of string

**Responses**

- **200** — OK
  Body (`application/json`, array of object):
  - `compound` (object)
  - `pdbId` (string, required) — PDB id
  - `source` (object)
  - `title` (string, required) — PDB description

### GET /pdb/header/{pdbId}

**Retrieves PDB header info by a PDB id**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `pdbId` | path | string | Yes | PDB id, for example 1a37 |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `compound` (object)
  - `pdbId` (string, required) — PDB id
  - `source` (object)
  - `title` (string, required) — PDB description

## pfam-controller

PFAM Controller

### POST /pfam/domain

**Retrieves PFAM domains by PFAM domain accession IDs**

**Request body** (`application/json`, required)

List of PFAM domain accession IDs. For example ["PF02827","PF00093","PF15276"]

- Body type: array of string

**Responses**

- **200** — OK
  Body (`application/json`, array of object):
  - `description` (string) — PFAM domain description
  - `name` (string, required) — PFAM domain name
  - `pfamAccession` (string, required) — PFAM domain accession

### GET /pfam/domain/{pfamAccession}

**Retrieves a PFAM domain by a PFAM domain ID**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `pfamAccession` | path | string | Yes | A PFAM domain accession ID. For example PF02827 |

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `description` (string) — PFAM domain description
  - `name` (string, required) — PFAM domain name
  - `pfamAccession` (string, required) — PFAM domain accession

## ptm-controller

PTM Controller

### GET /ptm/experimental

**Retrieves PTM entries by Ensembl Transcript ID**

**Parameters**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| `ensemblTranscriptId` | query | string | No | Ensembl Transcript ID. For example ENST00000646891 |

**Responses**

- **200** — OK
  Body (`application/json`, array of object):
  - `ensemblTranscriptIds` (array of string)
  - `position` (integer (int32))
  - `pubmedIds` (array of string)
  - `sequence` (string)
  - `type` (string)
  - `uniprotAccession` (string)
  - `uniprotEntry` (string)

### POST /ptm/experimental

**Retrieves PTM entries by Ensembl Transcript IDs**

**Request body** (`application/json`, required)

List of Ensembl transcript IDs. For example ["ENST00000420316", "ENST00000646891", "ENST00000371953"]

- `transcriptIds` (array of string) — List of Ensembl transcript IDs. For example ["ENST00000361390", "ENST00000361453", "ENST00000361624"]

**Responses**

- **200** — OK
  Body (`application/json`, array of object):
  - `ensemblTranscriptIds` (array of string)
  - `position` (integer (int32))
  - `pubmedIds` (array of string)
  - `sequence` (string)
  - `type` (string)
  - `uniprotAccession` (string)
  - `uniprotEntry` (string)

## info-controller

Info Controller

### GET /version

**Retrieve Genome Nexus Version**

**Responses**

- **200** — OK
  Body (`application/json`, object):
  - `version` (string)
