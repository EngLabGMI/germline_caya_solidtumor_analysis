
ls *.g.vcf.gz | sed s:.g.vcf.gz::  | xargs -I {} echo "bcftools view {}.g.vcf.gz | grep '0/0:' -v > {}.N.vcf" | parallel -j 30
ls *.vcf | cut -d "/" -f 3 | cut -d '.' -f 1 | xargs -I {} echo "bgzip {}.Exome.N.vcf" | parallel -j 30
ls *.vcf.gz | cut -d "/" -f 3 | cut -d '.' -f 1 | xargs -I {} echo "tabix -pvcf {}.Exome.N.vcf.gz" | parallel -j 30

mkdir data1 data2
mv *.g.* data1
mv *.N.* data2 

