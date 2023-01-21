import numpy as np
import numpy.linalg as la
import pandas as pd
import matplotlib as plt

database=pd.read_excel("QBProspects.xlsx")
seas=pd.read_excel("QBProspects.xlsx")
seas=seas.replace('-',np.nan)
t_columns='AVG PPG YR 1-3'

#print(seas[t_columns])
x=['Pass Yards/GP.1','Rush Yards/GP.1']

test_frame=seas.dropna(subset=[t_columns])
test_frame=test_frame.dropna(subset=x)
seas=test_frame.reset_index()
targ_vals=seas[t_columns].to_frame()



xarg_vals=seas[x]
print(len(xarg_vals))
col_o_1s=pd.DataFrame(index=np.arange(len(xarg_vals)),columns=['1cols'])

col_o_1s.loc[:,:]=1

test_xargs=xarg_vals
xarg_vals['1col']=col_o_1s
xarg_vals=xarg_vals.apply(pd.to_numeric, errors='coerce')
xarg_vals=xarg_vals.to_numpy()

w=np.dot(la.pinv(xarg_vals),targ_vals)


#Compute now for 2022 Rookies
QBRook=pd.read_excel("QBProspects.xlsx")

QBRook=QBRook.loc[(QBRook['Draft Year']==2022) & (QBRook['DR']!='UDFA')]
QBRookvals=QBRook[x]
QBRookvals['1col']=col_o_1s

QBpred=np.dot(QBRookvals,w)


pred_vals=QBRook['Player']

predicted=pd.DataFrame(pd.np.column_stack([pred_vals,QBpred]))
print('done')