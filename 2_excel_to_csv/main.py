import pandas as pd


excel_file = input('What excel file do you want to convert to csv file? ')
df = pd.read_excel(f'{excel_file}.xlsx')
df.to_csv(f'{excel_file}.csv', index=False)
