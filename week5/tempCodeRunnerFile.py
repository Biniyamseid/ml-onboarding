source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source,'lxml')
print(soup.prettify())