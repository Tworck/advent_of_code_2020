#%%
import numpy as np

#%%
data = np.loadtxt("1stinput.txt")

# def find_pairs(data):
#     sum_data = np.zeros(data.size)
#     numbers = []

#     for i in range(data.size):
#         sum_data = data + np.roll(data,i)

#         if 2020 in sum_data:
#             index = np.where(sum_data==2020)
#             a = data[index]
#             numbers.append(a)
#     return np.product(numbers)

# product = find_pairs(data)
# print(product)


def find_three(data):
    sum_data = np.zeros(data.size)
    numbers = []

    for i in range(data.size):
        for j in range(sum_data.size):
            sum_data = data + np.roll(data,i) + np.roll(data,j)
            if 2020 in sum_data:
                index = np.where(sum_data==2020)
                a = data[index]
                numbers.append(a)
    return int(np.product(np.unique(numbers)))

product = find_three(data)
print(product)
