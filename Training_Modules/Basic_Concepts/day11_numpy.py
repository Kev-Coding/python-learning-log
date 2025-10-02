import numpy as np

my_list = [10,20,30,40,50]
my_array = np.array(my_list)
print(my_array)
print(my_list)
my_new_array = my_array * 2
print(my_new_array) 

my_new_list = []

for item in my_list:
    my_new_list.append(item * 2)

print(my_new_list)