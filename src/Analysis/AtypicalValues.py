def filter_outlier_values(database,LIM1I1, LIM2I1, LIM1I2, LIM2I2, LIM1I3, LIM2I3):
    """
    Filters outlier values from a database based on specified limits for three parameters (I1, I2, I3).

    Parameters:
    database (list): List of lists where each sublist represents a row of data. It is assumed that rows have at least 7 elements.
    LIM1I1 (float): Upper limit for parameter I1.
    LIM2I1 (float): Lower limit for parameter I1.
    LIM1I2 (float): Upper limit for parameter I2.
    LIM2I2 (float): Lower limit for parameter I2.
    LIM1I3 (float): Upper limit for parameter I3.
    LIM2I3 (float): Lower limit for parameter I3.

    Returns:
    tuple: A tuple containing two lists:
        - values_within_limits (list): List of rows that are within the specified limits.
        - values_Atypical (list): List of rows that are outside the specified limits.
    
    Example:
    >>> database = [
    ...     ["header1", "header2", "header3", "header4", "I1", "I2", "I3"],
    ...     [1, 2, 3, 4, 5, 6, 7],
    ...     [8, 9, 10, 11, 12, 13, 14],
    ...     [15, 16, 17, 18, 19, 20, 21]
    ... ]
    >>> LIM1I1, LIM2I1 = 15, 5
    >>> LIM1I2, LIM2I2 = 20, 10
    >>> LIM1I3, LIM2I3 = 25, 15
    >>> filter_outlier_values(database, LIM1I1, LIM2I1, LIM1I2, LIM2I2, LIM1I3, LIM2I3)
    ([
        [1, 2, 3, 4, 5, 6, 7]
    ], [
        [8, 9, 10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19, 20, 21]
    ])
    """
    values_within_limits = []
    values_Atypical = []
    
    for row in database[1:]:
        I1 = row[4]
        I2 = row[5]
        I3 = row[6]
        if I1 < LIM2I1 or I1 > LIM1I1 or I2 < LIM2I2 or I2 > LIM1I2 or I3 < LIM2I3 or I3 > LIM1I3:
            values_Atypical.append(row)
        else:
           values_within_limits.append(row)
    
    return values_within_limits, values_Atypical