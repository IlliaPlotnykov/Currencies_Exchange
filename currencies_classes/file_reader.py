import pandas as pd

class FileReader:
    @staticmethod
    def get_currency_list(): #Створюємо лист валют з ексель файлу
        df = pd.read_excel('D:\\Programs\\all_python_projects\\Сurrency_Exchange\\config\\list_currencies.xlsx')
        return df['currencies'].tolist()


