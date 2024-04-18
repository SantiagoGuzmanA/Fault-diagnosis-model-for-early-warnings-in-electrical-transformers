def filtrar_valores_atipicos(database,LIM1I1, LIM2I1, LIM1I2, LIM2I2, LIM1I3, LIM2I3):
    valores_dentro_limites = []
    valores_atipicos = []
    
    for row in database[1:]:
        I1 = row[4]
        I2 = row[5]
        I3 = row[6]
        if I1 < LIM2I1 or I1 > LIM1I1 or I2 < LIM2I2 or I2 > LIM1I2 or I3 < LIM2I3 or I3 > LIM1I3:
            valores_atipicos.append(row)
        else:
            valores_dentro_limites.append(row)
    
    return valores_dentro_limites, valores_atipicos