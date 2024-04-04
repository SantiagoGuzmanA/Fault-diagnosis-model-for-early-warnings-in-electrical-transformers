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

def plot_column(column_data):
    plt.plot(column_data)
    plt.xlabel('Índice de fila')
    plt.ylabel('Valor')
    plt.title('Gráfico de la columna filtrada')
    plt.grid(True)
    plt.show()

def convert_column_to_float(DB, column_index):
    column_data = [row[column_index] for row in DB]
    converted_column = []

    for value in column_data:
        try:
            converted_value = float(value)
            converted_column.append(converted_value)
        except ValueError:
        
            pass

    return converted_column

    
#fname = input("Ingrese el nombre del archivo: ")
#DB = importDB(fname)
#for i in DB:
#    print(i) 