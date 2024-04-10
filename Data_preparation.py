# Import libraries
#%%
import pandas as pd


# Read the data

df = pd.read_csv('Data Sets\col_mat_nuw_output.csv')

df.head()

#%%
# Adding Column names
df.columns = ['HCHO Value','Location','Date','Next Date']

# %%
df.head()
# %%
print(df['Location'].unique())

# %%
c = 0
d = 0
n = 0

for i in df['Location']:
    if i == 'Colombo Proper':
        c += 1
    if i == 'Deniyaya, Matara':
        d += 1
    if i == 'Nuwara Eliya Proper':
        n += 1


    

print("c" ,c)
print("d" ,d)
print("n" ,n)
# %%
# Create separate dataframes for each location
colombo_df = df[df['Location'] == 'Colombo Proper']
Deniyaya_df = df[df['Location'] == 'Deniyaya, Matara']
Nuwara_Eliya_df = df[df['Location'] == 'Nuwara Eliya Proper']

# Print the dataframe
print(colombo_df)
print(Deniyaya_df)
print(Nuwara_Eliya_df)

# %%
# Save the dataframes to csv files
colombo_df.to_csv('Data Sets/Colombo.csv')
Deniyaya_df.to_csv('Data Sets/Deniyaya.csv')
Nuwara_Eliya_df.to_csv('Data Sets/Nuwara_Eliya.csv')

# %%
