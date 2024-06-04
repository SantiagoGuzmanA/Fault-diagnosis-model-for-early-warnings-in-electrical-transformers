import math
def standard_deviationOP(database):
    n = len(database)  # O(1)
    if n <= 1:  # O(1)
        return 0, 0, 0, 0, 0, 0, 0, 0, 0  # O(1)

    I1_sum,I2_sum,I3_sum,distMediaI1_sum,distMediaI2_sum,distMediaI3_sum  = 0,0,0,0,0,0  # O(1)

    for row in database[1:]:  # O(n)
        I1_sum += row[4]  # O(1)
        I2_sum += row[5]  # O(1)
        I3_sum += row[6]  # O(1)

    I1avg = I1_sum / (n - 1)  # O(1)
    I2avg = I2_sum / (n - 1)  # O(1)
    I3avg = I3_sum / (n - 1)  # O(1)

    for row in database[1:]:  # O(n)
        distMediaI1_sum += (row[4] - I1avg) ** 2  # O(1)
        distMediaI2_sum += (row[5] - I2avg) ** 2  # O(1)
        distMediaI3_sum += (row[6] - I3avg) ** 2  # O(1)

    DEI1 = round(math.sqrt(distMediaI1_sum / (n - 1)), 2)  # O(1)
    DEI2 = round(math.sqrt(distMediaI2_sum / (n - 1)), 2)  # O(1)
    DEI3 = round(math.sqrt(distMediaI3_sum / (n - 1)), 2)  # O(1)

    LIM1I1 = I1avg + DEI1  # O(1)
    LIM2I1 = I1avg - DEI1  # O(1)
    LIM1I2 = I2avg + DEI2  # O(1)
    LIM2I2 = I2avg - DEI2  # O(1)
    LIM1I3 = I3avg + DEI3  # O(1)
    LIM2I3 = I3avg - DEI3  # O(1)

    return DEI1, DEI2, DEI3, LIM1I1, LIM2I1, LIM1I2, LIM2I2, LIM1I3, LIM2I3  # O(1)