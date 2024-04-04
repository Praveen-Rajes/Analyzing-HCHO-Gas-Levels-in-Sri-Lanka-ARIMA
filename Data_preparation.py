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
