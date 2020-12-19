#%%
import pandas as pd
from itertools import groupby

file = open("4th_day_input.txt","r")
file = file.readlines()

# data = pd.read_csv("4th_day_input.txt", sep="", header=None)
# %%

test = [list(g) for k, g in groupby(file, key=lambda x: x != "\n") if k]

test1 = []
for k, g in groupby(file, key=lambda x: x != "\n"):
    if k:
        test1.append(list(g))
        # data_dict[idx] = line.split(" ")
        
# %%
