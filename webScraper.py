from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

def save(list):
    file_name="my_file.csv"

    with open(file_name,'a') as file_csv:
        csv_file=csv.writer(file_csv)
        csv_file.writerow(list)
    #file_csv.close()


  
def find(web,tag):
    if tag=='a':
        my_list={}
        h1_tags=web.find_all(tag,href=True)
        for x in range(0,len(h1_tags)):
            try :
               my_list[x]=[tag,h1_tags[x].text,h1_tags[x]['href']]
               save(my_list[x])
            except:
                continue
    else:
        my_list={}
        h1_tags=web.find_all(tag)
        for x in range(0,len(h1_tags)):
            try:
                my_list[x]=[tag,h1_tags[x].text,"none"]
                save(my_list[x])
            except:
                continue
    

    print(my_list)
    

url = "https://en.wikipedia.org/wiki/Shawn_Mendes#bodyContent"
req=requests.get(url)
web=BeautifulSoup(req.content,"html.parser")
save(["Tags","Text","link"])
find(web,'h1')
find(web,'h2')
find(web,'h3')
find(web,'h4')
find(web,'h5')
find(web,'h6')
find(web,'p')
find(web,'i')
find(web,'a')








