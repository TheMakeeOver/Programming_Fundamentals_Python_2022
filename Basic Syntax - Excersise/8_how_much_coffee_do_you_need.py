command = input()
number_of_coffees = 0

while command != "END":
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        number_of_coffees += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        number_of_coffees += 2
    else:
        number_of_coffees += 0
    command = input()

if number_of_coffees > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees)


#command = ""
#number_of_coffees = 0
#while command != "End":
#    command = input()
#   if command.lower() == "coding"\
#        or command.lower() == "dog" \
#        or command.lower() == "cat" \
#        or command.lower() == "movie":
#        if command.islower():
#            number_of_coffees += 1
#        else:
#           number_of_coffees += 0
