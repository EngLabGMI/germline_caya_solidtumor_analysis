author='roshan padmanabhan'
version=0.02
date='31Jan2019'

"""
- there are 181 variants
- each variants could come from multiple samples
- so the aim is to split the variant from each sample into differnt rows
- also adding a few more data  for each variant
"""

import pandas as pd
#indf = pd.read_excel( "IVA-test.xlsx", sheetname="input")
#indf = pd.read_excel( "StJude-1-012819_GeneticAnalysis_020519.xlsx")
indf = pd.read_excel( "Normalcases_1_PLP_021219_GeneticAnalysis.xlsx")

indf_col_list = indf.columns.tolist()
lst_nx = ['- Copy Number','- Inferred Activity','- Genotype','- Compound Heterozygous','- Call Quality','- Allele Fraction','- Read Depth']

copy_number = [ i for i in indf_col_list  if lst_nx[0] in i ]
inferred_activity = [ i for i in indf_col_list if lst_nx[1] in i ]
genotype = [ i for i in indf_col_list if lst_nx[2] in i ]
compound_heterozygous = [ i for i in indf_col_list if lst_nx[3] in i ]
call_quality = [ i for i in indf_col_list if lst_nx[4] in i ]
allele_fraction = [ i for i in indf_col_list if lst_nx[5] in i ]
read_depth = [ i for i in indf_col_list if lst_nx[6] in i ]

rest_nx = []
for i in indf_col_list:
        if lst_nx[0] in i :
            pass
        elif lst_nx[1] in i :
            pass
        elif lst_nx[2] in i :
            pass
        elif lst_nx[3] in i :
            pass
        elif lst_nx[4] in i :
            pass
        elif lst_nx[5] in i :
            pass
        elif lst_nx[6] in i :
            pass
        else :
            rest_nx.append( i )  

# subsetting out the data 

inferred_activity_df = indf[inferred_activity]
genotype_df = indf[genotype]
compound_heterozygous_df = indf[compound_heterozygous]
call_quality_df = indf[call_quality]
read_depth_df = indf[read_depth]
allele_fraction_df = indf[allele_fraction]
copy_number_df = indf[copy_number]

dfx = indf[rest_nx]

sample_attr_list = [inferred_activity,genotype, compound_heterozygous, call_quality, read_depth,allele_fraction, copy_number  ]

sample_df = {"inferred_activity" : inferred_activity_df,
"genotype": genotype_df,
"compound_heterozygous" : compound_heterozygous_df,
"call_quality" : call_quality_df,
"read_depth" : read_depth_df,
"allele_fraction" : allele_fraction_df,
"copy_number" : copy_number_df}

# keep this copy of list for final sorting
rn = rest_nx.copy()
rn = rn + [ i for i in sample_df.keys() ]

def _get_case_sample( csamp , attribute_lst ):
    """Return a column id 
    """
    x = [ i  for i in attribute_lst if csamp in i ][0]
    return(x)

def _get_case_values( case_id , index_id, sample_attr_list, sample_df):
    """[Return  a dict of sample attributes like inferred_activity \
    copy_number , genotype etc. ]
    Arguments:
        case_id {[str]} -- [case column id to search]
        index_id {[int]} -- [each row of the dfx data frame | variant number]
    """
    res = dict()
    for i in sample_attr_list :
        case_activity_id = _get_case_sample( csamp=case_id, attribute_lst=i )
        new_case_id = case_activity_id.split(' - ')[1].replace(' ','_').lower()
        # get each attribute values
        fdf = sample_df.get(new_case_id)
        res[ new_case_id] = fdf[  case_activity_id  ][index_id]
    return( res )

def _clean_case_samples(longstr):
    csamples = [ i for i in longstr.split(';') if not i.startswith('-') ]
    return( csamples)

def _clean_sample_genotype_quality(longstr):
    sgq = [ i for i in longstr.split('; ') if not i.startswith('-') ]
    return( sgq)

def _clean_sample_genotype_quality(longstr):
    sgq = [ i for i in longstr.split('; ') if not i.startswith('-') ]
    return( sgq)

def _single_row(index_id, each_case , sample_attr_list, sample_df):
    """Returns a dictionary of the row, along with the cleaned attribute values
    Arguments:
        index_id {int} -- [each row of the dfx data frame | variant number]
        each_case {str} -- [a single Case Sample name]
    """
    # get the index 
    cs = dfx.loc[index_id].loc['Case Samples']
    cs_n = _clean_case_samples(cs)
    cs_n_index = cs_n.index(each_case)

    res = dict()
    att_val_dict =  _get_case_values( each_case, index_id, sample_attr_list, sample_df)
    for each_colname in dfx.columns :
        if each_colname == 'Case Samples':
            cs = dfx.loc[index_id].loc[each_colname]
            #print(cs)
            res[each_colname] =  _clean_case_samples(cs)[cs_n_index]
        elif each_colname == 'Sample Genotype Quality':
            cs = dfx.loc[index_id].loc[each_colname]
            #print("Sample Genotype Quality : ", cs)
            try:
                csX = _clean_sample_genotype_quality(cs)[cs_n_index]
                res[each_colname] =csX
            except IndexError as e:
                res[each_colname] =_clean_sample_genotype_quality(cs)
        elif each_colname == 'Sample Upstream Filtering':
            cs = dfx.loc[index_id].loc[each_colname]
            #print("Sample Upstream Filtering : ", cs)
            try:
                csX = _clean_sample_genotype_quality(cs)[cs_n_index]
                res[each_colname] = csX
            except IndexError as e:
                res[each_colname] =_clean_sample_genotype_quality(cs)
        else :
            rest_of_the_values = dfx.loc[index_id].loc[each_colname]
            res[each_colname] = rest_of_the_values
    res.update( att_val_dict )
    return(res)

collect_dfs = []
for e, i in  enumerate( range(0,dfx.shape[0] )) :
        lname = dfx.loc[i].loc["Case Samples"]
        xxx = _clean_case_samples( lname )
        #print( e, i, ">>>", xxx )
        for each_case in xxx :
            s_x = pd.Series( _single_row( index_id=i, each_case=each_case , sample_attr_list=sample_attr_list, sample_df=sample_df) )
            s_x.name = each_case
            s_x.loc["Case Samples"] = s_x.name
            s_x = s_x[rn]
            #print( e, i, each_case, "--------------\n", s_x.head(10)  )
            collect_dfs.append( s_x )

X = pd.concat(collect_dfs, axis =1)
X = X.T[rn]
X.to_csv("Clean_output_Noraml_01.csv")
