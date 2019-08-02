
# Data Analysis for :  Diverse Genes with Germline Variants Converging on p53 Network May Predispose to Solid Tumors in Children, Adolescents, and Young Adults

- This github dir contains the data analysis jupyter notebooks, scripts and data tables accompaning the paper :  ```Diverse Genes with Germline Variants Converging on p53 Network May Predispose to Solid Tumors in Children, Adolescents, and Young Adults```
	- GermLine Analysis of Children, Adolescents, and Young Adults (C-AYA) with SolidTumor  
- Authors :  ```Sara Akhavanfard, Roshan Padmanabhan, Lamis Yehia, Feixiong Cheng, Charis Eng```

## Abstract

> Compared to adult carcinomas, there is a paucity of targeted treatments for solid tumors in children, adolescents, and young adults (C-AYA). The impact of germline genomic signatures has implications for heritability, but its impact on targeted treatment selection has not been fully appreciated. To address this gap, we performed variant-prioritization analysis, based on the American College of Medical Genetics and Genomics (ACMG) classification guidelines, on germline exome sequencing data of 1507 C-AYA patients with solid tumors. We identified 12% of these patients carrying germline pathogenic and/or likely pathogenic (P/LP) mutations in 54 of 203 known cancer-predisposing genes (KCPG), including RB1, NF1, and TP53, while adding 1 to 19 unexpected KCPG for each of adrenocortical carcinoma, astrocytoma, CNS tumors, Ewing sarcoma, neuroblastoma, osteosarcoma, retinoblastoma, soft tissue sarcoma, and Wilms tumor. An additional 61% had germline pathogenic mutations in non-KCPG genes, including PRKN, MCPH1, SMARCAL1, SMAD7, which we refer to as “candidate” genes. The frequency of germline mutations in C-AYA solid tumor patients found here would suggest that all C-AYA presentations of malignancy should be referred to germline testing in the setting of genetic counseling. Despite germline mutations in a broad gene spectrum, pathway analysis led to top canonical pathways and networks centering around p53. Our drug-target network analysis showed that more than one-third of patients with germline P/LP mutations had at least one druggable gene, with 31.5% of those genes having existing approved antineoplastic drugs. More than half of these gene-target candidates are from our “candidate” gene group, which would otherwise go unidentified in routine clinical care.
- Significance
> We show a broad spectrum of genes that may predispose to C-AYA solid tumors, yet with downstream pathways converging on the p53 network. Our drug-target network data uphold the importance of precision oncology practices for all C-AYA solid tumors, which currently have a paucity of targeted treatments, and suggest the immediate need for C-AYA-specific “basket” (i.e., by gene or pathway) clinical trials. The relatively high frequency of germline mutations in C-AYA solid tumor presentations implies that all such presentations be referred for germline testing.

## Contents
### IVA Filteration Parameters

- [CCF_CAYA_IVA_variant_filtertion_params](CCF_IVA_variant_filteration_parms_1012519.md)
- [StJude CAYA IVA variant filteration params](StJude_IVA_variant_filteration_1012819.md)

