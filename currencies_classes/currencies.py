class Currencies:
    def __init__(self):
        self.currencies = {}

    def display_info(self):
        return self.currencies

    def add_curr(self,code,rate):
        self.currencies[code] = rate

    def display_curr(self):
        for code,rate in self.currencies.items():
            print(f'{code}: {rate}')


curr1 = Currencies()
curr1.add_curr('USD',41)
curr1.display_curr()

