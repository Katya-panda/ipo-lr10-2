import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
for i, (quote, author) in enumerate(zip(quotes, authors), 1): 
    quote_text = quote.text.strip() 
    author_text = author.text.strip() 
    print(f'{i}. Quote: "{quote_text}"; Author: {author_text};')