import os
from datetime import datetime

class FileName:
    now = datetime.now()# отримуємо поточну дату та час

    #якщо Windows — заміняємо ":" на "-"
    if os.name == "nt":  # nt = Windows
        filename = now.strftime("%Y-%m-%d %H-%M-%S.xlsx")
    else:  # Linux / macOS
        filename = now.strftime("%Y-%m-%d %H:%M:%S.xlsx")