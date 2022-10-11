number = int(input())

for numbers in range(1, number + 1):
    digits_counter = 0
    digits = numbers

    while digits > 0:
        digits_counter += digits % 10
        digits = int(digits / 10)

    if digits_counter == 5 or digits_counter == 7 or digits_counter == 11:
        print(f"{numbers} -> True")
    else:
        print(f"{numbers} -> False")


