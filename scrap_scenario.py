import bs4
from bs4 import BeautifulSoup
import requests

output_list = []

def scraping(webpage):
    response = requests.get(webpage)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup_content = soup.findAll('div', attrs={'class':'grid-inner col-inner clearfix'})
    
    for x in range(len(soup_content)):
        
        #print(soup_content[x].find('a')['href'])
        link = soup_content[x].find('a')['href']
        
        #print(soup_content[x].find('span', attrs={'class':'field-content'}).text)
        upload_date = soup_content[x].find('span', attrs={'class':'field-content'}).text
        
        if soup_content[x].findAll('div', attrs={'class':'field-content'})[1].text != '':
            #print(soup_content[x].findAll('div', attrs={'class':'field-content'})[1].text)
            tag = soup_content[x].findAll('div', attrs={'class':'field-content'})[1].text
        else:
            #print('N/A')
            tag = 'N/A'
           
        #print(soup_content[x].findAll('span', attrs={'class':'field-content'})[1].text)
        title = soup_content[x].findAll('span', attrs={'class':'field-content'})[1].text
        
        news_info = {
            'link':link,
            'upload_date': upload_date,
            'tag': tag,
            'title': title
        }
        
        output_list.append(news_info)
    
    return output_list

#output = scraping('https://www.theedgemarkets.com/categories/corporate')
#print(output)