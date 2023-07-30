#1.Развернуть у себя на компьютере / виртуальной машине / хостинге MongoDB и реализовать функцию,
# которая будет добавлять только новые вакансии в вашу базу.

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

def parser_hh(world):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    params = {'page': 1}
    url = "https://hh.ru"
    vacancy_date = []
    session = requests.Session()
    response = session.get('https://hh.ru/search/vacancy?text=' + world + '&from=suggest_post', headers=headers, params=params)
    n = 1
    print('Количество новых вакансий: ')
    m = 0
    while True:
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all('div', {'class': 'vacancy-serp-item-body__main-info'})
        #Ограничения связанные с n, а именно, следующие две строки нужно закоментироватьб ввела из-за тормозов компа
        if n>4:
            break
        #
        for article in articles:
            info = article.find('a', {'class': 'serp-item__title'})
            vacname = info.text
            link = article.find('a').get('href')
            salary = article.find('span', {'class': 'bloko-header-section-2'})
            is_check_sarary = ''
            salary_currency = None
            salary_max = None
            salary_min = None
            vtmp1 = ''
            vtmp2 = ''
            v = ''
            if not salary:
                pass
            else:
                is_check_sarary = salary.text.replace(u'\u202f', u' ')
                v = is_check_sarary[is_check_sarary.rfind(' ') + 1:]
                is_check_sarary = is_check_sarary.replace(v, '')
                is_check_sarary = is_check_sarary.replace(' ', '')
                k = 0
                for i in is_check_sarary:
                    if i.isdigit() and k == 0:
                        vtmp1 = vtmp1 + i
                    elif i == ' ' and k == 0:
                        pass
                    elif vtmp1 != '':
                        k = 1
                    else:
                        pass
                k = 0
                for i in reversed(is_check_sarary):
                    if i.isdigit() and k == 0:
                        vtmp2 = i + vtmp2
                    elif i == ' ' and k == 0:
                        pass
                    elif vtmp2 != '':
                        k = 1
                    else:
                        pass

                if 'до' in is_check_sarary:
                    if vtmp2 !='':
                        salary_max = int(vtmp2)
                elif 'от' in is_check_sarary:
                    if vtmp1 !='':
                        salary_min = int(vtmp1)
                elif '–' in is_check_sarary:
                    if vtmp1 !='':
                        salary_min = int(vtmp1)
                    if vtmp2 !='':
                        salary_max = int(vtmp2)
                else:
                    if vtmp1 !='':
                        salary_currency = int(vtmp1)
                    #vacancy_date.append([vacname, link, salary_min, salary_currency, salary_max, v])

                persons = db.persons

            if persons.find_one({'_id': link}):
                pass
            else:
                persons.insert_one({'vacancy': vacname, '_id': link, 'salary_min': salary_min, 'salary_currency': salary_currency, 'salary_max': salary_max, 'v': v,'key':world})
                m=m+1

        n = n + 1
        params['page'] += 1
        response = session.get('https://hh.ru/search/vacancy?text=' + world + '&from=suggest_post', headers=headers, params=params)
        #for doc in persons.find({}):
            #pprint(doc)
    print('m',m)
    return m

m = 0
client = MongoClient('127.0.0.1', 27017)
db = client['users']
world = 'Python'
print(parser_hh(world))
client.close()
