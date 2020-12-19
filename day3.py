#%%
import pandas as pd

data = pd.read_csv("3rd_day_input.txt", header=None)

move_list = [(1,1),(3,1),(5,1),(7,1),(1,2)]
tree_count = 0
tree_product = 1

for right, down in move_list:
    data_rows = data.groupby(data.index // down).first()
    # print(data_rows)
    for index, row in data_rows.iterrows():

        if index+1 == len(data_rows[0]):
            break

        position = right*(index+1)
        
        if position > len(data[0][0])-1:
            position = position % (len(data[0][0]))

        char = data_rows[0][index+1][position]
        if char == "#":
            tree_count += 1

    tree_product *= tree_count

    tree_count = 0

    print(right, down)
    print(tree_count)
print(tree_product)
