from datetime import datetime
from currencies_classes.request_api import RequestAPI
from currencies_classes.file_writer_excel import FileWriter as FW

start = datetime(2025, 5, 1)
end = datetime(2025, 5, 2)

R_API = RequestAPI(start,end).get_data()

FW(R_API).write_to_excel('may_2025.xlsx')
