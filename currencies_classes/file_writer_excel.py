class FileWriter:
    def __init__(self,dataframe ):
        self.df = dataframe

    def write_to_excel(self,filename):
        try:
            self.df.to_excel(filename, index=False)
            print(f"It was saved in: {filename}")
        except Exception as e:
            print(f"Error {e}")