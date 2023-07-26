from newsdataapi import NewsDataApiClient
from dotenv import load_dotenv
import os
load_dotenv(".env")

api_key = os.getenv("NEWS_DATA")

# API key authorization, Initialize the client with your API key

api = NewsDataApiClient(apikey=api_key)

# You can pass empty or with request parameters {ex. (country = "us")}

def get_news(query ,category,language, country):
    response = api.news_api(category=category,language=language ,q=query,qInTitle=None, country = country)
    return response

response = get_news(category="business",language="en",query='Bajaj Finance Limited',country="in")
print(response)
