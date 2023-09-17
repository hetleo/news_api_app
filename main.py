import requests

api_key = "335a80ec984e4986b3fccdd0c82e21cf"
url = 'https://newsapi.org/v2/everything?q=("public library" AND vancouver)&from=2023-08-17&sortBy=publishedAt&apiKey=335a80ec984e4986b3fccdd0c82e21cf'

# Make request
request = requests.get(url)

# Make a dict with data
content = request.json()

# Access the article title and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
    print("- - - - -")