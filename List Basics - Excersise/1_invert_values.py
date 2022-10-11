numbers = input().split()
opposite_numbers = []

for given_number in numbers:
    current_number = -int(given_number)
    opposite_numbers.append(current_number)

print(opposite_numbers)
