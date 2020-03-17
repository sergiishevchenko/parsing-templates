from bs4 import BeautifulSoup
import re

# .find()
# .find_all()

# .parent
# .find_parent()

# .parents
# .find_parents()

# .find_next_sibling()
# .find_previous_sibling()

def get_copywriter(tag):
    whois = tag.find('div', id="whois").text.strip()
    if "Copywriter" in whois:
        return tag
    return None


def get_salary(s):
    pattern = r'\d{1,9}'
    # salary = re.findall(pattern, s)[0]
    salary = re.search(pattern, s).group()
    print(salary)

def main():
    file = open('index.html').read()
    soup = BeautifulSoup(file, 'lxml')
    # row = soup.find_all('div', {'data-set': 'salary'})
    # alena = soup.find('div', text="Alena").parent
    # print(alena)
    # copywriters = []

    # persons = soup.find_all('div', class_='row')
    # for person in persons:
    #     cw = get_copywriter(person)
    #     if cw:
    #         copywriters.append(cw)
    # print(copywriters)

    salary = soup.find_all('div', {'data-set': 'salary'})
    for i in salary:
        get_salary(i.text)


if __name__ == '__main__':
    main()
