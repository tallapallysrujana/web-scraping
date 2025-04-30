import requests
from bs4 import BeautifulSoup
import time

print('Put some skill taht you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://in.talent.com/jobs?l=Hyderabad&id=d616e9f58468').text
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

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)