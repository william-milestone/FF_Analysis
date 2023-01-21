import numpy as np
import numpy.linalg as la
import pandas as pd
import matplotlib as plt
from functionsFFDataMan import *
#Pull database info database=original database for ref, pros=prospect database after cleansing
POS='WR'
database=pd.read_excel("New"+POS+"Prospects.xlsx")

#Call database cleaning
pros=DataCleans(database,0)

t_columns='AVG PPG YR 1-3'
training_columns=['DR','AVGREC Yards/TM PA','AVGTouch/Team Attempt']


output=pred(pros,training_columns,t_columns,2021)

print('wait')