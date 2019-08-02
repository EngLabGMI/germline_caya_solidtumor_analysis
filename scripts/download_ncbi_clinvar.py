import pandas as pd
from os.path import join, exists
from os import mkdir
from pathlib import Path
import itertools
import requests
import logging
import time
from collections import Counter

"""
1. The results of IVA contains clinvar id
2. This script downloads the clinvar data as xml files from ncbi
"""

__author__ = 'Roshan Padmanabhan'
__version__ = 0.1

def _make_dir(fp):
    if exists(fp):
        pass
    else :
        mkdir(fp)

def _make_logger( namex ):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    # create a file handler
    handler = logging.FileHandler(namex+'_'+time.ctime().replace(' ','_').replace(':','-')+'.log')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return( logger )

def search_clinvar(rcv, out_loc ):
    recent_rcv = rcv.split(".")[0]
    url ="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
    payload={'db':'clinvar','rettype':'clinvarset', 'id':recent_rcv}
    out_file_name=join( out_loc , recent_rcv +'.xml')
    resp = requests.post(url, data=payload)
    if resp.status_code == 200 :
        # save the xml file 
        with open( out_file_name, 'wb') as f: 
            f.write(resp.content)
        return([recent_rcv,out_file_name,resp.status_code])
    else :
        return([recent_rcv,out_file_name,resp.status_code])

log = _make_logger("ClinVar-Scrap")
log.info('Loading the xls into pandas data frame\n')
df = pd.read_excel("Comined_CCF-SJ_IVA_PLP_02_021119.xlsx")
all_rcvs = list(itertools.chain(*[i.split('; ') for i in df['CLINVAR ID'] if not isinstance( i, float) ])) 
log.info('Total Number of RCVs in the data frame : {}'.format(len( all_rcvs )))
# make the dir
xml_out_fp="xml_out"
_make_dir(xml_out_fp)
log.info('Start send request to ClinVar db\n')

# loop around all rcv ids from df and download the data
for e,i in enumerate( all_rcvs ):
    log.info(': {} :Querying {} to ClinVar db'.format(e,i))
    res = search_clinvar(i, xml_out_fp )
    log.info('Clinical RCV xml file {} downloaded with the status of {} \n'.format(res[0],res[2]))

log.info("Done Downloading the data")






