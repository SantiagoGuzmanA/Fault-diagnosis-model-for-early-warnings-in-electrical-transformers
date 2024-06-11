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
    Realiza la prueba de Shapiro-Wilk para varios grupos de columnas.

    Parameters:
    df (DataFrame): El DataFrame con los datos a probar.
    groups_dict (dict): Un diccionario que mapea los nombres de los grupos a las listas de columnas correspondientes.

    Returns:
    dict: Diccionario anidado con los resultados de la prueba de Shapiro-Wilk para cada grupo y columna.
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
    Realiza el test de Kolmogorov-Smirnov para varios grupos de columnas.

    Parameters:
    df (DataFrame): El DataFrame con los datos a probar.
    groups_dict (dict): Un diccionario que mapea los nombres de los grupos a las listas de columnas correspondientes.
    distribution (str, optional): La distribución a comparar con los datos. Por defecto es 'norm' para distribución normal.

    Returns:
    dict: Diccionario anidado con los resultados del test de Kolmogorov-Smirnov para cada grupo y columna.
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
    Realiza el test de Kruskal-Wallis para comparar varias muestras independientes.

    Parámetros:
    df (DataFrame): El DataFrame que contiene los datos a comparar.
    columns (list): La lista de columnas que representan las muestras a comparar.

    Retorna:
    tuple: Una tupla que contiene el estadístico H y el valor p del test de Kruskal-Wallis.
    """
    columns = groups[group_name]
    h_statistic, p_value = kruskal(*[df[column] for column in columns])
    return h_statistic, p_value

def calculate_fisher_discriminant_ratio(df):
    """
    Calcula el ratio discriminante de Fisher para un DataFrame de datos numéricos.

    Parameters:
    df (DataFrame): El DataFrame que contiene los datos numéricos.

    Returns:
    dict: Un diccionario que contiene el ratio discriminante de Fisher para cada característica.
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
    Calcula los scores AUC para un grupo de características en un DataFrame.

    Parameters:
    df (DataFrame): El DataFrame que contiene los datos.
    features (list): La lista de características a utilizar.
    group_name (str): El nombre del grupo de características.

    Returns:
    list: Una lista de scores AUC para cada característica del grupo.
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
    Calcula el coeficiente de correlación entre las variables numéricas y las variables objetivo.

    Parameters:
    df (DataFrame): El DataFrame que contiene los datos.
    target_variables (list): La lista de variables objetivo para las cuales se calculará la correlación.

    Returns:
    dict: Un diccionario que contiene el coeficiente de correlación de cada variable numérica con cada variable objetivo.
    """
    numeric_columns = df.drop('DeviceTimeStamp', axis=1)
    correlation_results = {}
    for target_variable in target_variables:
        correlation_with_target = numeric_columns.corrwith(df[target_variable])
        correlation_results[target_variable] = correlation_with_target
    return correlation_results

def random_forest_classifier(df):
    """
    Trains a Random Forest Classifier model to predict faults based on phase currents.

    Parameters:
    df (DataFrame): DataFrame containing the dataset with relevant columns.

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
