import datetime
import time

from login import Bot

b = Bot()

b.login()

username = input("input username: ")
chat_raw = b.search_chat(username)
chat_url = chat_raw.get_attribute("href")
b.driver.get(chat_url)
time.sleep(1)
id1 = '1'

while True:
    time.sleep(0.5)
    id, text = b.get_last_message(chat_url)
    text = text.replace(f'{datetime.datetime.now().strftime("%H:%M")}', '')
    if id != id1:
        id1 = id
        b.send_message(text, username, chat_url)
