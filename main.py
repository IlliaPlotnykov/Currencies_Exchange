from datetime import datetime
from currencies_classes.request_api import RequestAPI
from currencies_classes.file_writer_excel import FileWriter as FW
from currencies_classes.file_reader import FileReader as FR
import os

FR.get_currency_list() # Отримуємо потрібні валюти

start = datetime(2025, 5, 1)
end = datetime(2025, 5, 31)

R_API = RequestAPI(start,end).get_data() # Отримуємо дані за потрібний проміжок часу

now = datetime.now()# отримуємо поточну дату та час

#якщо Windows — заміняємо ":" на "-"
if os.name == "nt":  # nt = Windows
    filename = now.strftime("%Y-%m-%d %H-%M-%S.xlsx")
else:  # Linux / macOS
    filename = now.strftime("%Y-%m-%d %H:%M:%S.xlsx")

FW(R_API).write_to_excel(filename) # Дані конвертуємо у ексель файл
