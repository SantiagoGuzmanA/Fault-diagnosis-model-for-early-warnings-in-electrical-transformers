import math
def calculate_power_per_record(database):

    powers = []
    for register in database[1:]:
        phase_voltages = register[1:4]  
        currents = register[4:7]  
        vf_average = sum(phase_voltages) / len(phase_voltages)
        vl = math.sqrt(3) * vf_average
        I_average = sum(currents) / len(currents)
        
        power_registration = (math.sqrt(3) * vl * I_average)/1000
        approximate_power = round(power_registration, 2)
        powers.append(approximate_power)
    return (powers)
