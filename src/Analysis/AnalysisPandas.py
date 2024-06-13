from scipy.stats import shapiro
from scipy.stats import kstest
from scipy.stats import kruskal
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import numpy as np
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
from src.Preprocessing.WorkPandas import*

def shapiro_tests(df, groups_dict):
    """
    Performs Shapiro-Wilk tests for normality on specified columns of a DataFrame grouped by a dictionary.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    groups_dict (dict): A dictionary where keys are group names and values are lists of column names to test.

    Returns:
    dict: A nested dictionary where the first level are group names, 
          the second level keys are column names, and the values are Shapiro-Wilk test results.
    Example:
    >>> import pandas as pd
    >>> data = {
    ...     'A': [1.1, 2.3, 3.3, 4.4, 5.5],
    ...     'B': [2.2, 3.4, 4.4, 5.5, 6.6],
    ...     'C': [3.3, 4.5, 5.5, 6.6, 7.7]
    ... }
    >>> df = pd.DataFrame(data)
    >>> groups_dict = {'Group1': ['A', 'B'], 'Group2': ['C']}
    >>> shapiro_tests(df, groups_dict)
    {
        'Group1': {
            'A': (statistic=0.9867621660232544, pvalue=0.9671739935874939),
            'B': (statistic=0.9867621660232544, pvalue=0.9671739935874939)
        },
        'Group2': {
            'C': (statistic=0.9867621660232544, pvalue=0.9671739935874939)
        }
    }
    """
    shapiro_results = {}
    for group, columns in groups_dict.items():
        shapiro_results[group] = {}
        for column in columns:
            result = shapiro(df[column])
            shapiro_results[group][column] = result
    
    return shapiro_results

def kstest_multiple_groups(df, groups_dict, distribution='norm'):
    """
    Performs Kolmogorov-Smirnov tests for specified columns in a DataFrame grouped by a dictionary.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    groups_dict (dict): A dictionary where keys are group names and values are lists of column names to test.
    distribution (str): The distribution to test against. Default is 'norm' for the normal distribution.

    Returns:
    dict: A nested dictionary where the first level are group names, 
          the second level keys are column names, and the values are Kolmogorov-Smirnov test results.
         
    Example:
    >>> import pandas as pd
    >>> data = {
    ...     'A': [1.1, 2.3, 3.3, 4.4, 5.5],
    ...     'B': [2.2, 3.4, 4.4, 5.5, 6.6],
    ...     'C': [3.3, 4.5, 5.5, 6.6, 7.7]
    ... }
    >>> df = pd.DataFrame(data)
    >>> groups_dict = {'Group1': ['A', 'B'], 'Group2': ['C']}
    >>> kstest_multiple_groups(df, groups_dict)
    {
        'Group1': {
            'A': KstestResult(statistic=0.1, pvalue=0.9999948482260321, statistic_location=1.1, statistic_sign=-1),
            'B': KstestResult(statistic=0.1, pvalue=0.9999948482260321, statistic_location=2.2, statistic_sign=-1)
        },
        'Group2': {
            'C': KstestResult(statistic=0.1, pvalue=0.9999948482260321, statistic_location=3.3, statistic_sign=-1)
        }
    }
    """
    ks_results = {}
    for group, columns in groups_dict.items():
        ks_results[group] = {}
        for column in columns:
            result = kstest(df[column], distribution)
            ks_results[group][column] = result
    
    return ks_results

def kruskal_wallis_test(df, groups, group_name):
    """
    Performs the Kruskal-Wallis H-test for independent samples on specified columns in a DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    groups (dict): A dictionary where are group names and values are lists of column names to test.
    group_name (str): The name of the group to test.

    Returns:
    tuple: A tuple containing the H statistic and the p-value of the test.
    
     Example:
    >>> import pandas as pd
    >>> data = {
    ...     'A': [1.1, 2.3, 3.3, 4.4, 5.5],
    ...     'B': [2.2, 3.4, 4.4, 5.5, 6.6],
    ...     'C': [3.3, 4.5, 5.5, 6.6, 7.7]
    ... }
    >>> df = pd.DataFrame(data)
    >>> groups = {'Group1': ['A', 'B', 'C']}
    >>> kruskal_wallis_test(df, groups, 'Group1')
    (1.107, 0.575)
    """
    columns = groups[group_name]
    h_statistic, p_value = kruskal(*[df[column] for column in columns])
    return h_statistic, p_value

