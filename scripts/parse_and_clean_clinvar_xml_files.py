import pandas as pd
from pathlib import Path
import xml.etree.ElementTree as ET 
import itertools
from collections import Counter

"""
1. I have downloded clinvar files from ncbi
2. parse the xmls
3. add the clinvar description to the data frame, for the corresponding RCV ID
"""

def _parse_xml(xml_file_path):
    """ str -> dict
    
    >>_parse_xml3("xml_out2/RCV000000180.xml")
    {'Description': 'Pathogenic/Likely pathogenic',
     'ReviewStatus': 'no assertion criteria provided'}
     
    >>_parse_xml3("xml_out2/RCV000039276.xml")
    {'Description': 'Conflicting interpretations of pathogenicity',
    'Explanation': 'Likely benign(1);Uncertain significance(1)',
    'ReviewStatus': 'criteria provided, conflicting interpretations'}
    """
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    res_out = {}
    # ReviewStatus
    for item in root.findall('./ClinVarSet/ReferenceClinVarAssertion/ClinicalSignificance/ReviewStatus'):
        res_out['ReviewStatus']=item.text
    # Description
    for item in root.findall('./ClinVarSet/ReferenceClinVarAssertion/ClinicalSignificance/Description'):
        res_out['Description']=item.text
    # Explanation
    for item in root.findall('./ClinVarSet/ReferenceClinVarAssertion/ClinicalSignificance/Explanation'):
        res_out['Explanation']=item.text
    return( res_out )

def _get_clinvar_attr( clinvar_dict, rcv ):
    """dict, str -> str
    Returns either clinvar description or review status
    
    >>_get_clinvar_attr(clinvar_desc, 'RCV000039276')
    'Conflicting interpretations of pathogenicity'
    >>_get_clinvar_attr(clinvar_revstat, 'RCV000039276')
    'criteria provided, conflicting interpretations'
    >>_get_clinvar_attr(clinvar_explanation, 'RCV000039276')
    'Likely benign(1);Uncertain significance(1)'
    """
    return( clinvar_dict.get(rcv) )

def add_attributes(DF, clinvar_attr, attr_name ):
    cnames_sort_order = DF.columns.tolist() + [attr_name]
    df_collector = []
    for e,i in enumerate( DF.CLINVAR_ID.tolist()):
        if isinstance(i, str):
            ss_rcv = i.split("; ")
            all_rcv_desc = []
            for each_rcv in ss_rcv :
                all_rcv_desc.append(_get_clinvar_attr(clinvar_attr, each_rcv.split('.')[0]))
            # messy 'nan'
            # To do
            #   clean this up later
            if all_rcv_desc == 'nan':
                all_rcv_desc_joined = all_rcv_desc
            else :
                all_rcv_desc_joined = all_rcv_desc
            
            tx = DF.loc[e] # get the series 
            tx2 = tx.append( pd.Series({attr_name : all_rcv_desc_joined}))
            df_collector.append( tx2.to_dict())
        else: 
            tx = DF.loc[e] # get the series
            tx2 = tx.append( pd.Series({attr_name:"none"}))
            df_collector.append( tx2.to_dict())
    df_clean = pd.DataFrame(df_collector)
    df_clean01 = df_clean[cnames_sort_order]
    return(df_clean01)


# the xml file loc
xml_out_fp="xml_out2"

# parse the xml data
lst = dict()
for i in sorted(Path(xml_out_fp).glob('*.xml')):
    lst[i.name.replace('.xml','')] = _parse_xml( str(i) )

df = pd.DataFrame( lst ).T

# Save the parsed info
df.to_csv("RCV_description_revstatus.csv", sep=',', index_label="RCV_ID")

# Dict for clinvar description 
clinvar_desc=df.Description.to_dict()

# Load the xls
dfx = pd.read_excel("Comined_CCF-SJ_IVA_PLP_02_021119.xlsx")
dfx.columns = [ i.replace(' ','_') for i in dfx.columns ]

# dicts
clinvar_desc=df.Description.to_dict()
clinvar_revstat=df.ReviewStatus.to_dict()
clinvar_explanation=df.Explanation.to_dict()

# add clinvar attributes to the data frame
c1 = add_attributes(dfx, clinvar_desc, 'CLINVAR_Description')
c2 = add_attributes(c1, clinvar_revstat, 'CLINVAR_ReviewStat')
c3 = add_attributes(c2, clinvar_explanation, 'CLINVAR_Explanation')

# Save the new df containing cleaned clinvar headers
c3.to_excel("Cleanded_CLINVAR_01.xls", index=False)









