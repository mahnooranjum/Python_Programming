from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    content = file.read()
    # print(content)

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    cards = soup.find_all('div', class_ = 'card')

    for i in cards:
        # print(i)
        course = i.h5.text
        price = i.a.text.split(' ')[-1]
        print(f'{course} costs {price}')