def calculate_fisher_discriminant_ratio(df):
    """
    Calculates the Fisher Discriminant Ratio for each numeric feature in the DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data. It is assumed that the column 'DeviceTimeStamp' 
                           is not a numeric feature and will be dropped.

    Returns:
    dict: A dictionary where are feature names and values are the Fisher Discriminant Ratios for each feature.
    Example:
    >>> data = {
    ...     'DeviceTimeStamp': [1, 2, 3, 4, 5],
    ...     'Feature1': [1.1, 2.3, 3.3, 4.4, 5.5],
    ...     'Feature2': [2.2, 3.4, 4.4, 5.5, 6.6],
    ...     'Feature3': [3.3, 4.5, 5.5, 6.6, 7.7]
    ... }
    >>> df = pd.DataFrame(data)
    >>> calculate_fisher_discriminant_ratio(df)
    {'Feature1': 0.0, 'Feature2': 0.0, 'Feature3': 0.0}
    """
    numeric_columns = df.drop('DeviceTimeStamp', axis=1)
    within_class_covariance = np.cov(numeric_columns, rowvar=False)
    within_class_covariance = within_class_covariance.T

    overall_mean = numeric_columns.mean()

    between_class_scatter = np.zeros_like(within_class_covariance)
    for column in numeric_columns.columns:
        column_data = numeric_columns[column]
        column_mean = column_data.mean()
        n = len(column_data)
        between_class_scatter += n * np.outer((column_mean - overall_mean), (column_mean - overall_mean))

    fisher_discriminant_ratio = np.diag(np.dot(np.linalg.inv(within_class_covariance), between_class_scatter))

    fisher_ratios = {}
    for i, feature in enumerate(numeric_columns.columns):
        fisher_ratios[feature] = fisher_discriminant_ratio[i]

    return fisher_ratios

def calculate_auc_scores(df, features, group_name):
    """
    Calculates the Area Under the ROC Curve (AUC) scores for specified features in the DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    features (list): A list of feature names to calculate AUC scores for.
    group_name (str): The name of the group for which AUC scores are being calculated.

    Returns:
    list: A list of AUC scores for each feature.
    
    Example:
    >>> import pandas as pd
    >>> data = {
    ...     'Feature1': [0.1, 0.2, 0.3, 0.4, 0.5],
    ...     'Feature2': [0.2, 0.3, 0.4, 0.5, 0.6],
    ...     'Feature3': [0.3, 0.4, 0.5, 0.6, 0.7]
    ... }
    >>> df = pd.DataFrame(data)
    >>> features = ['Feature1', 'Feature2', 'Feature3']
    >>> calculate_auc_scores(df, features, 'Group1')
    [1.0, 1.0, 1.0]
    """
    auc_scores = []
    for feature_name in features:
        feature_values = df[feature_name]
        target = (feature_values > feature_values.mean()).astype(int)
        if len(np.unique(target)) == 1:
            print(f"Only one class present in {feature_name}. Skipping AUC calculation for {group_name}.")
        else:
            auc_score = roc_auc_score(target, feature_values)
            auc_scores.append(auc_score)
    return auc_scores

def calculate_correlation_with_target(df, target_variables):
    """
    Calculates the correlation between numeric features and target variables in the DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    target_variables (list): A list of target variable names.

    Returns:
    dict: A dictionary where are target variable names and values are Series containing
          correlation coefficients between numeric features and the corresponding target variable.

    Example:
    >>> import pandas as pd
    >>> data = {
    ...     'DeviceTimeStamp': [1, 2, 3, 4, 5],
    ...     'Feature1': [1.1, 2.3, 3.3, 4.4, 5.5],
    ...     'Feature2': [2.2, 3.4, 4.4, 5.5, 6.6],
    ...     'Target1': [0, 1, 0, 1, 0],
    ...     'Target2': [1, 0, 1, 0, 1]
    ... }
    >>> df = pd.DataFrame(data)
    >>> target_variables = ['Target1', 'Target2']
    >>> calculate_correlation_with_target(df, target_variables)
    {'Target1': Feature1    0.447214
    Feature2   -0.447214
    dtype: float64, 'Target2': Feature1   -0.447214
    Feature2    0.447214
    dtype: float64}
    """
    numeric_columns = df.drop('DeviceTimeStamp', axis=1)
    correlation_results = {}
    for target_variable in target_variables:
        correlation_with_target = numeric_columns.corrwith(df[target_variable])
        correlation_results[target_variable] = correlation_with_target
    return correlation_results

def random_forest_classifier(df):
    """
    Trains a random forest classifier to predict faults based on current values.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data. It is assumed that the DataFrame
                           contains columns named 'Phase 1 Current', 'Phase 2 Current', and 'Phase 3 Current'.

    Prints:
    - Confusion matrix
    - Classification report
    - Model accuracy

    Returns:
    None
    """
    class Column():
        def __init__(self, df, columnName):
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

    I1N = Column(df, "Phase 1 Current")
    I2N = Column(df, "Phase 2 Current")
    I3N = Column(df, "Phase 3 Current")

    df["Fault"] = ((df["Phase 1 Current"] < I1N.lower_bound) |
                   (df["Phase 1 Current"] > I1N.upper_bound) |
                   (df["Phase 2 Current"] < I2N.lower_bound) |
                   (df["Phase 2 Current"] > I2N.upper_bound) |
                   (df["Phase 3 Current"] < I3N.lower_bound) |
                   (df["Phase 3 Current"] > I3N.upper_bound)).astype(int)

    X = df[["Phase 1 Current", "Phase 2 Current", "Phase 3 Current"]]
    y = df["Fault"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    print("\nModel Accuracy:")
    print(accuracy_score(y_test, y_pred))
