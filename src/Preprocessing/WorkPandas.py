import pandas as pd
def process_transformer_data(file_path):
    """
    Procesa el archivo de datos de monitoreo de transformadores.

    Parameters:
    file_path (str): Ruta al archivo de datos CSV.

    Returns:
    DataFrame: Un DataFrame con los datos procesados.
    """
    # Leer el archivo CSV
    df = pd.read_csv(file_path, sep=",")
    
    # Renombrar columnas
    df_rename = df.rename(columns={
        "VL1": "Phase 1 Voltage",
        "VL2": "Phase 2 Voltage",
        "VL3": "Phase 3 Voltage",
        "IL1": "Phase 1 Current",
        "IL2": "Phase 2 Current",
        "IL3": "Phase 3 Current",
        "VL12": "1-2 Voltage",
        "VL23": "2-3 Voltage",
        "VL31": "3-1 Voltage",
        "INUT": "Neutral Current"
    })
    
    # Filtrar filas donde las corrientes de fase no sean cero
    dfZeros = df_rename.loc[(df_rename[["Phase 1 Current", "Phase 2 Current", "Phase 3 Current"]] != 0).all(axis=1)]
    
    return df, df_rename, dfZeros
