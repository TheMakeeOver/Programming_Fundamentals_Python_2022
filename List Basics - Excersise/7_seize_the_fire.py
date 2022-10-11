list_of_fire_cells = input().split("#")
water_given = int(input())
water_available = water_given
effort_value = 0.25
total_effort = 0
total_fire = 0
print("Cells:")
for cells in list_of_fire_cells:
    current_cell = cells.split(" = ")
    type_of_fire = current_cell[0]
    value_of_cell = int(current_cell[1])

    if water_available - value_of_cell >= 0:
        if (type_of_fire == "High" and 81 <= value_of_cell <= 125) or (
                type_of_fire == "Medium" and 51 <= value_of_cell <= 80) or (
                type_of_fire == "Low" and 1 <= value_of_cell <= 50):
            if water_available - value_of_cell >= 0:
                water_available -= value_of_cell
                total_effort += value_of_cell * effort_value
                total_fire += value_of_cell
                print(f" - {value_of_cell}")
        else:
            continue
print(f"Effort: {total_effort:.2f}\nTotal Fire: {total_fire}")
