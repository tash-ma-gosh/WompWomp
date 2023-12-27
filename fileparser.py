import csv
import pandas as pd

databaseExcel = "Database.xlsx"

excelReader = pd.read_excel(databaseExcel)
excelReader.to_csv("DatabaseCsv.csv", index = None, header = True)

dataframeObject = pd.DataFrame(pd.read_csv("DatabaseCsv.csv"))

print(dataframeObject)