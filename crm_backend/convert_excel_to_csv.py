import pandas as pd

# Read the excel file
input_file = '/app/crm_backend/employ.xlsx'
output_file = '/app/crm_backend/employ.csv'

# Read the excel file
df = pd.read_excel(input_file)

# Save the dataframe to a csv file
df.to_csv(output_file, index=False)

print(f"Converted {input_file} to {output_file}")