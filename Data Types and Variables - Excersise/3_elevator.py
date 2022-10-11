persons = int(input())
capacity = int(input())

people_left = persons
tours = 0

while people_left > 0:
    people_left -= capacity
    tours += 1

print(f"{tours}")
