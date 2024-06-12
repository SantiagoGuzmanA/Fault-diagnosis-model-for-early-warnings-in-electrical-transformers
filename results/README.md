# Fault Diagnosis Model for Early Warnings in Electrical Transformers
# Results

## Methodology
1. **Literature Review**: Selection of the method of analysis of electrical variables.
2. **Selection of the Analysis Method**: Evaluation and selection of the most appropriate method.
3. **Identification of Processing Technique**: Research and selection of data processing techniques.
4. **Model Development**: Integration of results and establishment of alarm thresholds.
5. **Validation**: Simulation tests and necessary adjustments.
6. **Documentation and Dissemination**: Preparation of detailed documents on the process and results.

## Types of Results
- `figures/`: Graphs generated during the analysis.
- `tables/`: Tables with performance metrics and other relevant results.
- `model/`: Trained model.

## Results
**- Histograms of each variable:**
  
![Histograms of each variable](./figures/Histograms%20of%20each%20variable.png)

**- Distribution by voltage phase characteristics:**

![Distribution by voltage phase characteristics](./figures/Histogram%20of%20Phase%20Voltage.png)

**- Distribution by classes of phase currents with their density plot:**

![Distribution by classes of phase currents with their density plot](./figures/Histogram%20of%20Phase%20Current.png)

**- Density plot of inter-phase voltages:**

![Density plot of inter-phase voltages](./figures/Histogram%20of%20Voltage%20Differences.png)

**- Density plots:**

![Density plots](./figures/Density%20Plot%20of.png)

**- Box plots:**

![Box plots](./figures/Boxplot%20of.png)

**- Violin plots:**

![Violin plots](./figures/Violin%20Plot%20of.png)

## Discussion and Conclusions
**- Shapiro-Wilk test**
The results of the Shapiro-Wilk test for all features (phase voltages, phase currents, and voltage differences) show that none of the distributions are normal. This suggests that for any further analysis or statistical tests, we may need to use non-parametric techniques that do not assume normality in the data.


## Ejemplos
Aquí se incluyen ejemplos de archivos de resultados para referencia futura.



Estructura del Proyecto
src/: Códigos fuente en Python.
data/: Datasets utilizados.
results/: Resultados obtenidos, incluyendo figuras, gráficos y tablas.
