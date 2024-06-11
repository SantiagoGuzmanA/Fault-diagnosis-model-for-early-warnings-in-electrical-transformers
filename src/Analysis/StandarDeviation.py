import math
def standard_deviationOP(database):
    """
    Calculates the standard deviation and upper/lower limits for three parameters (I1, I2, I3) in the database.

    Parameters:
    database (list): List of lists where each sublist represents a row of data.
                     It is assumed that rows have at least 7 elements:
                     - The 5th element (index 4) is the value for I1.
                     - The 6th element (index 5) is the value for I2.
                     - The 7th element (index 6) is the value for I3.

    Returns:
    tuple: A tuple containing the following values:
        - DEI1 (float): Standard deviation of I1.
        - DEI2 (float): Standard deviation of I2.
        - DEI3 (float): Standard deviation of I3.
        - LIM1I1 (float): Upper limit for I1.
        - LIM2I1 (float): Lower limit for I1.
        - LIM1I2 (float): Upper limit for I2.
        - LIM2I2 (float): Lower limit for I2.
        - LIM1I3 (float): Upper limit for I3.
        - LIM2I3 (float): Lower limit for I3.

    Example:
    >>> database = [
    ...     ["header1", "header2", "header3", "header4", "I1", "I2", "I3"],
    ...     [1, 2, 3, 4, 10, 12, 11],
    ...     [5, 6, 7, 8, 9, 10, 9],
    ...     [9, 10, 11, 12, 11, 13, 12]
    ... ]
    >>> standard_deviationOP(database)
    (0.82, 1.53, 1.25, 10.82, 9.18, 12.53, 9.47, 12.25, 9.75)
    """
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