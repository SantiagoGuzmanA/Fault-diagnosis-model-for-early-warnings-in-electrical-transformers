def filter_outlier_values(database,LIM1I1, LIM2I1, LIM1I2, LIM2I2, LIM1I3, LIM2I3):
    values_within_limits = []
    values_Atypical = []
    
    for row in database[1:]:
        I1 = row[4]
        I2 = row[5]
        I3 = row[6]
        if I1 < LIM2I1 or I1 > LIM1I1 or I2 < LIM2I2 or I2 > LIM1I2 or I3 < LIM2I3 or I3 > LIM1I3:
            values_Atypical.append(row)
        else:
           values_within_limits.append(row)
    
    return values_within_limits, values_Atypical