from utils.requests.worker import *
from utils.config.worker import *
from utils.file.worker import *

def Main():
    try:
        quote, author, status = GetQuote()

        if status != 200:
            raise Exception(quote)

        response, status = WriteQuoteMD(quote, author)

        if status != 200:
            raise Exception(response)

        print(response, 200)

    except Exception as error:
        print(f"[Main] Error: {error}", 500)

if __name__ == "__main__":
    Main()