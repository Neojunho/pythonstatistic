# f = open('./sample/cc.csv', 'r', encoding='utf-8');
# data = f.read()
# print(data)
# f.close()

import pandas as pd
data = pd.read_csv("./sample/cc.csv")
print(data)