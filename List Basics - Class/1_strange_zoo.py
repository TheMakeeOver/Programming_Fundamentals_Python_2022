my_list = []

for data in range(3):
    my_list.append(input())

my_list[0], my_list[-1] = my_list[-1], my_list[0]

print(my_list)