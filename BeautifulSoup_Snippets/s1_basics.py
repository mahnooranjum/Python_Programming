from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    content = file.read()
    # print(content)

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    tags = soup.find('h5')
    # print(tags)

    tags = soup.find_all('h5')
    for i in tags:
        print(i.text)
