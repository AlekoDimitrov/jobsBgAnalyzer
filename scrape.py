from bs4 import BeautifulSoup
import requests
import pandas as pd


def extract(page, category):
    url = f'https://www.jobs.bg/front_job_search.php?frompage={page}&add_sh=1&categories%5B0%5D=56&domains%5B0%5D={category}&term=#paging'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup


def transform(soup):
    td = soup.findAll('td', {'class': 'offerslistRow'})
    
    for item in td:
        
        try:
            category = item.find('div', {'class', 'card__subtitle mdc-typography mdc-typography--body2'})
            skillsList = []
            
            salary = item.find('b')
            if salary is not None:
                salary = salary.text.strip().replace('до', '-').replace('от', '')
            else:
                salary = ''
            
            skills = item.findAll('img', alt=True)
            for img in skills:
                skills = img['alt']
                skillsList.append(skills)
                
            skillsNotImg = item.findAll('span', {'class': 'skill-not-img'})
            for skill in skillsNotImg:
                skills = skill.text
                skillsList.append(skills)                

            listToStr = ', '.join(skillsList)
            
            pair = {
                'Category:': category.text.strip().replace(';', ','),
                'Skills:': listToStr,
                'Salary:': salary
            }
            pairsList.append(pair)
        except AttributeError:
            category = ''


pairsList = []

page = 0
category = 1

while True:
    if page == 300:
        page = 0
        category += 1
        pairsList = []
    elif category == 29:
        break

    print(f'{page}, {category}')
    c = extract(page, category)
    transform(c)
    page += 15
    df = pd.DataFrame(pairsList)
    df.to_csv(f'dataFolder/data{category}.csv', index=False)