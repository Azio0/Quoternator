import time

def ReadQuoteMD():
    try:
        with open("utils/file/template.md", 'r') as file:
            text = file.read()

        file.close()

        return text, 200
    
    except Exception as error:
        return f"[ReadQuoteMD] {error}", 500
    
def WriteQuoteMD(quote, author):
    try:
        response, status = ReadQuoteMD()

        if status != 200:
            raise Exception(response)

        text = (
            response.replace("{time_stamp}", time.strftime("%Y-%m-%d %H:%M:%S"))
                .replace("{quote}", quote)
                .replace("{author}", author)
            )

        with open("../QUOTE.md", 'w') as file:
            file.write(text)

        file.close()

        return "QUOTE.md updated successfully.", 200
    
    except Exception as error:
        return f"[WriteQuoteMD] {error}", 500
