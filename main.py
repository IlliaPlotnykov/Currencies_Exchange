from datetime import datetime
from currencies_classes.request_api import RequestAPI
from currencies_classes.file_writer_excel import FileWriter as FW

start = datetime(2025, 5, 1)
end = datetime(2025, 5, 2)

RA = RequestAPI(start,end).get_data()

FileWriter(RA).write_to_excel()
