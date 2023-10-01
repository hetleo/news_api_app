import requests
from functions import send_email

api_key = "335a80ec984e4986b3fccdd0c82e21cf"
url = f'https://newsapi.org/v2/everything?q=iota and wallet&from=2023-09-10&apiKey={api_key}'

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()    

# Access the article titles and description
body = ""
for article in content["articles"]:
    title = article["title"]
    desc = article["description"]
    article_url = article["url"]
    body = body + f"{title.upper()} \n{desc} \n{article_url} \n\n"

print(body)
# body = body.encode("utf-8")
# send_email(message=body)