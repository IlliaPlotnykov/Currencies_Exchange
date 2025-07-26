class Currencies:
    def __init__(self):
        self.currencies = []

    def display_info(self):
        return self.currencies

    def add_curr(self,code):
        self.currencies.append(code)

    def display_curr(self):
        for code in self.currencies:
            print(f'{code}')
