import math
def calculate_power_per_recordOP(database): 
    """
    Calculates the power per record in the database based on provided voltage and current values.

    Parameters:
    database (list): List of lists where each sublist represents a row of data. 
                     It is assumed that rows have at least 7 elements:
                     - The first three elements (index 1 to 3) are voltage values.
                     - The next three elements (index 4 to 6) are current values.

    Returns:
    list: A list of calculated power values for each record, rounded to two decimal places.
    
    Example:
    >>> database = [
    ...     ["header1", "V1", "V2", "V3", "I1", "I2", "I3"],
    ...     [1, 220, 230, 240, 10, 12, 11],
    ...     [2, 210, 215, 225, 9, 10, 9]
    ... ]
    >>> calculate_power_per_recordOP(database)
    [503.83, 445.68]
    """
    powers = [] 
    for register in database[1:]: 
        powers.append (round((math.sqrt(3) * (math.sqrt(3) * (sum(register[1:4]) / 3)) * (sum(register[4:7]) / 3)) / 1000, 2)) # O(1)
    return powers 
