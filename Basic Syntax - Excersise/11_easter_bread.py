budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price_per_liter = flour_price * 1.25
milk_needed_price = milk_price_per_liter * 0.25

loaves_made = 0
budget_spend = 0
coloured_eggs = 0

loaves_price = flour_price + milk_needed_price + eggs_price

while budget_spend < (budget - loaves_price):
    loaves_made += 1
    coloured_eggs += 3
    if loaves_made % 3 == 0:
        coloured_eggs -= loaves_made - 2
    budget_spend += loaves_price
money_left = budget - budget_spend
print(f"You made {loaves_made} loaves of Easter bread! Now you have {coloured_eggs} eggs and {money_left:.2f}BGN left.")