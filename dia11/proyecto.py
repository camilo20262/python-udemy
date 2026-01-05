import bs4 
import requests 

url_base=  'https://books.toscrape.com/catalogue/category/books_1/page-{}.html'

for n in range(1,11):
    print(url_base.format(n))

