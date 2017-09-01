import pandas as pd
import os

PATH = os.path.abspath('C:/Users/Офис/Desktop/result.xlsx')

df = pd.io.excel.read_excel(open(PATH), sheetname=0)
