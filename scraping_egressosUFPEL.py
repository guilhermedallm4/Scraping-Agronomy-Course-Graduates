from bs4 import BeautifulSoup
import requests
import pandas as pd 
#!/usr/bin/python
# -*- coding: utf-8 -*-


response = requests.get('https://dctaufpel.com.br/ppgcta/nossa-equipe/egressos')

content = response.content

beautiful = BeautifulSoup(content, 'html.parser')

#print(beautiful.prettify)
name_student = beautiful.findAll('td', attrs={'class': 'nicdark_padding_20 td1'})
email_information = beautiful.findAll('td', attrs={'class': 'nicdark_padding_20 td4'})
graduating = beautiful.findAll('td', attrs={'class': 'nicdark_padding_20 td3'})


def main():
    text_name = [] 
    text_graduating = []
    text_email = []
    #create the archive for save information takem from scraping
    with open('prospect.csv', 'a', encoding="UTF-8") as columns:
        columns.write(('"nome"') + ',')
        columns.write(('"graduação"') + ',')
        columns.write(('"email"') + '\n')
    
    #response for name of the student
    for name in name_student:
        text_name.append(name.text)
        
    #response for states graduating the student
    for graduating_information in graduating:
        formation = graduating_information.find('p').text
        text_graduating.append(formation)
        
    #response for get email contact the student
    for information in email_information:
        email = information.find('p').text
        text_email.append(email.replace(' ',''))

    saveForFile(text_name, text_graduating, text_email)
    
    
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
                email_archive.write(auxEmail + '\n')
    
    registerAjusted() 
    
    
def registerAjusted():
    df = pd.read_csv('prospect.csv',encoding='utf-8', delimiter=',')
    df = df.drop_duplicates()
    print(df)    
    #print(text_name[0])
    #print(text_graduating.('Mestrado'))
    #print(text_email[0])


   
main()

 