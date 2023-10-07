import requests
from bs4 import BeautifulSoup

#Defines the function that collect information from an article
def pageread(idn, data_page, url, links):

    #Collects more article links
    links = getlinks(links, url)

    #Requests the html content
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    #The relevant information is stored in <meta> fields in the html
    metas = soup.find_all('meta')

    #Initiates the variables that will store the information
    theme_element = None
    title_element = None
    description_element = None
    tags_element = None
    #Initiates a string that is used when collecting the article body
    start = '<script type="application/ld+json">{"@type":"NewsArticle","@context":"https://schema.org","articleBody":"'
    end = '","articleSection":'

    #Collects <script> fields and checks if they are valid
    #If not valid the function returns with no changes
    s = str(soup.find('script', type='application/ld+json'))
    if not s.startswith(start):
        return [data_page, links]

    #If valid the article body is stored
    article_element = (s.split(start))[1].split(end)[0]
    link_element = url

    #Collects the information from the respective <meta> fields
    for m in metas:
        if m.get('name') == 'description':
            description_element = m.get('content')
        if m.get('name') == 'theme':
            theme_element = m.get('content')
        if m.get('property') == 'og:title':
            title_element = m.get('content').split('|', 1)[0]
        if m.get('name') == 'keywords':
            tags_element = m.get('content')

    #final check if the data collect is valid
    if theme_element is None or title_element is None:
        return [data_page, links]
    return [data_page + [(idn, title_element, description_element, article_element, tags_element, theme_element, link_element)], links]

#Defines the function that collects aggregators from cnn's main page
def getagregator(agrs, url):

    #requests the html content
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    #links are stored in <a> fields
    links1 = soup.find_all('a')

    #For every <a> field verifies if it has a link and if it is valid
    for li in links1:
        temp = li.get('href')
        if str(temp).startswith('https://edition.cnn.com/') and str(temp) not in agrs:
            agrs = agrs + [temp]

    #returns the aggregator links
    return agrs

#Defines the function that collects article links from other articles or aggregators
def getlinks(links, url):

    #Same as the above
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    links1 = soup.find_all('a')

    #Also same as the above, although links are stored differently in articles and in aggregators
    for li in links1:
        temp = li.get('href')
        #For aggregators
        if str(temp).startswith('/2023/') and str('https://edition.cnn.com' + temp) not in links:
            links = links + ['https://edition.cnn.com' + temp]
        #For articles
        #Also checks if it leads to "gallery" or "video" tipe articles, which are invalid as the have no body
        #if so, it does not store them
        else:
            if str(temp).startswith('https://edition.cnn.com/2023/') and str(temp) not in links and '/videos/' not in str(temp) and '/gallery/' not in str(temp):
                links = links + [temp]

    return links
