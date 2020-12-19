#%%
import json
import pandas as pd

#%%

file = "2nd_day_input.txt"
names =  ["num_chars","char","password"]

data = pd.read_csv(file, sep=" ",header = None, names = names)

data["min_chars"], data["max_chars"] = data["num_chars"].str.split("-",1).str
data["min_chars"] = pd.to_numeric(data["min_chars"])
data["max_chars"] = pd.to_numeric(data["max_chars"])
data["char"] = data["char"].str[0]
data.drop(columns=["num_chars"])

char = data["char"]
min_chars = data["min_chars"]
max_chars = data["max_chars"]
password = data["password"]

# %%
count = 0
count2 = 0
for index, row in data.iterrows():
    if min_chars[index] <= password[index].count(char[index]) <= max_chars[index]:
        count += 1
    if password[index][min_chars[index]-1] == char[index] and password[index][max_chars[index]-1] != char[index]:
        count2 += 1
    if password[index][min_chars[index]-1] != char[index] and password[index][max_chars[index]-1] == char[index]:
        count2 += 1

print(count, count2)   


# %%
 