from datetime import datetime
from currencies_classes.request_api import RequestAPI
from file_reader import FileReader as FR

start = datetime(2025, 5, 1)
end = datetime(2025, 5, 3)

# requester = RequestAPI(start, end)
# requester.get_data()

RequestAPI(start,end).get_data()
