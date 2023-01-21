import numpy as np
import numpy.linalg as la
import pandas as pd
import matplotlib as plt
def DataCleans(df,P5_only_on):

    df.loc[(df['DR']=='UDFA'),'DR']=8
    df.loc[(df['DP']=='UDFA'),'DP']=260
    df=df.replace('-',np.nan)
    Pow5=['Big 12','ACC','SEC','Pac-12','Big Ten']

    if P5_only_on==1:
        df=df[(df['Conf'].isin(Pow5))]




    return df




def pred(df, train,targ,predictor_year):
    dfstore=df
    df=df.dropna(subset=[targ])
    df=df.dropna(subset=train)

    seas=df.reset_index()
    targ_vals=seas[targ].to_frame()
    targ_vals=targ_vals.apply(pd.to_numeric, errors='coerce')

    xarg_vals=seas[train]
    col_o_1s=pd.DataFrame(index=np.arange(len(xarg_vals)),columns=['1cols'])
    col_o_1s.loc[:,:]=1

    xarg_vals['1col']=col_o_1s
    xarg_vals=xarg_vals.apply(pd.to_numeric, errors='coerce')
    xarg_vals=xarg_vals.to_numpy()

    w=np.dot(la.pinv(xarg_vals),targ_vals)

    #Now pull rookies 
    rooks=dfstore
    rooks=rooks.loc[(rooks['Draft Year'].isin(predictor_year)) & (rooks['DR']!='UDFA')]
    rooksvals=rooks[train]
    rooksvals['1col']=col_o_1s
    
    rookpred=np.dot(rooksvals,w)
    output_data=['Player','Draft Year','School']
    name_store=rooks[output_data]
    predicted=pd.DataFrame(pd.np.column_stack([name_store,rookpred]))

    return predicted

