import requests
from bs4 import BeautifulSoup


def pageread(idn, data_page, url, links):

    links = getlinks(links, url)

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    metas = soup.find_all('meta')

    theme_element = None
    title_element = None
    description_element = None
    tags_element = None
    start = '<script type="application/ld+json">{"@type":"NewsArticle","@context":"https://schema.org","articleBody":"'
    end = '","articleSection":'

    s = str(soup.find('script', type='application/ld+json'))
    if not s.startswith(start):
        return [data_page, links]

    article_element = (s.split(start))[1].split(end)[0]
    link_element = url

    for m in metas:
        if m.get('name') == 'description':
            description_element = m.get('content')
        if m.get('name') == 'theme':
            theme_element = m.get('content')
        if m.get('property') == 'og:title':
            title_element = m.get('content').split('|', 1)[0]
        if m.get('name') == 'keywords':
            tags_element = m.get('content')

    if theme_element is None or title_element is None:
        return [data_page, links]
    return [data_page + [(idn, title_element, description_element, article_element, tags_element, theme_element, link_element)], links]


def getagregator(agrs, url):

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    links1 = soup.find_all('a')

    for li in links1:
        temp = li.get('href')
        if str(temp).startswith('https://edition.cnn.com/') and str(temp) not in agrs:
            agrs = agrs + [temp]

    return agrs


def getlinks(links, url):

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    links1 = soup.find_all('a')

    for li in links1:
        temp = li.get('href')
        if str(temp).startswith('/2023/') and str('https://edition.cnn.com' + temp) not in links:
            links = links + ['https://edition.cnn.com' + temp]
        else:
            if str(temp).startswith('https://edition.cnn.com/2023/') and str(temp) not in links and '/videos/' not in str(temp) and '/gallery/' not in str(temp):
                links = links + [temp]

    return links
