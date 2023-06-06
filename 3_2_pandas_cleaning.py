import pandas as pd
import os

CWD = os.path.dirname(os.path.realpath(__file__))

# json
print(" MARS DATA - JSON ".center(50,"="))
mars = pd.read_json(CWD+"/mars_data_01.json")
print(mars)
# csv
print(" TEMP DATA - CSV ".center(50,"="))
temp = pd.read_csv(CWD+"/temp_data_01.csv")
print(temp)
# cleaning Missing
print(" TEMP DATA - Cleaning Missing ".center(50,"="))
temp = pd.read_csv(CWD+"/temp_data_01.csv", na_values=['Missing'])
print(temp)
# writing data -- check files
temp.to_csv(CWD+"/df_out.csv", index=False)
temp.to_json(CWD+"/df_out.json")
# Manipulating columns
print(" TEMP DATA - Manipulating Cols ".center(50,"="))
temp = pd.read_csv(CWD+"/temp_data_01.csv", na_values=['Missing'], header=0,
     names=range(18), usecols=range(4,18))
print(temp)