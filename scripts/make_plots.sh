OUT_DIR="/home/padmanr/eng_lab/NGS_Working/Roshan_Padmanabhan/projects/Sara/XHMM/results/res20180823"
BAM_LIST=$OUT_DIR"/bam.list"
EXOM_BED="/home/padmanr/eng_lab/NGS_Working/Roshan_Padmanabhan/projects/Sara/XHMM/data/new_file_june5.sorted.bed"
LOCAL_DB="/home/padmanr/eng_lab/NGS_Working/Roshan_Padmanabhan/projects/Sara/XHMM/references/locdb"

pseq . loc-intersect --group refseq --locdb $LOCAL_DB --file $EXOM_BED --out $OUT_DIR"/annotated_targets.refseq"

#R < example_make_XHMM_plots.R --save

