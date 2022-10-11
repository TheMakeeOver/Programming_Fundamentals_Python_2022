day_events = input().split("|")
total_coins = 100
total_energy = 100
event_name = ""
event_value = ""
bakery_is_open = True
for event in day_events:
    current_event = event.split("-")
    name_of_event = current_event[0]
    value_of_event = int(current_event[1])
    # name_of_event, int(value_of_event) = event.split("-")
    if name_of_event == "rest":
        current_energy = total_energy
        total_energy += value_of_event
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif name_of_event == "order":
        if total_energy >= 30:
            total_coins += value_of_event
            total_energy -= 30
            print(f"You earned {value_of_event} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= value_of_event:
            total_coins -= value_of_event
            print(f"You bought {name_of_event}.")
        else:
            print(f"Closed! Cannot afford {name_of_event}.")
            bakery_is_open = False
            break

if bakery_is_open:
    print(f"Day completed!\nCoins: {total_coins}\nEnergy: {total_energy}")
