
# usage : download_caya_files.sh BT &>> cancer_type.log 2>&1

CTYPE=$1
BDIR="../data"

echo -ne "INFO:"$(date)":-----Downoad manifest for CTYPE-----: "; echo $CTYPE
dx find data --property  sj_diseases=$CTYPE --property sample_type="germline" --property sequencing_type="WES"  >$BDIR/$CTYPE.tab
echo -ne "INFO:"$(date)":-----Total Number of lines in CTYPE-----: "; wc -l $BDIR/$CTYPE.tab ;
echo -ne "INFO:"$(date)":-----sanity check CTYPE-----: "; grep ".gz " $BDIR/$CTYPE.tab | nl | tail -3
echo  "INFO:"$(date)":-----Download files CTYPE-----: "; 
awk '{print $6}' $BDIR/$CTYPE.tab  | sort | xargs -I {} echo dx download -f {} | split -l 10 - download_${CTYPE}_ -d --additional-suffix .sh


echo  "INFO:"$(date)":----Run it in parallel from data dir-----: ";
ls download_${CTYPE}_*.sh | sed s'/.sh//'| xargs -I {} echo "bash {}.sh &>>{}.log 2>&1" 

mv download_${CTYPE}_*.sh $BDIR 

