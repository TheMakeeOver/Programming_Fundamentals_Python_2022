list_of_items = input().split("|")
budget = float(input())
current_budget = budget

item_type = ""
item_price = ""

train_ticket = 150
clothes_max_price = 50
shoes_max_price = 35
accessories_max_price = 20.50
profit_in_percent = 1.4

new_price = 0.00
list_of_sold_items_price = []
final_budget = 0
profit = 0

for item in list_of_items:
    current_item = item.split("->")
    item_type = current_item[0]
    item_price = float(current_item[1])
    if budget - item_price >= 0:
        if item_type == "Clothes":
            if item_price <= clothes_max_price and item_price <= current_budget:
                current_budget -= item_price
                new_price = item_price * profit_in_percent
                list_of_sold_items_price.append(new_price)
                final_budget += new_price
                profit += (new_price - item_price)
            else:
                continue
        elif item_type == "Shoes":
            if item_price <= shoes_max_price and item_price <= current_budget:
                current_budget -= item_price
                new_price = item_price * profit_in_percent
                list_of_sold_items_price.append(new_price)
                final_budget += new_price
                profit += (new_price - item_price)
            else:
                continue
        else:
            if item_price <= accessories_max_price and item_price <= current_budget:
                current_budget -= item_price
                new_price = (item_price * profit_in_percent)
                list_of_sold_items_price.append(new_price)
                final_budget += new_price
                profit += (new_price - item_price)
            else:
                continue

for i in range(len(list_of_sold_items_price)):
    print(f"{list_of_sold_items_price[i]:.2f} ", end="")

print(f"\nProfit: {profit:.2f}")
if final_budget + profit >= train_ticket:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")
