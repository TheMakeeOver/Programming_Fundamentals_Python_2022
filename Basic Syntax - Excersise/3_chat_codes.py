number_of_messages = int(input())

for message in range(number_of_messages):
    number = int(input())
    if number == 88:
        saying = "Hello"
    elif number == 86:
        saying = "How are you?"
    elif number < 88 and number != 88 and number != 86:
        saying = "GREAT!"
    else:
        saying ="Bye."

    print(saying)

