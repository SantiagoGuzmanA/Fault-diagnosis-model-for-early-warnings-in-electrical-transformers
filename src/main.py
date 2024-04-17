# Este es el programa principal que va a llamar las funciones
#Main : Este programa extrae la informacion de una base de datos guardada en un archivo .txt, para posteriormente hacerle el siguiente tratamiento:
#   - Guardar la base de datos en un elemento tipo lista
#   - Eliminar las filas que contengan un valor 0 en la columna especificada
#   - Graficar la columna del voltaje en funcion del tiempo 
#   - Contar las filas que se eliminaron por tener un 0 
#   - Mostrar las filas que quedaron despues de las eliminadas por 0
#   - Hacer el calculo de la potencia y verificarlo con la columna de la potencia para garantizar que esten bien los datos
#   - ....
#   - ....
#   INPUT:
#       - Nombre del archivo de la base de datos con su respectiva extención: Solo compatible con archivos .txt
#       - Numero de la columna en la que se desea buscar valores 0: Se empieza a contar a partir de 1
#       - ....
#   OUTPUT
#       - Numero de filas en 0 
#       - Numero de filas restantes 
#       - Grafica del voltaje
#       - Visualizacion de las filas corregidas por potencia
#       - ....
from importDB import*
from DeleteZerosDB import*
from GraphicDB import*
from CalculoPotencia import*
from Desviacion_Estandar import*

fname = "DatosMonitoringTransformer.txt"
column = [4, 5, 6]
DB = impDB(fname)
print("Tamaño de la Base de datos con ceros: " + str(len(DB)))
#for i in DB:
    #print(i)
DBZ = deleteZeros(DB,column)
print("Tamaño de la Base de datos sin ceros: " + str(len(DBZ)))
#for i in DB:
    #print(i)
    
plot_column(DBZ,4)
plot_column1(DBZ,5)
plot_column2(DBZ,6)

potencias_por_registro = calcular_potencia_por_registro(DBZ)
print("Valores de las primeras 30 filas de la base de datos y potencias calculadas:")
for i, (registro, potencia) in enumerate(zip(DBZ[1:31], potencias_por_registro[:30]), 1):
    print(f'Registro {i}: Datos = {registro}, Potencia = {potencia} KvA')

DE1,DE2,DE3 = desviacion_estandar(DBZ)
print(f"Desviación Estándar I1: {DE1}")
print(f"Desviación Estándar I2: {DE2}")
print(f"Desviación Estándar I3: {DE3}")