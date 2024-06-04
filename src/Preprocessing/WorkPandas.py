import pandas as pd
df = pd.read_csv("DatosMonitoringTransformer.txt", sep=",")

dfRename = df.rename(columns={
                        "VL1": "Phase 1 Voltage",
                        "VL2": "Phase 2 Voltage",
                        "VL3": "Phase 3 Voltage",
                        "IL1": "Phase 1 Current",
                        "IL2": "Phase 2 Current",
                        "IL3": "Phase 3 Current",
                        "VL12": "1-2 Voltage",
                        "VL23": "2-3 Voltage",
                        "VL31": "3-1 Voltage",
                        "INUT": "Neutral Current"})

dfZeros = dfRename.loc[(dfRename[["Phase 1 Current", "Phase 2 Current", "Phase 3 Current"]] != 0).all(axis=1)]
