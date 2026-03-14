import pandas as pd
import numpy as np


data_DF1=pd.read_csv("musae_git_edges.csv")
print(data_DF1.columns)

data_DF2=pd.read_csv("edges.csv")
print(data_DF2.columns)


numerical_df1 = data_DF1.select_dtypes(include=['number'])
print(numerical_df1.columns)


numerical_df2 = data_DF2.select_dtypes(include=['number'])
print(numerical_df2.columns)


mean1=data_DF1.mean("id_2")
print(mean1)



# mean2=data_DF1.mean("11553")
# print(mean2)

min_value = data_DF1['id_2'].min()
data_DF1.std()


import sklearn.linear_model as lp