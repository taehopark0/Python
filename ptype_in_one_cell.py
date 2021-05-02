import pandas as pd
import numpy as np

file_name= "/Users/taehopark/PycharmProjects/dalchaebi/달채비데이터폴더/Python/Python/Product_pad_large_201215.xlsx"


data = pd.read_excel(file_name, sheet_name='대형최종.1210')
df = pd.DataFrame(data)
df_array = np.array(df)

# excel 행 갯수 세기

line = len(np.array(df.loc[:,'id']))
print(line)

# ID 값 세기

attr_list = np.array(df.loc[:,'id'])
attr_number = pd.value_counts(attr_list)
attr_order = attr_number.index.sort_values()
print(len(attr_order))

# 동일 id의 ptype만 추출
new_list = []
final_list = []

for i in range(line):
    for j in range(len(attr_order)):
        if df_array[i][0] == j+1:
            new_list.append(df_array[i][7])
            final_list.append(list(new_list))
    print(len(final_list))









