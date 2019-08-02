##
## XHMM script is broken down to three scripts
## This first script makes the depth of coberage of Group 1 and Group 2
## Next script run_xhmm.sh runs the rest of the steps in XHMM
## Last step is plotting the data
## Which is in the three script make_plots.sh
##

GATK3_5="/home/padmanr/eng_lab/NGS_Working/niazif-share/Farshad/GATK3.5/GenomeAnalysisTK.jar"
OUT_DIR="/home/padmanr/eng_lab/NGS_Working/Roshan_Padmanabhan/projects/Sara/XHMM/results/res20180823"
BAM_43_LIST=$OUT_DIR"/bam.43.list"
BAM_6_LIST=$OUT_DIR"/bam.6.list"
PARAM_FILE=$OUT_DIR"/params.txt"
EXOM_BED="/home/padmanr/eng_lab/NGS_Working/Roshan_Padmanabhan/projects/Sara/XHMM/data/new_file_june5.sorted.bed"
REF_FAS_FAR="/home/padmanr/eng_lab/NGS_Working/niazif-share/Farshad/LIBRARY_FILES/hg19.fa"
REF_FAS="/home/padmanr/eng_lab/NGS_Working/Roshan_Padmanabhan/projects/Sara/XHMM/references/human_g1k_v37.fasta"

echo "INFO:"$(date)":-----Step 1 DepthCov with GATK for G1-----:"
java -Xmx11g -jar  $GATK3_5 \
    -T DepthOfCoverage -I $BAM_43_LIST \
    -L $EXOM_BED \
    -R $REF_FAS_FAR \
    -dt BY_SAMPLE  -dcov 5000 \
    -l INFO --omitDepthOutputAtEachBase \
    --omitLocusTable --minBaseQuality 0 \
    --minMappingQuality 20 --start 1 --stop 5000  --nBins 200 \
    --includeRefNSites --countType COUNT_FRAGMENTS -o $OUT_DIR/G1_DATA.RD.txt

echo "INFO:"$(date)":-----Step 1 DepthCov with GATK for G2-----:"
java -Xmx11g -jar  $GATK3_5 \
    -T DepthOfCoverage -I $BAM_6_LIST \
    -L $EXOM_BED \
    -R $REF_FAS_FAR \
    -dt BY_SAMPLE  -dcov 5000 \
    -l INFO --omitDepthOutputAtEachBase \
    --omitLocusTable --minBaseQuality 0 \
    --minMappingQuality 20 --start 1 --stop 5000  --nBins 200 \
    --includeRefNSites --countType COUNT_FRAGMENTS -o $OUT_DIR/G2_DATA.RD.txt

echo "INFO:"$(date)":-----Step 1a Merge GATK Depths-----:"
xhmm --mergeGATKdepths  -o $OUT_DIR/DATA.RD.txt \
    --GATKdepths $OUT_DIR/G1_DATA.RD.txt.sample_interval_summary \
    --GATKdepths $OUT_DIR/G2_DATA.RD.txt.sample_interval_summary

bash ./run_xhmm.sh

##
##
## For running the step2 onwards, copy the 
## DATA.RD.txt 
## DATA.filtered_centered.RD.txt.filtered_targets.txt
## DATA.filtered_centered.RD.txt.filtered_samples.txt
##
##

