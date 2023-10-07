import pageReader
import csv

#Initiates a tupple list which also works as the file header later on
data_page = [("ID", "Title", "Description", "Body", "Keywords", "Theme", "Link")]
links = []
agrs = []

#Initiates the User Agent, in case of errors try swapping this for another one, you can find them online fairly easily
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/93.0.4577.82 Safari/537.36'}

#Runs the function which collects the aggregators/subsections from cnn's main page
agrs = pageReader.getagregator(agrs, "https://edition.cnn.com")

#Translates to "Finished reading aggregators" ((I am brazillian))
print("Leitura dos agregadores concluida")

#Runs the function which collects the article links from an aggregator
#Runs for every aggregator
for a in agrs:
    links = pageReader.getlinks(links, a)

#Translates to "Finished reading link, current ammount of articles:"
print("Leitura dos links conluida, total de noticias: " + str(len(links)))

#Counts how many links have been read
cnt = 0

#For every link collected runs the function that collects information and links from the article
#Works for new links collected during the loop
while True:
    l2 = links[cnt]
    cnt += 1
    #I set an arbitrary 5000 observations limit but you can take it out if you want and ride this to valhalla
    #In my experience it didn't reach 5000 anyways
    if len(data_page) < 5000 and cnt < len(links):
        print("Progresso: " + str(cnt) + "/" + str(len(links)))
        temp = pageReader.pageread(cnt, data_page, l2, links)
        data_page = temp[0]
        links = temp[1]
    else:
        break

#Translates to "Generating csv file"
print("Gerando arquivo csv")

#Generates the csv file
csv_file = open('news.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

#Writes to the scv file
for p in data_page:
    writer.writerow(p)
