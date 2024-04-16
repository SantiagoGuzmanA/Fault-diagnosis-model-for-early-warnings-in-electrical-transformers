import math

def calcular_potencia_por_registro(database):
    # Calcula la potencia trifásica para cada registro en la base de datos
    potencias = []
    for registro in database[1:]:
        voltajes_fase = registro[1:4]  # Indices de las columnas de voltajes de fase VL1, VL2, VL3
        corrientes = registro[4:7]  # Indices de las columnas de corrientes IL1, IL2, IL3
        
        # Calcula el voltaje de línea promedio (VL) en función de los voltajes de fase
        vf_promedio = sum(voltajes_fase) / len(voltajes_fase)
        vl = math.sqrt(3) * vf_promedio  # Voltaje de línea
        
        potencia_registro = math.sqrt(3) * vl * sum(corrientes)  # Calcula la potencia
        potencias.append(potencia_registro)
    return (potencias)
