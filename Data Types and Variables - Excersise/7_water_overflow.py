number_of_lines = int(input())
water_tank = 255
water_filled = 0

for current_line in range(number_of_lines):
    litters_of_water = int(input())
    if water_tank - litters_of_water < 0:
        water_tank += litters_of_water
        print("Insufficient capacity!")
        continue
    water_tank -= litters_of_water
    water_filled += litters_of_water
print(f"{water_filled}")

