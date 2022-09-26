number_of_orders = int(input())
price_per_capsule = float(input())
days = int(input())
capsules_needed = int(input())

for i in range(number_of_orders +1):
    total_price = ""
    for price_per_capsule in range(0.01, 100.00, +0.01):
        for days in range(1, 31, +1):
            for capsules_needed in range(1, 2000, +1):
                price = price_per_capsule * days * capsules_needed
                print("The price for the coffee is ${price:00d}")
print("Total: ${total_price:00d")




