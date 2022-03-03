import requests
import json


companies = requests.get('https://api.hh.ru/vacancies/',data={'text':'Django'})
company_name = companies.json()['items'][0]['employer']['name']
print(company_name)
company_info = requests.get('https://api.hh.ru/employers/',data={'text':company_name}).json()
company_url_vacancies = company_info['items'][0]['vacancies_url']
print(company_url_vacancies)
company_all_vacancies = requests.get(company_url_vacancies).json()
for i in range(len(company_all_vacancies['items'])):
    print(company_all_vacancies['items'][i]['name'])
