def deleteZeros(DataBase,Column):
    try:
        if not isinstance(DataBase,list):
            raise TypeError("El input de la funcion deleteZeros no es un arreglo")
    except TypeError as Error:
        print(Error)
    
    DB=[]
    for row in DataBase:
        if row[Column-1] != 0:
            DB.append(row)
    return(DB)