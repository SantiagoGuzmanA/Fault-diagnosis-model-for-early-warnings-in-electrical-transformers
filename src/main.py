# Este es el programa principal que va a llamar las funciones
#Main : Este programa extrae la informacion de una base de datos guardada en un archivo .txt, para posteriormente hacerle el siguiente tratamiento:
#   - Guardar la base de datos en un elemento tipo lista
#   - Eliminar las filas que contengan un valor 0 en la columna especificada
#   - ....
#   - ....
#   INPUT:
#       - Nombre del archivo de la base de datos con su respectiva extención: Solo compatible con archivos .txt
#       - Numero de la columna en la que se desea buscar valores 0: Se empieza a contar a partir de 1
#       - ....
#   OUTPUT
#       -....
from importDB import*

fname = "DatosMonitoringTransformer.txt"
column = input("Ingrese la columna de la potencia: ")

DB = imptDB(fname)
print("Tamaño de la Base de datos con ceros: " + str(len(DB)))

DB = deleteZeros(DB,int(column))
print("Tamaño de la Base de datos sin ceros: " + str(len(DB)))
  
column_index = 1

plot_column(DB,1)