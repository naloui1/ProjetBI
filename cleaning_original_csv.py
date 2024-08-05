import os
import pandas as pd

directory = './data_brut'

### latin to UTF-8
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        
        with open(file_path, 'r', encoding='latin-1') as infile:
            content = infile.read()
        
        with open(file_path, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
        
        print(f'Converted {filename} to UTF-8 encoding.')

### replacing , by .
files_to_process = ['SIE_2023_anonymise.csv', 'Athanor_caracterisations.csv']

for filename in files_to_process:
    file_path = os.path.join(directory, filename)
    
    with open(file_path, 'r', encoding='utf-8') as infile:
        content = infile.read()
    
    content = content.replace(',', '.')
    
    with open(file_path, 'w', encoding='utf-8') as outfile:
        outfile.write(content)
    
    print(f'Replaced commas with periods in {filename}.')


### duplicates in pk

df1 = pd.read_csv(directory + '/SIMPLICITI_2023_anonymise.csv', sep=";")
df2 = pd.read_csv(directory + '/Referentiel_Athanor_produit.csv', sep=",")

pk1 = df1['IMMAT']
duplicates_pk1 = pk1[pk1.duplicated(keep=False)]

# Output the duplicates
print("Duplicates in SIMPLICITI_2023_anonymise.csv:")
print(duplicates_pk1)

pk2 = df2['PRD_CODE']
duplicates_pk2 = pk2[pk2.duplicated(keep=False)]

# Output the duplicates
print("Duplicates in Referentiel_Athanor_produit.csv:")
print(duplicates_pk2)