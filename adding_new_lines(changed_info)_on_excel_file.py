import pandas as pd
import numpy as np

file_name = 'name_of_excel.xlsx'

# Mission
# 1. Find specific information on the 14th column in one excel file
# 2. Change the searched information into the new information
# 3. Add the lines with the changed information to existing excel file
# 4. Save the result as "test1.xlsx"

data = pd.read_excel(file_name)
df = pd.DataFrame(data)
df_array = np.array(df)

condition_list = []
for i in range(len(df_array)):
    if df_array[i][13] == 'Ad2':
        df_array[i][13]='Ci1'

    elif df_array[i][13] == 'Ad3':
          df_array[i][13] = 'Ci2'

    elif df_array[i][13] == 'Ea3':
          df_array[i][13] = 'Cb'

    elif df_array[i][13] == 'Ea6':
          df_array[i][13] = 'Ca1'

    elif df_array[i][13] == 'Ci1':
          df_array[i][13] = 'Ad2'

    elif df_array[i][13] == 'Ci2':
          df_array[i][13] = 'Ad3'


    if df_array[i][13] =='Ci1':
        condition_list.append(df_array[i])

    elif df_array[i][13] == 'Ci2':
          condition_list.append(df_array[i])

    elif df_array[i][13] == 'Cb':
          condition_list.append(df_array[i])

    elif df_array[i][13] == 'Ca1':
          condition_list.append(df_array[i])

    elif df_array[i][13] == 'Ad2':
          condition_list.append(df_array[i])

    elif df_array[i][13] == 'Ad3':
          condition_list.append(df_array[i])


df2 = pd.DataFrame(condition_list)
df2.columns=['column1_sameasdf','column2_sameasdf','column3_sameasdf','column4_sameasdf','column5_sameasdf',
             'column6_sameasdf','column7_sameasdf','column8_sameasdf','column9_sameasdf','column10_sameasdf',
             'column11_sameasdf','column12_sameasdf','column13_sameasdf','column14_sameasdf']

data_combined = pd.concat([df,df2])
data_combined.to_excel('test1.xlsx')
