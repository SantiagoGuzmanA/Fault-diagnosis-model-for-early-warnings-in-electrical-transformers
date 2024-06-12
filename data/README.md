# Fault Diagnosis Model for Early Warnings in Electrical Transformers

## Data Description

Following the guidelines of our thesis work focused on a fault diagnosis model for early warnings in electrical transformers. The database contains measurements of various electrical variables related to the operation of electrical transformers. These variables are crucial to monitoring transformer health and performance over time. Recorded variables include:

- VL1- Phase Line 1

- VL2- Phase Line 2

- VL3- Phase Line 3

- IL1- Current line 1

- IL2- Current line 2

- IL3- Current line 3

- VL12- Voltage line 1 2

- VL23- Voltage line 2 3

- VL31- Voltage line 3 1

- INUT-Neutral current

**Voltage (VL1, VL2, VL3):** Represents the voltages across different phases of the transformer. Variations in voltage levels can indicate irregularities in the electrical supply or transformer operation.

**Current (IL1, IL2, IL3):** Refers to the electrical currents flowing through each phase of the transformer. Current variations can signal changes in load conditions or potential faults within the transformer.

**Voltage Line Measurements (VL12, VL23, VL31):** These measurements capture the voltages between specific lines of the transformer, providing information on the voltage relationships between phases.

**Neutral Current (INUT):** Represents the current that flows through the neutral line of the transformer. Neutral current monitoring is essential to detect unbalanced loads or ground faults.

The data sampling frequency is every 15 minutes and for a year, so it is likely that a variety of electrical events can be found that could indicate problems in the transformers. In addition to overcurrents, overvoltages, and tripping, here are some other events that might be relevant when analyzing transformer data:

- **Overcurrents and Overvoltages:** Instances where electrical currents or voltages exceed normal operating levels, indicating potential stress on the transformer or external power supply issues.

- **Disconnections and Interruptions:** Sudden drops or interruptions in voltage or current readings, signifying power supply disruptions or faults in the electrical network.

- **Imbalances:** Significant differences between currents or voltages in the three phases that could signal problems in load distribution or system failures.

- **Load Fluctuations:** Changes in load conditions reflected in current and voltage variations, which can indicate shifts in power demand or distribution system issues.

- **Voltage drops:** Sudden reductions in voltage that could indicate connection problems or degradation in the system.

Where with these we will work initially in filtering them to eliminate data rows with currents or voltages in 0, then proceed to heat the instantaneous load of the transformer, in addition to this calculate statistical values such as the standard deviation of the transformer currents, which leads to averages and other values this in order to be able to calculate the minimum and maximum limits of the currents to later do a data labeling analysis and detect atypical values in the currents, with this finally graph the different initial data and obtained to illustrate them in a more efficient way to analyze.
Este directorio contiene los datasets utilizados en el proyecto.
