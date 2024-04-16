import math

def calcular_potencia_por_registro(database):

    potencias = []
    for registro in database[1:]:
        voltajes_fase = registro[1:4]  
        corrientes = registro[4:7]  
        vf_promedio = sum(voltajes_fase) / len(voltajes_fase)
        vl = math.sqrt(3) * vf_promedio  
        
        potencia_registro = math.sqrt(3) * vl * sum(corrientes)
        potencias.append(potencia_registro)
    return (potencias)
