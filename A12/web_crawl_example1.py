from bs4 import BeautifulSoup
import requests

URL= 'https://www.monster.com/jobs/search/?q=Programmer&where=Tennessee'
page= requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')     #print(results_collapse1.prettify())

job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:

    #each job element is a new beautifulsoup object
    #You can use the same methods on it as you did before
     
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print('----------------')
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()
