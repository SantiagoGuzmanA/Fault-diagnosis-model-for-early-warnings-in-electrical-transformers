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

**- Shapiro-Wilk test:**
The results of the Shapiro-Wilk test for all features (phase voltages, phase currents, and voltage differences) show that none of the distributions are normal. This suggests that for any further analysis or statistical tests, we may need to use non-parametric techniques that do not assume normality in the data.

**- Shapiro-Wilk test and the Kolmogorov-Smirnov test:**
Both the results of the Shapiro-Wilk test and the Kolmogorov-Smirnov test provide strong evidence that none of the data distributions (phase voltages, phase currents, and voltage differences) are normal. The extremely high KS-statistic values and the p-values of 0.0 in all tests suggest that these distributions deviate significantly from a normal distribution.

**- Kruskal-Wallis test:**
The results of the Kruskal-Wallis test indicate that at least one of the transformer's features (phase voltages, phase currents, etc.) is significantly different from the others since the p-value is less than the typically used significance level (α) of 0.05, we reject the null hypothesis. Therefore, we conclude that there is a significant difference between at least one of the groups of transformer features.

**- Fisher Discriminant Ratio Conclusion:**

* Phase 3 Voltage and Phase 2 Current: These features have high FDR values, suggesting they are effective in distinguishing between different instances within the class in the dataset.

* 1-2 Voltage and 2-3 Voltage: They also show high FDR values, indicating they are relevant in distinguishing between different instances within the class in the dataset.

* Phase 1 Voltage, Phase 2 Voltage, Phase 1 Current, Phase 3 Current, and 3-1 Voltage: These features have lower FDR values compared to the former. Although they still show some degree of effectiveness in distinguishing between different instances within the class, the variability between instances is not as dominant compared to the variability within each feature.

**- AUC Conclusion:** These results occur because calculating the AUC requires at least two classes to evaluate the separation ability between them. Since my dataset only has one class, the AUC cannot be calculated.

Given this scenario, we should consider other metrics or approaches to evaluate the discriminative ability of the features in my dataset.

**- Correlation coefficient:**
These results show the correlations between the numerical features and the target variables 'Phase 1 Current', 'Phase 2 Current', and 'Phase 3 Current'.

* Positive correlations: The features 'Phase 1 Current', 'Phase 2 Current', and 'Phase 3 Current' exhibit strong positive correlations with themselves, as expected, since they represent the same variable in different phases.

* Negative correlations: The voltage features (Phase 1 Voltage, Phase 2 Voltage, and Phase 3 Voltage) show moderate negative correlations with their respective currents.

* Weak correlations: The voltage difference features (1-2 Voltage, 2-3 Voltage, and 3-1 Voltage) exhibit weak correlations with the currents.

* Neutral Current: The neutral current shows moderate to strong correlations with all phase currents. This suggests that the neutral current is more related to the phase currents than to the voltage or voltage differences between phases.
  



Estructura del Proyecto
src/: Códigos fuente en Python.
data/: Datasets utilizados.
results/: Resultados obtenidos, incluyendo figuras, gráficos y tablas.
