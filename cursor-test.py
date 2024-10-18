# function to import a csv and use pandas and dataframe to read the csv and print the first 5 rows
def import_csv(file_path):
    import pandas as pd
    df = pd.read_csv(file_path)
    print(df.head())

import_csv('data.csv')
# 寫一個function將data.csv裡面的第一行資料算出前三天的差值，並放入第二行
def calculate_diff(df):
    df.iloc[1, 1] = df.iloc[0, 1] - df.iloc[3, 1]
    return df

# function to output a csv to the same file path
def output_csv(df, file_path):
    df.to_csv(file_path, index=False)

output_csv(df, 'data.csv')

