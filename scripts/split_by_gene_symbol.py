"""
This script splits the MAF csv file @ Hugo Symbol into separate rows
"""

import pandas as pd

df = pd.read_csv("Clean_output_Noraml_01.csv", sep=",")

collector = []
for e,i in enumerate( df.Hugo_Symbol.tolist() ):
    lnx = df.loc[e].to_dict()
    nX =i.split('; ')
    if len(nX) >1 :
        for x in nX :
            lnx = df.loc[e].to_dict()
            #print( '>>', e,lnx.get('Hugo_Symbol'), x )
            lnx.update({'Hugo_Symbol': x })
            #print( '>>>',e, lnx.get('Hugo_Symbol'), x )
            collector.append(lnx)
    else :
        collector.append(lnx)
        #print( '>',e, lnx.get('Hugo_Symbol') )

dfX = pd.DataFrame( collector )
dfX = dfX[df.columns.tolist()]

dfX.to_csv("Clean_output_Noraml_02.csv", index=False)

