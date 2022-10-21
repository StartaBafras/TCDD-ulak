import requests
TOKEN = ""
chat_id = ""
#message = "hello from your telegram bot"

def gönder(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json()) # this sends the message