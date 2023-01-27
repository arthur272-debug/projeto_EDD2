import pandas as pd;
import logging;

headers = pd.read_csv("escolas_ideb_v2.csv", nrows=0).columns;

data2 = pd.read_csv("escolas_ideb_v2.csv", skiprows=866, names=headers, nrows=1000);


# data = data[(data["latitude"].notna()) & (data["longitude"].notna())];

print(data2);
# print(data2);


# result = pd.concat([data, data2], ignore_index=True);

# print(result);
