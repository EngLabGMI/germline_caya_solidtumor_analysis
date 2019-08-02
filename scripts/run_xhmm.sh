## Second script in the XHMM pipeline
## RUN AS run_xhmm.sh &>> xhmm_$(date +%Y%m%d_%s ).log 2>&1

GATK3_5="/home/padmanr/eng_lab/NGS_Working/niazif-share/Farshad/GATK3.5/GenomeAnalysisTK.jar"
OUT_DIR="/home/padmanr/eng_lab/NGS_Working/Roshan_Padmanabhan/projects/Sara/XHMM/results/res20180828"
BAM_43_LIST=$OUT_DIR"/bam.43.list"
BAM_6_LIST=$OUT_DIR"/bam.6.list"
BAM_LIST=$OUT_DIR"/bam.list"
PARAM_FILE=$OUT_DIR"/params.txt"
EXOM_BED="/home/padmanr/eng_lab/NGS_Working/Roshan_Padmanabhan/projects/Sara/XHMM/data/new_file_june5.sorted.bed"
REF_FAS_FAR="/home/padmanr/eng_lab/NGS_Working/niazif-share/Farshad/LIBRARY_FILES/hg19.fa"
REF_FAS="/home/padmanr/eng_lab/NGS_Working/Roshan_Padmanabhan/projects/Sara/XHMM/references/human_g1k_v37.fasta"


# DATA.RD.txt is the merged depth of cov file

echo "INFO:"$(date)":-----Step 2 center the data-----:"
xhmm --matrix -r $OUT_DIR/DATA.RD.txt \
    --centerData --centerType target \
    -o $OUT_DIR/DATA.filtered_centered.RD.txt \
    --outputExcludedTargets $OUT_DIR/DATA.filtered_centered.RD.txt.filtered_targets.txt \
    --outputExcludedSamples $OUT_DIR/DATA.filtered_centered.RD.txt.filtered_samples.txt 
    #--minTargetSize 10 --maxTargetSize 10000 \
    #--minMeanTargetRD 10 --maxMeanTargetRD 500 \
    #--minMeanSampleRD 25 --maxMeanSampleRD 200 \
    #--maxSdSampleRD 150

echo "INFO:"$(date)":-----Step 3 Runs PCA on mean-centered data -----:"
xhmm --PCA -r $OUT_DIR/DATA.filtered_centered.RD.txt --PCAfiles $OUT_DIR/DATA.RD_PCA


echo "INFO:"$(date)":-----Step 4 Normalizes mean-centered data using PCA information -----:"
xhmm --normalize \
    -r $OUT_DIR/DATA.filtered_centered.RD.txt \
    --PCAfiles $OUT_DIR/DATA.RD_PCA \
    --normalizeOutput $OUT_DIR/DATA.PCA_normalized.txt \
    --PCnormalizeMethod PVE_mean --PVE_mean_factor 0.7

echo "INFO:"$(date)":-----Step 5 Filters and z-score centers (by sample) the PCA-normalized data -----:"
xhmm --matrix \
    -r $OUT_DIR/DATA.PCA_normalized.txt \
    --centerData --centerType sample --zScoreData \
    -o  $OUT_DIR/DATA.PCA_normalized.filtered.sample_zscores.RD.txt \
    --outputExcludedTargets $OUT_DIR/DATA.PCA_normalized.filtered.sample_zscores.RD.txt.filtered_targets.txt \
    --outputExcludedSamples $OUT_DIR/DATA.PCA_normalized.filtered.sample_zscores.RD.txt.filtered_samples.txt \
    --maxSdTargetRD 30

echo "INFO:"$(date)":-----Step 6 Filters original read-depth data to be the same as filtered, normalized data -----:"
xhmm --matrix -r $OUT_DIR/DATA.RD.txt \
    --excludeTargets $OUT_DIR/DATA.filtered_centered.RD.txt.filtered_targets.txt \
    --excludeTargets $OUT_DIR/DATA.PCA_normalized.filtered.sample_zscores.RD.txt.filtered_targets.txt \
    --excludeSamples $OUT_DIR/DATA.filtered_centered.RD.txt.filtered_samples.txt \
    --excludeSamples $OUT_DIR/DATA.PCA_normalized.filtered.sample_zscores.RD.txt.filtered_samples.txt \
    -o $OUT_DIR/DATA.same_filtered.RD.txt

echo "INFO:"$(date)":-----Step 7 Discovers CNVs in normalized data -----:"
xhmm --discover -p $OUT_DIR/params.txt \
    -r $OUT_DIR/DATA.PCA_normalized.filtered.sample_zscores.RD.txt  \
    -R $OUT_DIR/DATA.same_filtered.RD.txt \
    -c $OUT_DIR/DATA.xcnv -a $OUT_DIR/DATA.aux_xcnv -s $OUT_DIR/DATA

echo "INFO:"$(date)":-----Step 8 Genotypes discovered CNVs in all samples -----:"
xhmm -G -p $OUT_DIR/params.txt -r $OUT_DIR/DATA.PCA_normalized.filtered.sample_zscores.RD.txt  -R $OUT_DIR/DATA.same_filtered.RD.txt -g .$OUT_DIR/DATA.xcnv -F $REF_FAS_FAR -v $OUT_DIR/DATA.vcf
    
