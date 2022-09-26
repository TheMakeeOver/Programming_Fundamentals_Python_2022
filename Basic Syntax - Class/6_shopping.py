budget = int(input())
price = input()

while price != "End":
    sum = int(price)
    budget -= sum
    if budget < 0:
        print("You went in overdraft")
        break
    price = input()
else:
    print('You bought everything needed')













