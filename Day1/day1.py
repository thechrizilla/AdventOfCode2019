import math

def fuel_mass(mass):
    fuel = math.floor(mass/3) - 2
    return fuel

def total_mass():
    file = open("day1_input.txt", "r")
    sum = 0
    inputs = file.readlines()
    for input in inputs:
        sum += fuel_mass(int(input))
    return int(sum)

print(total_mass())
