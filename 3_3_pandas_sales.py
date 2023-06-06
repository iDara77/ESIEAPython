import pandas as pd
import os

CWD = os.path.dirname(os.path.realpath(__file__))

calls = pd.read_csv(CWD+"/sales_calls.csv")
print(calls)
revenue = pd.read_csv(CWD+"/sales_revenue.csv")
print(revenue)
calls_revenue = pd.merge(calls, revenue, on=['Territory', 'Month'])
print(calls_revenue)
print(calls_revenue[calls_revenue.Month == 1])