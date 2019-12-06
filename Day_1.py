import math

def mass_to_fuel_req(masses):

    file = open(masses, "r")
    data = file.readlines()
    list_to_combine = []
    for line in data:
        mass = line.split()
        divided = int(mass[0]) / 3
        #Not Satisfied with how I extracted information from the file
        floored = math.floor(divided)
        deduct = floored - 2
        list_to_combine.append(deduct)

    total = sum(list_to_combine)
    return total

    file.close()

print(mass_to_fuel_req("Puzzle_Input_1.txt"))
