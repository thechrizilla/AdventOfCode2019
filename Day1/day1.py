import math

def fuel(mass):
    fuel = math.floor(mass/3) - 2
    return fuel

def total_fuel():
    file = open("day1_input.txt", "r")
    sum = 0
    inputs = file.readlines()
    for input in inputs:
        sum += fuel(int(input))
    return int(sum)

def fuel_c(mass):
    t_fuel = fuel(mass)
    if t_fuel <= 0:
        return 0
    else:
        return t_fuel + fuel_c(t_fuel)

def total_fuel_c():
    file = open("day1_input.txt", "r")
    sum = 0
    inputs = file.readlines()
    for input in inputs:
        sum += fuel_c(int(input))
    return int(sum)


print(total_fuel())
print(total_fuel_c())
