import pageReader
import csv

data_page = [("ID", "Title", "Description", "Body", "Keywords", "Theme", "Link")]
links = []
agrs = []

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/93.0.4577.82 Safari/537.36'}

agrs = pageReader.getagregator(agrs, "https://edition.cnn.com")

print("Leitura dos agregadores concluida")

for a in agrs:
    links = pageReader.getlinks(links, a)

print("Leitura dos links conluida, total de noticias: " + str(len(links)))

cnt = 0

while True:
    l2 = links[cnt]
    cnt += 1
    if len(data_page) < 5000 and cnt < len(links):
        print("Progresso: " + str(cnt) + "/" + str(len(links)))
        temp = pageReader.pageread(cnt, data_page, l2, links)
        data_page = temp[0]
        links = temp[1]
    else:
        break

print("Gerando arquivo csv")

csv_file = open('news.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

for p in data_page:
    writer.writerow(p)
