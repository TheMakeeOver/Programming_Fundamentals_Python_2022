group_size = int(input())
days = int(input())
people = group_size
coins = 0
coins_per_person = int(coins / people)

for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        people -= 2
    if current_day % 15 == 0:
        people += 5
    coins += 50
    coins -= people * 2
    if current_day % 3 == 0:
        coins -= people * 3
    if current_day % 5 == 0:
        coins += people * 20
        if current_day % 3 == 0:
            coins -= people * 2
coins_per_person = int(coins / people)
print(f"{people} companions received {coins_per_person} coins each.")
