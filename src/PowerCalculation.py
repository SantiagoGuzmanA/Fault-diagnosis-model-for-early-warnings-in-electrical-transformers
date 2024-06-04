import math
def calculate_power_per_recordOP(database): # O(1)
    powers = [] # O(1)
    for register in database[1:]: # O(n)
        powers.append (round((math.sqrt(3) * (math.sqrt(3) * (sum(register[1:4]) / 3)) * (sum(register[4:7]) / 3)) / 1000, 2)) # O(1)
    return powers # O(1)
