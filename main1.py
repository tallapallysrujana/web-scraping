import requests
from bs4 import BeautifulSoup

print('Put some skill taht you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

html_text = requests.get('https://in.talent.com/jobs?l=Hyderabad&id=d616e9f58468').text
#print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_='card-content')
for job in jobs:
    job_title = job.find('h2', class_='card__title').text
    job_location = job.find('span', class_='card__location').text
    job_company = job.find('span', class_='card__company').text
    job_salary = job.find('span', class_='card__salary').text
    print(f'Job Title: {job_title.strip()}')
    print(f'Job Location: {job_location.strip()}')
    print(f'Job Company: {job_company.strip()}')
    print(f'Job Salary: {job_salary.strip()}')
    print()

job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date=job.find('span', class_='sim-posted').span.text
    if '4 days' in published_date: 
        company_name=job.find('span', class_='company-name').text.replace(' ','')
        skills=job.find('span', class_='srp-skills').text.replace(' ','')
        more_info=job.header.h2.a['href']
        if unfamiliar_skill not in skills:

            print(f"Company name: {company_name.strip()}")
            print(f"Skills: {skills.strip()}")
            print(f"Published Date: {published_date.strip()}")
            print(f"More Info: {more_info}")
    #print(published_date)
#print(company_name)
       # print(f'''
        #    Company Name: {company_name}
         #   Required Skills: {skills}
         #   Published Date: {published_date}
          #  ''' )
       # print('')



