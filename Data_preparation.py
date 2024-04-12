# Import libraries
#%%
import pandas as pd


# Read the data

df_col_mat_nuw = pd.read_csv('Data Sets\col_mat_nuw_output.csv')
df_kan = pd.read_csv('Data Sets\kan_output.csv')
df_mon_kur_jaf = pd.read_csv('Data Sets\mon_kur_jaf_output.csv')

#%%
# Check the data
print(df_col_mat_nuw.head())
print(df_kan.head())
print(df_mon_kur_jaf.head())

#%%
# Adding Column names
columns = ['HCHO Value','Location','Date','Next Date']
df_col_mat_nuw.columns = columns
df_kan.columns = columns
df_mon_kur_jaf.columns = columns

# %%
print(df_col_mat_nuw.head())
print(df_kan.head())
print(df_mon_kur_jaf.head())
# %%
#check the location values
print(df_col_mat_nuw['Location'].unique())
print(df_kan['Location'].unique())
print(df_mon_kur_jaf['Location'].unique())

# %%
# check the data count for each location

location_counts = {
    'Colombo Proper': 0,
    'Deniyaya, Matara': 0,
    'Nuwara Eliya Proper': 0,
    'Kandy Proper': 0,
    'Bibile, Monaragala': 0,
    'Kurunegala Proper': 0,
    'Jaffna Proper': 0
}

for location in df_col_mat_nuw['Location']:
    if location in location_counts:
        location_counts[location] += 1
for location in df_kan['Location']:
    if location in location_counts:
        location_counts[location] += 1
for location in df_mon_kur_jaf['Location']:
    if location in location_counts:
        location_counts[location] += 1

for i in location_counts:
    print(i, location_counts[i])
# %%
# Create separate dataframes for each location
colombo_df = df_col_mat_nuw[df_col_mat_nuw['Location'] == 'Colombo Proper']
Deniyaya_df = df_col_mat_nuw[df_col_mat_nuw['Location'] == 'Deniyaya, Matara']
Nuwara_Eliya_df = df_col_mat_nuw[df_col_mat_nuw['Location'] == 'Nuwara Eliya Proper']
Kandy_df = df_kan[df_kan['Location'] == 'Kandy Proper']
Bibile_df = df_mon_kur_jaf[df_mon_kur_jaf['Location'] == 'Bibile, Monaragala']
Kurunegala_df = df_mon_kur_jaf[df_mon_kur_jaf['Location'] == 'Kurunegala Proper']
Jaffna_df = df_mon_kur_jaf[df_mon_kur_jaf['Location'] == 'Jaffna Proper']

# Print the dataframe
print(colombo_df)
print(Deniyaya_df)
print(Nuwara_Eliya_df)
print(Kandy_df)
print(Bibile_df)
print(Kurunegala_df)
print(Jaffna_df)

# %%
# Save the dataframes to csv files
colombo_df.to_csv('Data Sets/Colombo.csv')
Deniyaya_df.to_csv('Data Sets/Deniyaya.csv')
Nuwara_Eliya_df.to_csv('Data Sets/Nuwara_Eliya.csv')
Kandy_df.to_csv('Data Sets/Kandy.csv')
Bibile_df.to_csv('Data Sets/Bibile.csv')
Kurunegala_df.to_csv('Data Sets/Kurunegala.csv')
Jaffna_df.to_csv('Data Sets/Jaffna.csv')

# %%
# check for null values
print('Colombo\n',colombo_df.isnull().sum())
print('Deniyaya\n',Deniyaya_df.isnull().sum())
print('Nuwaraeliya\n',Nuwara_Eliya_df.isnull().sum())
print('Kandy\n',Kandy_df.isnull().sum())
print('Bibile\n',Bibile_df.isnull().sum())
print('Kurunegala\n',Kurunegala_df.isnull().sum())
print('Jaffna\n',Jaffna_df.isnull().sum())
# %%
# describe column 'HCHO Value' of each dataframe
print('Colombo\n',colombo_df['HCHO Value'].describe())
print('Deniyaya\n',Deniyaya_df['HCHO Value'].describe())
print('Nuwaraeliya\n',Nuwara_Eliya_df['HCHO Value'].describe())
print('Kandy\n',Kandy_df['HCHO Value'].describe())
print('Bibile\n',Bibile_df['HCHO Value'].describe())
print('Kurunegala\n',Kurunegala_df['HCHO Value'].describe())
print('Jaffna\n',Jaffna_df['HCHO Value'].describe())


# %%
#filling missing values with mean 'HCHO Value' of each dataframe


# %%
# check for null values
print('Colombo\n',colombo_df.isnull().sum())
print('Deniyaya\n',Deniyaya_df.isnull().sum())
print('Nuwaraeliya\n',Nuwara_Eliya_df.isnull().sum())
print('Kandy\n',Kandy_df.isnull().sum())
print('Bibile\n',Bibile_df.isnull().sum())
print('Kurunegala\n',Kurunegala_df.isnull().sum())
print('Jaffna\n',Jaffna_df.isnull().sum())
# %%

#plot the kandy HCHO values
import matplotlib.pyplot as plt
plt.plot(Kandy_df['HCHO Value'])
plt.xlabel('Date')
plt.ylabel('HCHO Value')
plt.title('Kandy HCHO Values')
plt.show()

# %%
print('Kandy\n',Kandy_df.isnull().sum())

# %%
Kandy_df.head()
# %%
#filling missing values with mean 'HCHO Value' of Kandy dataframe

Kandy_df['Date'] = pd.to_datetime(Kandy_df['Date'])

Kandy_df['Filled HCHO values'] = Kandy_df['HCHO Value'].interpolate(method='linear')
# %%
print('Kandy\n',Kandy_df.isnull().sum())
# %%
import matplotlib.pyplot as plt
plt.plot(Kandy_df['Filled HCHO values'])
plt.xlabel('Date')
plt.ylabel('Filled HCHO values')
plt.title('Kandy HCHO Values')
plt.show()
# %%
# stationary test on Kandy data
from statsmodels.tsa.stattools import adfuller
result = adfuller(Kandy_df['Filled HCHO values'])
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
# %%
# creating time series arima model for Kandy data

