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


# part 2

def mass_to_fuel_req_2(masses):
    file = open(masses, "r")
    data = file.readlines()
    list_to_combine = []
    for line in data:
        mass = line.split()
        divided = int(mass[0]) / 3  # divide every mass by 3
        # Not Satisfied with how I extracted information from the file
        floored = math.floor(divided)  # round down divided masses
        deduct = floored - 2  # subtract rounded, divided masses by 2
        new_deducts_list = []  # add divided mass to a new list

        while deduct > 0:  # check if a positive number
            divided = deduct / 3  # repeat division
            # Not Satisfied with how I extracted information from the file
            floored = math.floor(divided)  # round down divided masses
            deduct = floored - 2  # subtract rounded and divided masses

            if deduct > 0:  # if a positive number once more
                new_deducts_list.append(deduct)

        new_deducts_list.append(deduct)
        new_sum = sum(new_deducts_list)

        list_to_combine.append(new_sum)

    total = sum(list_to_combine)
    return total

    file.close()


print(mass_to_fuel_req("Puzzle_Input_Day_1.txt"))
print(mass_to_fuel_req_2("Puzzle_Input_Day_1.txt"))
