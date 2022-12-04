from bs4 import BeautifulSoup
import requests
import pandas as pd 
#!/usr/bin/python
# -*- coding: utf-8 -*-

name = []
specialist = []
email = []
counter = 0

def main(url, counter):
    response = requests.get(url)
    content = response.content
    beautiful = BeautifulSoup(content, 'html.parser')
    table_students = beautiful.find('div', attrs={'class': 'box_1 nicdark_container nicdark_clearfix profiles'})
    information = table_students.findAll('div', attrs={'class': 'grid grid_3'})
    for getInformation in information:
        name.append(getInformation.find('h2').text)
        specialist.append(getInformation.find('h3').text)
        email.append(getInformation.find('h5').text)
    counter = counter + 1
    if(counter == 1):
        main('https://dctaufpel.com.br/ppgcta/nossa-equipe/pos-doutorandos', counter)
    elif(counter == 2):
        main('https://dctaufpel.com.br/ppgcta/nossa-equipe/discentes', counter)
    else:
        saveForFile(name, specialist, email)
        return 0


def saveForFile(text_name, text_graduating, text_email):
    for i in range(len(text_name)):  
            with open('prospect.csv', 'a', encoding="UTF-8") as name_archive:
                auxName = text_name[i]
                name_archive.write(auxName + ',')
            with open('prospect.csv', 'a', encoding="UTF-8") as graduating_archive:
                auxGraduating = text_graduating[i]
                graduating_archive.write(auxGraduating + ',')
            with open('prospect.csv', 'a', encoding="UTF-8") as email_archive:
                auxEmail = text_email[i]
                if(i != len(text_name)):
                    email_archive.write(auxEmail + '\n')
                else:
                    email_archive.write(auxEmail)
    return 0
    
main('https://dctaufpel.com.br/ppgcta/nossa-equipe/docentes', counter)