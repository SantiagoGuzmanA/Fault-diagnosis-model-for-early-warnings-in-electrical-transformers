import pandas as pd
def process_transformer_data(file_path):
    """
    Processes transformer data from a CSV file.

    Parameters:
    file_path (str): The file path to the CSV file containing transformer data.

    Returns:
    tuple: A tuple containing three DataFrames:
           1. The original DataFrame read from the CSV file.
           2. A DataFrame with columns renamed for clarity.
           3. A DataFrame with rows filtered where phase currents are not zero.

    Example:
    >>> process_transformer_data("transformer_data.csv")
    (original_df, renamed_df, filtered_df)
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
