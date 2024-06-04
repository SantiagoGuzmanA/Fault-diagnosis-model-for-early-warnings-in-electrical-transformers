from scipy.stats import shapiro
from scipy.stats import kstest
from scipy.stats import kruskal
from sklearn.metrics import roc_auc_score
import numpy as np
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
from src.Visualization.VisualizationPandas import*
from src.Preprocessing.WorkPandas import*
#Shapiro-Wilk Test for Phase Voltages:
shapiro_results = {}
for group, columns in [("Phase Voltages", voltage_features),
                       ("Phase Currents", current_features),
                       ("Voltage Differences", difference_features)]:
    shapiro_results[group] = {}
    for column in columns:
        result = shapiro(dfZeros[column])
        shapiro_results[group][column] = result

for group, results in shapiro_results.items():
    print(f"Shapiro-Wilk Test for {group}:")
    print("\n")
    for column, result in results.items():
        print(f"{column}: W-statistic = {result.statistic}, p-value = {result.pvalue}")
#Shapiro-Wilk Test for Phase Currents:
phase_1_current = dfZeros["Phase 1 Current"]
phase_2_current = dfZeros["Phase 2 Current"]
phase_3_current = dfZeros["Phase 3 Current"]

shapiro_result_phase_1 = shapiro(phase_1_current)
shapiro_result_phase_2 = shapiro(phase_2_current)
shapiro_result_phase_3 = shapiro(phase_3_current)

print("Shapiro-Wilk Test for Phase Currents:")
print("\n")
#print("Shapiro-Wilk Test for phase 1 current: ", shapiro_result_phase_1)
print(f"Phase 1 Current: W-statistic = {shapiro_result_phase_1.statistic}, p-value = {shapiro_result_phase_1.pvalue}")
print(f"Phase 2 Current: W-statistic = {shapiro_result_phase_2.statistic}, p-value = {shapiro_result_phase_2.pvalue}")
print(f"Phase 3 Current: W-statistic = {shapiro_result_phase_3.statistic}, p-value = {shapiro_result_phase_3.pvalue}")
#Kolmogorov-Smirnov Test for Phase Voltages:
ks_results = {}
for group, columns in [("Phase Voltages", voltage_features),
                       ("Phase Currents", current_features),
                       ("Voltage Differences", difference_features)]:
    ks_results[group] = {}
    for column in columns:
        result = kstest(dfZeros[column], 'norm')
        ks_results[group][column] = result

for group, results in ks_results.items():
    print(f"Kolmogorov-Smirnov Test for {group}:")
    for column, result in results.items():
        print(f"{column}: KS-statistic = {result.statistic}, p-value = {result.pvalue}")
#Kruskal-Wallis Test:
h_statistic, p_value = kruskal(dfZeros['Phase 1 Current'], dfZeros['Phase 2 Current'], dfZeros['Phase 3 Current'])

print("Kruskal-Wallis Test:")
print(f"H-statistic: {h_statistic}")
print(f"P-value: {p_value}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference between the groups.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference between the groups.")
#Quantitative separability
#fisher
numeric_columns = dfZeros.drop('DeviceTimeStamp', axis=1)
within_class_covariance = np.cov(numeric_columns, rowvar=False)
within_class_covariance = within_class_covariance.T

overall_mean = numeric_columns.mean()
print('Overall mean of feature j:\n')
print(overall_mean)

between_class_scatter = np.zeros_like(within_class_covariance)
for column in numeric_columns.columns:
    column_data = numeric_columns[column]
    column_mean = column_data.mean()
    n = len(column_data)
    between_class_scatter += n * np.outer((column_mean - overall_mean), (column_mean - overall_mean))

fisher_discriminant_ratio = np.diag(np.dot(np.linalg.inv(within_class_covariance), between_class_scatter))

print('\nFisher Discriminant Ratio:\n')
for i, feature in enumerate(numeric_columns.columns):
    print(f"{feature}: {fisher_discriminant_ratio[i]}")
#AUC
auc_scores = []

def calculate_auc(feature_values, target):
    if len(np.unique(target)) == 1:
        print("Only one class present in the target variable. Skipping AUC calculation.")
        return
    auc_score = roc_auc_score(target, feature_values)
    auc_scores.append(auc_score)

for group_name, group_features in zip(['Voltage', 'Current', 'Difference'],
                                      [voltage_features, current_features, difference_features]):
    print(f"AUC scores for {group_name} features:")
    for feature_name in group_features:
        feature_values = dfZeros[feature_name]
        target = (feature_values > feature_values.mean()).astype(int)
        calculate_auc(feature_values, target)

for group_name, group_features in zip(['Voltage', 'Current', 'Difference'],
                                      [voltage_features, current_features, difference_features]):
    print(f"\nAUC scores for {group_name} features:")
    for feature_name, auc_score in zip(group_features, auc_scores):
        print(f"AUC for {feature_name}: {auc_score}")
#cORRELATION COEFFICIENTE
target_variables = ["Phase 1 Current", "Phase 2 Current", "Phase 3 Current"]

for target_variable in target_variables:

    correlation_with_target = numeric_columns.corrwith(dfZeros[target_variable])

    print("Correlation with target variable '{}':".format(target_variable))
    print(correlation_with_target)
    print()
#Random Forest Classifier
class Column():
  def  __init__(self,df,columnName):
    self.column = df[columnName]
    self.mean = self.column.mean()
    self.mode = self.column.mode()
    self.median = self.column.median()
    self.Q1 = self.column.quantile(0.25)
    self.Q3 = self.column.quantile(0.75)
    self.std = self.column.std()
    self.IQR = self.Q3 - self.Q1
    self.lower_bound = self.mean - self.std
    self.upper_bound = self.mean + self.std

I1N = Column(dfRename,"Phase 1 Current")
I2N = Column(dfRename,"Phase 2 Current")
I3N = Column(dfRename,"Phase 3 Current")

dfRename["Fault"] = ((dfRename["Phase 1 Current"] < I1N.lower_bound) | (dfRename["Phase 1 Current"] > I1N.upper_bound) | (dfRename["Phase 2 Current"] < I2N.lower_bound) | (dfRename["Phase 2 Current"] > I2N.upper_bound) | (dfRename["Phase 3 Current"] < I3N.lower_bound) | (dfRename["Phase 3 Current"] > I3N.upper_bound)).astype(int)

dfRename.head(10)

X = dfRename[["Phase 1 Current", "Phase 2 Current","Phase 3 Current"]]
y = dfRename["Fault"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nModel Accuracy:")
print(accuracy_score(y_test, y_pred))