import pandas as pd
import os

CWD = os.path.dirname(os.path.realpath(__file__))

calls = pd.read_csv(CWD+"/sales_calls.csv")
print(calls)
revenue = pd.read_csv(CWD+"/sales_revenue.csv")
print(revenue)