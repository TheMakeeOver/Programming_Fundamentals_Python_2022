quantity_of_decorations = int(input())
days_until_christmas = int(input())
budget = 0
total_spirit = 0

ornaments_price = 2
ornaments_spirit = 5

skirt_price = 5
skirt_spirit = 3

garland_price = 3
garland_spirit = 10

lights_price = 15
lights_spirit = 17

for days in range(1, days_until_christmas + 1, +1):
    if days % 11 == 0:
        quantity_of_decorations += 2
    if days % 2 == 0:
        budget += ornaments_price * quantity_of_decorations
        total_spirit += ornaments_spirit
    if days % 3 == 0:
        budget += (skirt_price + garland_price) * quantity_of_decorations
        total_spirit += skirt_spirit + garland_spirit
    if days % 5 == 0:
        budget += lights_price * quantity_of_decorations
        total_spirit += lights_spirit
        if days % 3 == 0:
            total_spirit += 30
    if days % 10 == 0:
        total_spirit -= 20
        budget += skirt_price + garland_price + lights_price
if days_until_christmas % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")




