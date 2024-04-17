def deleteZeros(DataBase,Columns):
    try:
        if not isinstance(DataBase,list):
            raise TypeError("La entrada de la funcion para eliminar los ceros de la columna de voltage no es un arreglo")
    except TypeError as Error:
        print(Error)
    
    DBZ=[]
    for row in DataBase:
        if all(row[Column] == 0 for Column in Columns):
            continue
        else:
            DBZ.append(row)
    return(DBZ)