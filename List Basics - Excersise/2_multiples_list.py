factor = int(input())
count = int(input())
multiple_list = []

for current_number in range(1, count + 1, +1):
    multiple_list.append(factor * current_number)

print(multiple_list)
