command = input()
new_string = ""

while command != "End":
    if command == "SoftUni":
        continue
    else:
        for char in command:
            print(char * 2, end="")
        print(new_string)
        command = input()



