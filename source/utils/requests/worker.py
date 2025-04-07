import requests
from utils.config.worker import *

def GetQuote():
    try:
        url = ConfigParser('quoteSource', 'url')
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            quote = data['quote']
            author = data['author']

            return quote, author, 200
        
        else:
            raise Exception(response.text)
        
    except Exception as error:
        return f"[GetQuote] Error: {error}", 500
