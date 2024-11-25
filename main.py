from datetime import date
import requests
from bs4 import BeautifulSoup
import json
url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
data = []
for i, (quote, author) in enumerate(zip(quotes, authors), 1): 
    quote_text = quote.text.strip() 
    author_text = author.text.strip() 
    print(f'{i}. Quote: "{quote_text}"; Author: {author_text};')
with open('data.json', 'w', encoding='utf-8') as f: json.dump(data, f, ensure_ascii=False, indent=4) 
print("Данные успешно сохранены в файл data.json.")