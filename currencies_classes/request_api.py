import requests
import pandas as pd
from datetime import timedelta
import sys
sys.path.append("_")
from config.global_config import *
from currencies_classes.file_reader import FileReader as FR

class RequestAPI:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.all_data = []

    def get_data(self):
        current_date = self.start_date
        while current_date <= self.end_date:
            date_str = current_date.strftime('%Y%m%d')
            for curr in FR.get_currency_list():
                url = f"{str(URL)}{str(curr)}&date={date_str}&json"
                response = requests.get(url=url)
                if response.status_code == 200:
                    day_data = response.json()
                    if day_data:
                        self.all_data.append(day_data[0])
                else:
                    print(f"Ошибка запроса на {date_str}: {response.status_code}")
            current_date += timedelta(days=1)

        df = pd.DataFrame(self.all_data)
        return df
        print(df)