from datetime import datetime
from currencies_classes.request_api import RequestAPI
from currencies_classes.file_writer_excel import FileWriter as FW
from currencies_classes.file_reader import FileReader as FR
from currencies_classes.filename import FileName as FL

FR.get_currency_list() # Отримуємо потрібні валюти

start = datetime(datetime.now().year, datetime.now().month, 1)
end = FL.now #datetime(2025, 5, 31)

R_API = RequestAPI(start,end).get_data() # Отримуємо дані за потрібний проміжок часу

FW(R_API).write_to_excel(FL.filename) # Дані конвертуємо у ексель файл