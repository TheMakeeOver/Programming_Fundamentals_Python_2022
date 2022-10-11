number_of_lines = int(input())
sum_of_words = 0

for character in range(number_of_lines):
    current_character = input()
    sum_of_words += ord(current_character)

print(f"The sum equals: {sum_of_words}")





