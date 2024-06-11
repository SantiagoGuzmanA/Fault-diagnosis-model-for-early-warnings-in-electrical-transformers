import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
from src.Preprocessing.WorkPandas import*
from src.Analysis.AnalysisPandas import*

file_path = "DatosMonitoringTransformer.txt"
df, dfRename, dfZeros = process_transformer_data(file_path)
groups = {
        "Phase Voltages": ["Phase 1 Voltage", "Phase 2 Voltage", "Phase 3 Voltage"],
        "Phase Currents": ["Phase 1 Current", "Phase 2 Current", "Phase 3 Current"],
        "Voltage Differences": ["1-2 Voltage", "2-3 Voltage", "3-1 Voltage"]
    }
#import Dataframe 
print("Here we can see a summary of the information in the dataframe: \n")
df.info()
#Rename columns
print("Here we can see a summary of the dataframe information but now with the modified column names: \n")
dfRename.info()
print("\n")
print("Viewing the first rows of the DataFrame as a table: \n")
print(dfRename.head(10))
#Delete zeros
print("Here we can see a summary of the information in the dataframe after removing the rows with zeros: \n")
dfZeros.info()
print("\n")
print("Viewing the first rows of the DataFrame with zeros as a table: \n")
print(dfZeros.head(10))
#statistics
print("Summary of statistics:")
print("\n")
print(dfZeros.describe())
#Shapiro-Wilk Test for Phase Currents:
shapiro_results = shapiro_tests(dfZeros, groups)
for group, results in shapiro_results.items():
        print(f"Shapiro-Wilk Test for {group}:")
        print("\n")
        for column, result in results.items():
            print(f"{column}: W-statistic = {result.statistic}, p-value = {result.pvalue}")
#Kolmogorov-Smirnov Test for Phase Voltages:
ks_results = kstest_multiple_groups(dfZeros, groups, 'norm')
for group, results in ks_results.items():
        print(f"Kolmogorov-Smirnov Test for {group}:")
        for column, result in results.items():
            print(f"{column}: KS-statistic = {result.statistic}, p-value = {result.pvalue}")
#Kruskal-Wallis Test:    
group_name = "Phase Currents"      
h_statistic, p_value = kruskal_wallis_test(dfZeros, groups, group_name)
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
fisher_ratios = calculate_fisher_discriminant_ratio(dfZeros)
print('\nFisher Discriminant Ratio:\n')
for feature, ratio in fisher_ratios.items():
    print(f"{feature}: {ratio}")
#AUC
for group_name, group_features in groups.items():
        print(f"AUC scores for {group_name} features:")
        auc_scores = calculate_auc_scores(dfZeros, group_features, group_name)
        for feature_name, auc_score in zip(group_features, auc_scores):
            print(f"AUC for {feature_name}: {auc_score}")
#correlation
target_variables = ["Phase 1 Current", "Phase 2 Current", "Phase 3 Current"]
correlation_results = calculate_correlation_with_target(dfZeros, target_variables)
for target_variable, correlation_with_target in correlation_results.items():
    print("Correlation with target variable '{}':".format(target_variable))
    print(correlation_with_target)
    print()
#Random Forest Classifier
random_forest_classifier(dfRename)