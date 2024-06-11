def impDB(DataBase):
    """
    Imports a database from a specified .txt file, converting numeric values to floats.

    Parameters:
    DataBase (str): The path to the .txt file containing the database.

    Returns:
    list: A list of lists where each sublist represents a row of data. 
          Numeric values are converted to floats, and non-numeric values are kept as strings.

    Raises:
    FileNotFoundError: If the specified file does not exist.

    Example:
    >>> # Assuming the file 'data.txt' contains:
    >>> # 1,2,3
    >>> # 4,5,6
    >>> impDB('data.txt')
    [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    """
    try:
        Data = open(DataBase)
    except:
        print("El archivo .txt no existe en la ruta especificada")
        quit()
    
    DB = []
    for line in Data:
        row = [float(value) if value.replace('.', '', 1).isdigit() else value for value in line.strip().split(',')]
        DB.append(row)
    return(DB)
