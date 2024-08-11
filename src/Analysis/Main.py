import sys
import os

# Add project root to the system path
# HELLO
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
print(project_root)

# Import modules from project
from src.Preprocessing.ImportDB import *
from src.Preprocessing.DeleteZerosDB import*
from src.Visualization.GraphicDB import*
from src.Analysis.PowerCalculation import*
from src.Analysis.StandarDeviation import*
from src.Analysis.AtypicalValues import*

fname = os.path.join(project_root, 'data', 'raw', 'DatosMonitoringTransformer.txt')
column = [4, 5, 6]
# Import database
DB = impDB(fname)
print("Tamaño de la Base de datos con ceros: " + str(len(DB)))

# Delete rows with zeros
DBZ = deleteZerosOP(DB,column)
print("Tamaño de la Base de datos sin ceros: " + str(len(DBZ)))

# Generate graphs for specified columns
plot_column(DBZ,4)
plot_column1(DBZ,5)
plot_column2(DBZ,6)
plot_power_bar(DBZ)

# Calculate power per record
potencias_por_registro = calculate_power_per_recordOP(DBZ)
print("Valores de las primeras 30 filas de la base de datos y potencias calculadas:")
for i, (registro, potencia) in enumerate(zip(DBZ[1:31], potencias_por_registro[:30]), 1):
    print(f'Registro {i}: Datos = {registro}, Potencia = {potencia} KvA')
    
# Calculate standard deviation
DE1,DE2,DE3,LIM1I1,LIM2I1,LIM1I2,LIM2I2,LIM1I3,LIM2I3 = standard_deviationOP(DBZ)
print(f"Standard deviation I1: {DE1}")
print(f"Standard deviation I2: {DE2}")
print(f"Standard deviation I3: {DE3}")
print(f"Upper limit I1: {LIM1I1}")
print(f"Lower limit I1: {LIM2I1}")
print(f"Upper limit I2: {LIM1I2}")
print(f"Lower limit I2: {LIM2I2}")
print(f"Upper limit I3: {LIM1I3}")
print(f"Lower limit I3: {LIM2I3}\n")

# Filter outlier values
valores_dentro_limites, valores_atipicos = filter_outlier_values(DBZ, LIM1I1, LIM2I1, LIM1I2, LIM2I2, LIM1I3, LIM2I3)
print("Valores dentro de los límites:")
print(len(valores_dentro_limites))
print("\nValores atípicos:")
print(len(valores_atipicos))
