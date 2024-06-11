def deleteZerosOP(DataBase, Columns):  # O(1)
    """
    Removes rows from the database where all specified columns have a value of zero.

    Parameters:
    DataBase (list): List of lists where each sublist represents a row of data.
    Columns (list): List of column indices to check for zero values.

    Returns:
    list: A new list with rows removed where all specified columns have zero values.

    Raises:
    TypeError: If the DataBase is not a list or if there is a type error during processing.

    Example:
    >>> DataBase = [
    ...     ["header1", "header2", "header3", "header4"],
    ...     [1, 0, 0, 0],
    ...     [2, 3, 4, 5],
    ...     [0, 0, 0, 0]
    ... ]
    >>> Columns = [1, 2, 3]
    >>> deleteZerosOP(DataBase, Columns)
    [['header1', 'header2', 'header3', 'header4'], [2, 3, 4, 5]]
    """
    if not isinstance(DataBase, list):  # O(1)
        raise TypeError("The input of the function to remove zeros from the current column is not an array")  # O(1)
    try:  # O(1)
        DBZ = [row for row in DataBase if not all(row[column] == 0 for column in Columns)]  # O(n)
    except TypeError as Error:  # O(1)
        print(Error)  # O(1)
    return DBZ  # O(1)