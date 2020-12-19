#%%
import pandas as pd
from itertools import groupby

with open("4th_day_input.txt", "r") as f:
    d = f.read().splitlines()
    data = [list(g) for k, g in groupby(d, key=lambda x: x != "") if k]

passports = {}
for index, entry in enumerate(data):
    passports[index] = {}
    for char, string in enumerate(entry):
        entry_list = data[index][char].split(" ")
        for i in entry_list:
            key = i[0:3]
            value = i[4::]
            passports[index][key] = value

sorted_data = pd.DataFrame.from_dict(passports)
