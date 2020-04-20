from bs4 import BeautifulSoup
import requests
import os
import pandas as pd           # Import pandas library
import matplotlib.pyplot as plt

URL= 'https://www.city-data.com/coronavirus/'    #downloading the website data 
page= requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results_collapse1 = soup.find(id='collapse1')

state_elems= results_collapse1.find_all('tr')    #scrape and save 
state_data= []
for s_ct, state_row in enumerate(state_elems):
    columns_col= state_row.find_all('td')
    if columns_col:
        state_tag, confirmed_tag, recovered_tag, active_tag, deaths_tag = columns_col
        state_data.append([
            str(state_tag.text),
            int(confirmed_tag.text.replace(',', '')),
            int(deaths_tag.text.replace(',', ''))
        ])
         
df= pd.DataFrame(state_data, columns= ['State', 'Confirmed', 'Deaths'])  # Create the pandas DataFrame 
df.to_csv(os.path.join('data', 'city_covid_data.csv'))

# Visualize 
df.sort_values(by=['Confirmed'], inplace=True, ascending=True)
print(df.head(10))
ax= df.head(25).plot.bar(x= 'State', y={'Confirmed', 'Deaths'}, rot=0)
plt.xticks(rotation=45)
plt.savefig(os.path.join('data', 'least25.pdf'))
plt.show()
