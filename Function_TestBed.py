import numpy as np
import numpy.linalg as la
import pandas as pd
import matplotlib as plt
from functionsFFDataMan import *

db=pd.read_excel("NewQBProspects.xlsx")

testdb=DataCleans(db,1)


print('done')