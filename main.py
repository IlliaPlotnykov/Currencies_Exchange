from datetime import datetime
from currencies_classes.request_api import RequestAPI
from currencies_classes.file_writer_excel import FileWriter as FW
from currencies_classes.file_reader import FileReader as FR
from currencies_classes.filename import FileName as FL

FR.get_currency_list() # Get The Currencies

start = datetime(datetime.now().year, datetime.now().month, 1)
end = FL.now #datetime(2025, 5, 31)

R_API = RequestAPI(start,end).get_data() # Collect data for the required period of time

FW(R_API).write_to_excel(FL.filename) # convert the data in excel file