import os
from datetime import datetime

class FileName:
    now = datetime.now()# get actual data and time

    #If Windows — replace ":" to  "-"
    if os.name == "nt":  # nt = Windows
        filename = now.strftime("%Y-%m-%d %H-%M-%S.xlsx")
    else:  # Linux / macOS
        filename = now.strftime("%Y-%m-%d %H:%M:%S.xlsx")