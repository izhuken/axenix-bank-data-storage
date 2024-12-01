import pandas as pd


class ParsingDatabase():

    def __init__(self, file):
        self.file = file
        self.format_file = file.split(".")[-1]

    async def parsing_database(self):
        if self.format_file == "csv":
            df = pd.read_csv(self.file)
        else:
            df = pd.read_excel(self.file)
        
        print(df)
        pass