import pandas as pd

input_df = pd.read_excel('input.xlsx')

input_df['Total'] = input_df['Quantity'] + input_df['Price']

# Create a new xlsx file instead of mutating the input.xlsx file
input_df.to_excel('totaled_input.xlsx', index=False)
