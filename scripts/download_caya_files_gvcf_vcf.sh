
# usage : bash download_caya_files.sh CANCER_TYPE DIR &>> cancer_type.log 2>&1

CTYPE=$1
BDIR=$2

# -------------Make Res Dir-------------------------
if [ ! -d "$BDIR" ]; then
	mkdir $BDIR
fi
#---------------------------------------------------

echo -ne "INFO:"$(date)":-----Downoad manifest for $1 ----: "; echo $CTYPE
dx find data --property  sj_diseases=$CTYPE --property sample_type="germline" --property sequencing_type="WES"  >$BDIR/$CTYPE.tab

echo -ne "INFO:"$(date)":-----Total Number of lines in $1 -----: "; wc -l $BDIR/$CTYPE.tab ;

# GVCF
nl_gVCF=`grep gVCF $BIDR/CTYPE.tab`

# VCF
nl_VCF=`grep gVCF -v $BIDR/CTYPE.tab`

echo -ne "INFO:"$(date)":-----Total Number of VCF files in $1-----: "; wc -l $BDIR/$CTYPE.gvcf.tab ;
echo -ne "INFO:"$(date)":-----Total Number of gVCF files in $1-----: "; wc -l $BDIR/$CTYPE.vcf.tab ;

if [ nl_gVCF >= 1 ]; then
	grep  gVCF $BDIR/$CTYPE.tab > $BDIR/$CTYPE.gvcf.tab;
	awk '{print $6}' $BDIR/$CTYPE.gvcf.tab  | sort | xargs -I {} echo dx download -f {} | split -l 10 - download_${CTYPE}_gvcf_ -d --additional-suffix .sh;
	ls download_${CTYPE}_gvcf_*.sh | sed s'/.sh//'| xargs -I {} echo "bash {}.sh &>>{}.log 2>&1" >>run_gvcf_download.sh;
	#mv download_${CTYPE}_gvcf_*.sh $BDIR >>run_gvcf_download.sh;
fi

echo

if [ nl_VCF >= 1 ]; then
	grep  gVCF -v $BDIR/$CTYPE.tab > $BDIR/$CTYPE.vcf.tab
	awk '{print $6}' $BDIR/$CTYPE.vcf.tab  | sort | xargs -I {} echo dx download -f {} | split -l 10 - download_${CTYPE}_vcf_ -d --additional-suffix .sh;
	ls download_${CTYPE}_vcf_*.sh | sed s'/.sh//'| xargs -I {} echo "bash {}.sh &>>{}.log 2>&1" >>run_vcf_download.sh ;
	#mv download_${CTYPE}_vcf_*.sh $BDIR >>run_vcf_download.sh;
fi


echo  "INFO:"$(date)":-----check run_x_download.sh-----: "; 

