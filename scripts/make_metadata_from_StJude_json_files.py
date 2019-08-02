
"""
This script makes a csv file of metadata 
   - from the meta data I downloaded from StJude
Author : Roshan Padmanabhan
Date : 29Jan2018
env : python3
"""

import pandas as pd
import pathlib

loc="../MetaData/"
locx = pathlib.Path(loc)
files = locx.glob("*.vcf.gz.json")
files_list = [ i for i in files ]

def _make_df( file ):
    res = []
    tdf = pd.read_json( str( file ) ).T
    colnames = [ i for i in tdf.to_dict()[0] ]
    X = tdf.to_dict()[0]
    for i in colnames :
        if isinstance( X.get(i) , dict ):
            x = pd.Series( X.get(i))
            for e,k in enumerate( x.index) :
                    res.append([ k,x[e]] )
        else :
            res.append( [i,X.get(i)] )
    resx = pd.DataFrame(res,  columns=["ATTRIBUTES", X.get('name')])
    resx.set_index( keys='ATTRIBUTES' , inplace=True )
    return( resx )
    
res = []
for i in files_list:
    res.append(  _make_df(i) )
t1 = pd.concat( res, axis=1, sort=True)
t1 = t1.T
t1.to_csv("T1.csv")