import pandas as pd
import matplotlib as plt
import numpy as np
import seaborn as sns
data = pd.read_csv('./DATA/RAW/GSE81089/FPKM_cufflinks.tsv', sep='\t',header =None)
data_T = data.T
data_T = data_T.drop(0,axis=1)
data_T_columns = data_T[0:1]
data_T =  data_T.drop(0,axis=0)
data_T.columns=data_T_columns.values.tolist()
data_T = data_T.reset_index(drop=True)
data_T=data_T.astype(float)
data_T.corr()