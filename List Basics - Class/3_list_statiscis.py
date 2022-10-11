number_of_lines = int(input())
positive_list = []
negative_list = []
count_of_positives = 0
sum_of_negatives = 0

for numbers in range(number_of_lines):
    current_number = int(input())
    if current_number >= 0:
        positive_list.append(current_number)
        count_of_positives += 1
    else:
        negative_list.append(current_number)
        sum_of_negatives += current_number

print(positive_list)
print(negative_list)
print(f"Count of positives: {count_of_positives}")
print(f"Sum of negatives: {sum_of_negatives}")