### Analysis
  - [Known Cancer Predisposing Genes (KCPG)](analysis/KCPG)
        -[KCPG_woAR_Oncoplot](KCPG_woAR_Oncoplot.ipynb)
        -[KCPG_Heatmap](KCPG_Heatmap.ipynb)
        -[KCPG_LollipopPlots](KCPG_LollipopPlots.ipynb)
        -[KCPG_woAR_TT-AdrenocorticalCarcinoma_Oncoplot](KCPG_woAR_TT-AdrenocorticalCarcinoma_Oncoplot.ipynb)
        -[KCPG_woAR_TT-Carcinoma_Oncoplot](KCPG_woAR_TT-Carcinoma_Oncoplot.ipynb)
        -[KCPG_woAR_TT-CentralNervousSystem_Oncoplot](KCPG_woAR_TT-CentralNervousSystem_Oncoplot.ipynb)
        -[KCPG_woAR_TT-EwingsSarcoma_Oncoplot](KCPG_woAR_TT-EwingsSarcoma_Oncoplot.ipynb)
        -[KCPG_woAR_TT-GermCellTumor_Oncoplot](KCPG_woAR_TT-GermCellTumor_Oncoplot.ipynb)
        -[KCPG_woAR_TT-HighGradeGlioma_Oncoplot](KCPG_woAR_TT-HighGradeGlioma_Oncoplot.ipynb)
        -[KCPG_woAR_TT-LowGradeGlioma_Oncoplot](KCPG_woAR_TT-LowGradeGlioma_Oncoplot.ipynb)
        -[KCPG_woAR_TT-Neuroblastoma_Oncoplot](KCPG_woAR_TT-Neuroblastoma_Oncoplot.ipynb)
        -[KCPG_woAR_TT-Osteosarcoma_Oncoplot](KCPG_woAR_TT-Osteosarcoma_Oncoplot.ipynb)
        -[KCPG_woAR_TT-OtherSolidTumor_Oncoplot](KCPG_woAR_TT-OtherSolidTumor_Oncoplot.ipynb)
        -[KCPG_woAR_TT-Retinoblastoma_Oncoplot](KCPG_woAR_TT-Retinoblastoma_Oncoplot.ipynb)
        -[KCPG_woAR_TT-Rhabdomyosarcoma_Oncoplot](KCPG_woAR_TT-Rhabdomyosarcoma_Oncoplot.ipynb)
        -[KCPG_woAR_TT-SoftTissueSarcoma_Oncoplot](KCPG_woAR_TT-SoftTissueSarcoma_Oncoplot.ipynb)
        -[KCPG_woAR_TT-Wilmstumor_Oncoplot](KCPG_woAR_TT-Wilmstumor_Oncoplot.ipynb)  
  - [Candidate Genes](analysis/Candidate)
        -[CandidateGenes_Oncoplot](CandidateGenes_Oncoplot.ipynb)
        -[CandidateGenes_Heatmap](CandidateGenes_Heatmap.ipynb)
        -[CandidateGenes_LollipopPlots](CandidateGenes_LollipopPlots.ipynb)
        -[CandidateGenes_TT-AdrenocorticalCarcinoma_Oncoplot](CandidateGenes_TT-AdrenocorticalCarcinoma_Oncoplot.ipynb)
        -[CandidateGenes_TT-Carcinoma_Oncoplot](CandidateGenes_TT-Carcinoma_Oncoplot.ipynb)
        -[CandidateGenes_TT-CentralNervousSystem_Oncoplot](CandidateGenes_TT-CentralNervousSystem_Oncoplot.ipynb)
        -[CandidateGenes_TT-EwingsSarcoma_Oncoplot](CandidateGenes_TT-EwingsSarcoma_Oncoplot.ipynb)
        -[CandidateGenes_TT-GermCellTumor_Oncoplot](CandidateGenes_TT-GermCellTumor_Oncoplot.ipynb)
        -[CandidateGenes_TT-HighGradeGlioma_Oncoplot](CandidateGenes_TT-HighGradeGlioma_Oncoplot.ipynb)
        -[CandidateGenes_TT-LowGradeGlioma_Oncoplot](CandidateGenes_TT-LowGradeGlioma_Oncoplot.ipynb)
        -[CandidateGenes_TT-Neuroblastoma_Oncoplot](CandidateGenes_TT-Neuroblastoma_Oncoplot.ipynb)
        -[CandidateGenes_TT-Osteosarcoma_Oncoplot](CandidateGenes_TT-Osteosarcoma_Oncoplot.ipynb)
        -[CandidateGenes_TT-OtherSolidTumor_Oncoplot](CandidateGenes_TT-OtherSolidTumor_Oncoplot.ipynb)
        -[CandidateGenes_TT-Retinoblastoma_Oncoplot](CandidateGenes_TT-Retinoblastoma_Oncoplot.ipynb)
        -[CandidateGenes_TT-Rhabdomyosarcoma_Oncoplot](CandidateGenes_TT-Rhabdomyosarcoma_Oncoplot.ipynb)
        -[CandidateGenes_TT-SoftTissueSarcoma_Oncoplot](CandidateGenes_TT-SoftTissueSarcoma_Oncoplot.ipynb)
        -[CandidateGenes_TT-Wilmstumor_Oncoplot](CandidateGenes_TT-Wilmstumor_Oncoplot.ipynb)
  - [C-AYA Patiants with solid tumors vs NonTCGA-ExAC controls](analysis/CAYA_vs_NonTCGA-ExAc)
        -[Freq_Plot_of_CAYA_vs_NonTCGA-ExAc](Freq_Plot_of_CAYA_vs_NonTCGA-ExAc.ipynb)
  - [Congential Heart Defects (CHD) Related Genes / Variants](analysis/CHD)
        -[CHD_only_monoallelic_Oncoplots](CHD_only_monoallelic_Oncoplots.ipynb)
        -[CHD_monoallelic_Heatmap](CHD_monoallelic_Heatmap.ipynb)
### Data
- table dir contain the supplimentary excel files
### Scripts 
- includes inhouse scipts to process the data


***
