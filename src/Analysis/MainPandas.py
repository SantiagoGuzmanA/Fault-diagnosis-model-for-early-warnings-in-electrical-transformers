# Este es el programa principal que va a llamar las funciones
#Main : Este programa extrae la informacion de una base de datos guardada en un archivo .txt, para posteriormente hacerle el siguiente tratamiento:
#   - Guardar la base de datos en un elemento tipo lista
#   - Eliminar las filas que contengan un valor 0 en la columna especificada
#   - Graficar la columna del voltaje en funcion del tiempo 
#   - Contar las filas que se eliminaron por tener un 0 
#   - Mostrar las filas que quedaron despues de las eliminadas por 0
#   - Hacer el calculo de la potencia y verificarlo con la columna de la potencia para garantizar que esten bien los datos
#   - ....
# Los readme se deben de hacer para cada carpeta
#   - ....
#   INPUT:
#       - Nombre del archivo de la base de datos con su respectiva extención: Solo compatible con archivos .txt
#       - Numero de la columna en la que se desea buscar valores 0: Se empieza a contar a partir de 1
#       - ....
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
from src.Preprocessing.WorkPandas import*
#import Dataframe 
print("Here we can see a summary of the information in the dataframe: \n")
df.info()
#Rename columns
print("Here we can see a summary of the dataframe information but now with the modified column names: \n")
dfRename.info()
print("\n")
print("Viewing the first rows of the DataFrame as a table: \n")
print(dfRename.head(10))
#Delete zeros
print("Here we can see a summary of the information in the dataframe after removing the rows with zeros: \n")
dfZeros.info()
print("\n")
print("Viewing the first rows of the DataFrame with zeros as a table: \n")
print(dfZeros.head(10))
#statistics
print("Summary of statistics:")
print("\n")
print(dfZeros.describe())
