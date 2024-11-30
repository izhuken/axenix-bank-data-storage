
import os

import pandas as pd

from .s3 import BaseFileService


class BuilderReportService():
    s3_service = BaseFileService()

    def __init__(self, report_name, values, format_report, request):
        self.report_name = report_name
        self.values = values
        self.format_report = format_report
        self.request = request
    
    async def create_file(self):
        insert_data = []
        columns = []
        for value in self.values:
            new_value = []
            for keys, item in value.items():
                if keys == "field_name":
                    continue
                new_value.append(item)
                columns.append(keys)
            insert_data.append(new_value)
        print(columns)
        df = pd.DataFrame(insert_data, columns=list(columns))

        df.to_excel(f"{self.report_name}.xlsx", sheet_name="sheet1")
        if self.format_report == "csv":
            df.to_csv(f"{self.report_name}.csv")
            with open(f"{self.report_name}.csv", "rb") as f:
                file_path = await self.s3_service.upload_file_to_s3_for_builder(f"{self.report_name}.csv", f, self.request)
                os.remove(f"{self.report_name}.csv")
        else:
            with open(f"{self.report_name}.xlsx", "rb") as f:
                file_path = await self.s3_service.upload_file_to_s3_for_builder(f"{self.report_name}.xlsx", f, self.request)
                os.remove(f"{self.report_name}.xlsx")
        return file_path


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