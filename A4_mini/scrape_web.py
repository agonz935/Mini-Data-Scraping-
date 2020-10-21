from bs4 import BeautifulSoup
import requests
import sys

with open('Burtscher.html') as html_file: #Html input file name here, can change
    soup = BeautifulSoup(html_file, 'lxml')

name = soup.find('div', class_='page-heading clearfix').find('h1', class_='heading-title pull-left')
name_txt = name.text
txt = name_txt.strip(" \n,\t")

info = soup.find_all('div', class_='panel-body')
info1 = info[0].text
info2 = info[1].text
info3 = info[2].p.text

wp = soup.find('div', class_='details col-md-9 col-sm-8 col-xs-6').find('a', href=True)

original_stdout = sys.stdout

with open('output.txt', 'w') as f:
    sys.stdout = f
    print("Name: " + txt)
    print("Education: " + info2)
    print("Research Interests: " + info1)
    print("Office: " + info3)
    print("Webpage: " + wp['href'])
    sys.stdout = original_stdout

