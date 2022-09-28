number_of_strings = int(input())
for string in range(number_of_strings):
    current_string = input()
    status = ""
    if "," in current_string:
        status = f"{current_string} is not pure!"
    elif "." in current_string:
        status = f"{current_string} is not pure!"
    elif "_" in current_string:
        status = f"{current_string} is not pure!"
    else:
        status = f"{current_string} is pure."
    print(status)
