from bs4 import BeautifulSoup
import requests
import csv
import json
url = "https://www.fcbarcelona.com/en/football/first-team/players/4974/lionel-messi"
r = requests.get(url).text
soup = BeautifulSoup(r,"html.parser")
filejson = open('messitruphy.json', 'w',encoding='utf8')
filejson.write('[\n')
filecsv = open('messi1_truphy.csv', 'w', encoding='utf8')
data = {}
csv_data = ['type','title','year']
writer = csv.DictWriter(filecsv, fieldnames=csv_data)
anchors = soup.findAll('div',class_="player-honour")

writer.writeheader()
for anchor in anchors:
  type_ = anchor.find('div',class_="player-honour__type").text
  title = anchor.find('div',class_="player-honour__title").text
  year = anchor.find('div',class_="player-honour__dates").text
  year_= year.replace('\n','').replace("                                     ","")
  year__= year_.replace("                             ","").strip().split('•')
  writer.writerow({'type':type_,'title':title,'year':year__})
  data['type'] = type_
  data['title'] = title
  data['year'] = year__
  json_data = json.dumps(data, ensure_ascii=False)
  filejson.write(json_data)
  filejson.write(",\n")
filejson.write('\n]')
filejson.close()
filecsv.close()
