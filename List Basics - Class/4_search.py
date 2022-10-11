number_of_lines = int(input())
our_word = input()
my_list1 = []
my_list = []
for sent in range(number_of_lines):
    current_sent = input()
    my_list1.append(current_sent)
    if our_word in current_sent:
        my_list.append(current_sent)

print(my_list1)
print(my_list)
