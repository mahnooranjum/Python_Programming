from bs4 import BeautifulSoup
import requests


html = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# print(html)


soup = BeautifulSoup(html, 'lxml')
jobs = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx")



for job in jobs:
    url = job.header.h2.a['href']
    company = job.find('h3', class_ = 'joblist-comp-name').text

    skills  = job.find('span', class_ = "srp-skills").text
    
    posted  = job.find('span', class_ = "sim-posted").span.text

    if ('Posted few days ago' in posted):
        print(f'Company: {company.strip()}')
        print(f'Skills: {skills.strip()}')
        print(f'Posted: {posted}')

# for i in jobs:
#     print(i.text)