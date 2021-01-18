import requests
import bs4
import pandas as pd
b_url="https://www.worldometers.info/coronavirus/country/"
coun=input("Enter your country name")
coun=coun.lower()
url=b_url+coun+"/"

resu=requests.get(url)

soup=bs4.BeautifulSoup(resu.text,"lxml")

cases=soup.find_all("div",class_ = "maincounter-number")
#print(cases)

#storing the data
info=[]
for i in cases:
    span=i.find("span")
    info.append(span.string)

"""death_rate=str((int(info[1])/int(info[0]))*100)
recover_rate=str((int(info[2])/int(info[0]))*100)

info.append(death_rate)
info.append(recover_rate)"""

df=pd.DataFrame({'Coronavirus':info})
df.index=['TotalCases','Deaths','Recovered']

df.to_csv('Corona_Data.csv')

exit()