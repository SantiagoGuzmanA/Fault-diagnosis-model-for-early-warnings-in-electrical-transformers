import math

def calcular_potencia_por_registro(database):

    potencias = []
    for registro in database[1:]:
        voltajes_fase = registro[1:4]  
        corrientes = registro[4:7]  
        vf_promedio = sum(voltajes_fase) / len(voltajes_fase)
        vl = math.sqrt(3) * vf_promedio
        I_promedio = sum(corrientes) / len(corrientes)
        #il = math.sqrt(3) * I_promedio
          
        
        potencia_registro = (math.sqrt(3) * vl * I_promedio)/1000
        potencia_aproximada = round(potencia_registro, 2)
        potencias.append(potencia_aproximada)
    return (potencias)
