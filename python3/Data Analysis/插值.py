import pandas as pd
import numpy as np
from scipy.interpolate import lagrange
input_file = 'demo1.xlsx'
output_file = 'demo1_output.xlsx'
data = pd.read_excel(input_file)

def interpolate_lagrange_column(s, n, k=5):
    y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))] #取数
    y = y[y.notnull()] #剔除空值
    return lagrange(y.index, list(y))(n) #插值并返回插值结果

#逐个元素判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data[i][j] = interpolate_lagrange_column(s=data[i], n=j)
data.to_excel(output_file)