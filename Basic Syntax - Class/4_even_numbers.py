number = int(input())

for i in range(number):
    numbers = int(input())
    if not numbers % 2 == 0:
        print(f"{numbers} is odd!")
        break
else:
    print("All numbers are even.")