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
#   OUTPUT
#       - Numero de filas en 0 
#       - Numero de filas restantes 
#       - Grafica del voltaje
#       - Visualizacion de las filas corregidas por potencia
#       - ....
from ImportDB import*
from DeleteZerosDB import*
from GraphicDB import*
from PowerCalculation import*
from StandarDeviation import*
from AtypicalValues import*

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

potencias_por_registro = calculate_power_per_record(DBZ)
print("Valores de las primeras 30 filas de la base de datos y potencias calculadas:")
for i, (registro, potencia) in enumerate(zip(DBZ[1:31], potencias_por_registro[:30]), 1):
    print(f'Registro {i}: Datos = {registro}, Potencia = {potencia} KvA')


DE1,DE2,DE3,LIM1I1,LIM2I1,LIM1I2,LIM2I2,LIM1I3,LIM2I3 = standard_deviation(DBZ)
print(f"Desviación Estándar I1: {DE1}")
print(f"Desviación Estándar I2: {DE2}")
print(f"Desviación Estándar I3: {DE3}")


valores_dentro_limites, valores_atipicos = filter_outlier_values(DBZ, LIM1I1, LIM2I1, LIM1I2, LIM2I2, LIM1I3, LIM2I3)

print("Valores dentro de los límites:")
#for row in valores_dentro_limites:
print(len(valores_dentro_limites))

print("\nValores atípicos:")
#for row in valores_atipicos:
    #print(valores_atipicos)
print(len(valores_atipicos))
print(type(valores_atipicos))