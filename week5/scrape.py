from bs4 import BeautifulSoup, BeautifulStoneSoup
import requests
import csv
# with open("simple.html") as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# #this method finds only the first occurence of the tag
# match = soup.title.text

# #lets use another approach
# match = soup.find('div',class_= 'footer')

# #መዘክዝዘኪንግ
# article = soup.find('div',class_='article')
# match = article.h2.a.text
# #the problem is that it only finds the first occurence, and if the first occurence lacks a it will become none and if you try to obtain text from none it will give an error
# #lets try to find all the articles
# for article in soup.find_all('div',class_='article'):
#     headline = article.h2.a.text
#     print(headline)
#     summary = article.p.text
#     print(summary)
#     print()

# print(match)

csv_file = open('cms_scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name","price","rating","availability"])

source = requests.get('http://books.toscrape.com/').text
soup = BeautifulSoup(source,'lxml')
for article in soup.find_all('article', class_ = 'product_pod'):
    image  = article.a.img['src']
    print("image:",image)
    rating = article.p['class'][1]
    print("rating:",rating)
    title = article.h3.a['title']
    print("title:",title)
    price = article.find('p',class_='price_color').text 
    print("price:",price)
    availability = article.find('p',class_='instock availability').text.strip()
    print("availability:",availability)
    csv_writer.writerow([title,price,rating,availability])
    print()
csv_file.close()






# print(soup.section.article)
# print(soup.prettify())
