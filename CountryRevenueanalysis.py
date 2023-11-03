
################# COUNTRY GENERATING THE HIGHEST REVENUE #######
import numpy as np
import pandas as pd
largestcomp = pd.read_html('https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue')
Final_table = largestcomp[0]


# --------------------------------------------------------------------
#convert to csv for the final df and download in the computer
Final_table.to_csv('Final_data.csv', index = False)

# --------------------------------------------------------------------
#read into the new file
New_data = pd.read_csv('Final_data.csv') 
New_data.head(5)
print(New_data.dtypes)

# --------------------------------------------------------------------


#convert columns to integers
##first column
New_data['Revenue USD millions'] = New_data['Revenue USD millions'].str.replace('$', '').str.replace(',', '').astype(int)

##second column
New_data['Profit USD millions2'] = New_data['Profit USD millions2'].str.replace('[,() ]', '', regex=True)
New_data['Profit USD millions2'] = pd.to_numeric(New_data['Profit USD millions2'], errors='coerce').fillna(0).astype(int)
New_data


# --------------------------------------------------------------------

#delete a column
del New_data['Ref.']


# --------------------------------------------------------------------
#check countries that are listed
countries = New_data['Headquarters[note 1]'].unique()
countries

# --------------------------------------------------------------------

#check which country has the most revenue
##aligned header rows 
Countrydata = New_data.groupby('Headquarters[note 1]', as_index=False).sum()
# Countrydata
Countrydata.drop(columns=['Rank','Name', 'Industry', 'Employees'], inplace=True)
Countrydata

#rename a specific column
Countrydata = Countrydata.rename(columns={'Headquarters[note 1]': 'Countries'})
Countrydata


# --------------------------------------------------------------------
# Sort the DataFrame by 'Revenue USD millions' in descending order
Countrydata = Countrydata.sort_values(by='Revenue USD millions', ascending=False)

##graph it
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
Countrydata.plot(x='Countries', y='Revenue USD millions', kind='bar')
plt.title('Revenue USD millions by Headquarters')
plt.xlabel('Countries')
plt.ylabel('Revenue USD millions')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------


#Check US Company that has the most Revenue.
New_data
US = New_data[New_data['Headquarters[note 1]'] == 'United States']

#plot US Company
US.plot(x= 'Name', y = 'Revenue USD millions', kind = 'bar')
plt.title('Revenue USD millions by USA Headquarters')
plt.xlabel('Company')
plt.ylabel('Revenue USD millions')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------

#Check for Saudi Arabia
SaudiArabia = New_data[New_data['Headquarters[note 1]'] == 'Saudi Arabia']
SaudiArabia

# --------------------------------------------------------------------

#Check for China
China = New_data[New_data['Headquarters[note 1]'] == 'China']
China
China.plot(x= 'Name', y = 'Revenue USD millions', kind = 'bar')
plt.title('Revenue USD millions by USA Headquarters')
plt.xlabel('Company')
plt.ylabel('Revenue USD millions')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------

#Check for Switzerland
Switzerland = New_data[New_data['Headquarters[note 1]'] == 'Switzerland']
Switzerland

# --------------------------------------------------------------------

#Check for United Kingdom
United_Kingdom = New_data[New_data['Headquarters[note 1]'] == 'United Kingdom']
United_Kingdom

# --------------------------------------------------------------------

#Check for Singapore
Singapore = New_data[New_data['Headquarters[note 1]'] == 'Singapore']
Singapore

# --------------------------------------------------------------------

#Check for Germany
Germany = New_data[New_data['Headquarters[note 1]'] == 'Germany']
Germany.plot(x= 'Name', y = 'Revenue USD millions', kind = 'bar')
plt.title('Revenue USD millions by Germany Headquarters')
plt.xlabel('Company')
plt.ylabel('Revenue USD millions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# --------------------------------------------------------------------

#Check for Japan
Japan = New_data[New_data['Headquarters[note 1]'] == 'Japan']
Japan

# --------------------------------------------------------------------

#Check for France
France = New_data[New_data['Headquarters[note 1]'] == 'France']
France

# --------------------------------------------------------------------

#Check for South Korea
SouthKorea = New_data[New_data['Headquarters[note 1]'] == 'South Korea']
SouthKorea


# --------------------------------------------------------------------

#Check for Taiwan
Taiwan = New_data[New_data['Headquarters[note 1]'] == 'Taiwan']
Taiwan


# --------------------------------------------------------------------

#Check for Netherlands
Netherlands = New_data[New_data['Headquarters[note 1]'] == 'Netherlands']
Netherlands


# --------------------------------------------------------------------

#Check for Russia
Russia = New_data[New_data['Headquarters[note 1]'] == 'Russia']
Russia

# --------------------------------------------------------------------
