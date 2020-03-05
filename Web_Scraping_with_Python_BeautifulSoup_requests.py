import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re
import random

#input needed on lines: 11,12,15,24,25,36,37; some inputs are url links and the other inputs are depending on the html code.


file = open('path to where to save the text file of data collection.txt', 'a')
urlBASE = "http://url_base.html"


url = "http://some_url_page_1_in_here.html"
counter = 1   #we'll be using counter the watch the progress of the scraping

while url:
    # loading url in
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # getting content and url
    c = soup.find_all('a')   #< next page link
    t = soup.find_all("table")   # < find all the separate tables

    # writing content in text file:
    for i in t:
        a = i.text
        file.write(re.sub("\n","",a))   #getting rid off unnecessary new lines
        break


    # getting the link for next page:
    for i in c:
        if i.find("img"):
            if i.find(attrs = {"alt": "Next Topic/Section"}):
                next_page_url = i.get('href')
                url = urlBASE + next_page_url  #< next page url
                break

    number = random.randint(1,10)   #generating random times between pages
    time.sleep(number)

    print('Round:', counter)   # print progress during the scraping
    counter += 1

print('finished!')   #feedback when we reach the last page


