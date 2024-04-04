def importDB(DataBase):
    try:
        fhand = open(DataBase)
    except:
        print("El archivo .txt no existe en la ruta especificada")
        quit()
    
    DB = []
    for line in fhand:
        row = [float(value) if value.replace('.', '', 1).isdigit() else value for value in line.strip().split(',')]
        DB.append(row)
    return(DB)

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

    
import matplotlib.pyplot as plt

def plot_column(DataBase,column_index):
    column_data = [row[column_index] for row in DataBase]
    converted_column = []

    for value in column_data[1:]:
        converted_column.append(value)
        
    plt.plot(converted_column)
    plt.xlabel('# De datos')
    plt.ylabel('Voltaje')
    plt.title('Gráfico de Voltaje')
    plt.grid(True)
    plt.show()

