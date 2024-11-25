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
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quotes Collection</title>
    <style>
        body {{
            background-image: url('https://img.freepik.com/fotos-kostenlos/ultradetaillierte-nebel-abstrakte-tapete-4_1562-749.jpg?t=st=1732563130~exp=1732566730~hmac=85b5909f71c37b0be3ed65118fb84a743f5d13c7f19160b544f26ad3592c60d5&w=1060');
            background-size: cover;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            color: #333;
        }}
        h1 {{
            text-align: center;
            padding: 20px;
            background: rgba(255, 255, 255, 0.8);
        }}
        table {{
            width: 80%;
            margin: 20px auto;
            border-collapse: collapse;
            background: rgba(255, 255, 255, 0.8);
        }}
        th, td {{
            padding: 10px;
            border: 1px solid #ddd;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        a {{
            color: #ff6f61;
            text-decoration: none;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h1>Quotes Collection</h1>
    <table>
        <tr>
            <th>#</th>
            <th>Quote</th>
            <th>Author</th>
        </tr>
        {''.join([f"<tr><td>{i+1}</td><td>{quote['quote']}</td><td>{quote['author']}</td></tr>" for i, quote in enumerate(data)])}
    </table>
    <p>Источник данных: <a href="https://quotes.toscrape.com/">quotes.toscrape.com</a></p>
</body>
</html>
'''
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("HTML-страница успешно сгенерирована и сохранена в файл index.html.")