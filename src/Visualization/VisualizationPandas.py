import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
from src.Preprocessing.WorkPandas import*
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
# #Histogramas
# dfZeros.hist(figsize=(10, 8))
# print("Histograms of each variable:")
# print("\n")
# plt.tight_layout()
# plt.show()
# #Distribution histogram
# voltage_features = ["Phase 1 Voltage", "Phase 2 Voltage", "Phase 3 Voltage"]
# current_features = ["Phase 1 Current", "Phase 2 Current", "Phase 3 Current"]
# difference_features = ["1-2 Voltage", "2-3 Voltage", "3-1 Voltage"]
# plt.figure(figsize=(25, 5))
# for feature in voltage_features:
#     plt.subplot(1, 3, 1)
#     sns.histplot(data=dfZeros, x=feature, kde=False, alpha=0.7, label=feature)
# plt.title('Histogram of Phase Voltage')
# plt.xlabel('Voltage')
# plt.ylabel('Frequency')
# plt.legend(loc='upper left')
# print("Distribution by voltage phase characteristics:")
# print("\n")
# plt.tight_layout()
# plt.show()
# #Distribution histogram by density plot 
# plt.figure(figsize=(25, 5))
# for feature in current_features:
#     plt.subplot(1, 3, 2)
#     sns.histplot(data=dfZeros, x=feature, kde=True, alpha=0.7, label=feature)
# plt.title('Histogram of Phase Current')
# plt.xlabel('Current')
# plt.ylabel('Frequency')
# plt.legend()
# print("Distribution by classes of phase currents with their density plot:")
# print("\n")
# plt.tight_layout()
# plt.show()
# #density plot
# plt.figure(figsize=(25, 5))
# for feature in difference_features:
#     plt.subplot(1, 3, 3)
#     sns.kdeplot(data=dfZeros, x=feature, fill=True, alpha=0.5,  linewidth=0.5, label=feature)
# plt.title('Histogram of Voltage Differences')
# plt.xlabel('Voltage Difference')
# plt.ylabel('Frequency')
# plt.legend(loc='upper left')
# print("Density plot of inter-phase voltages:")
# print("\n")
# plt.tight_layout()
# plt.show()
# #Density plots:
# feature_groups = {
#     'Phase Voltages': ["Phase 1 Voltage", "Phase 2 Voltage", "Phase 3 Voltage"],
#     'Phase Currents': ["Phase 1 Current", "Phase 2 Current", "Phase 3 Current"],
#     'Voltage Differences': ["1-2 Voltage", "2-3 Voltage", "3-1 Voltage"]
# }

# plt.figure(figsize=(25, 5))

# for i, (title, features) in enumerate(feature_groups.items()):
#     plt.subplot(1, 3, i + 1)
#     for feature in features:
#         sns.kdeplot(data=dfZeros, x=feature, fill=True, alpha=0.5, linewidth=0.5, label=feature)
#     plt.title(f'Density Plot of {title}')
#     plt.xlabel('Values')
#     plt.ylabel('Density')
#     plt.legend(loc='upper center')
# print("Density plots:")
# print("\n")
# plt.tight_layout()
# plt.show()
# #Box plots
# plt.figure(figsize=(15, 5))

# for i, (title, features) in enumerate(feature_groups.items()):
#     plt.subplot(1, 3, i + 1)
#     sns.boxplot(data=dfZeros[features])
#     plt.title(f'Boxplot of {title}')
#     plt.xlabel(title)
#     plt.ylabel('Values')
#     plt.xticks(ticks=range(len(features)), labels=features)
# print("Box plots:")
# print("\n")
# plt.tight_layout()
# plt.show()
# #violin
# plt.figure(figsize=(15, 5))

# for i, (title, features) in enumerate(feature_groups.items()):
#     plt.subplot(1, 3, i + 1)
#     sns.violinplot(data=dfZeros[features], palette='Set2')
#     plt.title(f'Violin Plot of {title}')
#     plt.xlabel(title)
#     plt.ylabel('Values')
#     plt.xticks(ticks=range(len(features)), labels=features)
# print("Violin plots:")
# print("\n")
# plt.tight_layout()
# plt.show()
def plot_histograms(df):
    """
    Plots histograms, distribution plots, density plots, boxplots, and violin plots for specified features.

    Parameters:
    df (DataFrame): DataFrame containing the dataset with relevant columns.

    Returns:
    None
    """
    df.hist(figsize=(10, 8))
    plt.title('Histograms of each variable')
    plt.tight_layout()
    plt.show()

    voltage_features = ["Phase 1 Voltage", "Phase 2 Voltage", "Phase 3 Voltage"]
    current_features = ["Phase 1 Current", "Phase 2 Current", "Phase 3 Current"]
    difference_features = ["1-2 Voltage", "2-3 Voltage", "3-1 Voltage"]

    plt.figure(figsize=(25, 5))

    for feature in voltage_features:
        sns.histplot(data=df, x=feature, kde=False, alpha=0.7, label=feature)

    plt.title('Histogram of Phase Voltage')
    plt.xlabel('Voltage')
    plt.ylabel('Frequency')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(25, 5))

    for feature in current_features:
        sns.histplot(data=df, x=feature, kde=True, alpha=0.7, label=feature)

    plt.title('Histogram of Phase Current')
    plt.xlabel('Current')
    plt.ylabel('Frequency')
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(25, 5))

    for feature in difference_features:
        sns.kdeplot(data=df, x=feature, fill=True, alpha=0.5,  linewidth=0.5, label=feature)

    plt.title('Histogram of Voltage Differences')
    plt.xlabel('Voltage Difference')
    plt.ylabel('Frequency')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

    feature_groups = {
        'Phase Voltages': voltage_features,
        'Phase Currents': current_features,
        'Voltage Differences': difference_features
    }

    plt.figure(figsize=(25, 5))

    for i, (title, features) in enumerate(feature_groups.items()):
        plt.subplot(1, 3, i + 1)
        for feature in features:
            sns.kdeplot(data=df, x=feature, fill=True, alpha=0.5, linewidth=0.5, label=feature)
        plt.title(f'Density Plot of {title}')
        plt.xlabel('Values')
        plt.ylabel('Density')
        plt.legend(loc='upper center')

    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(15, 5))

    for i, (title, features) in enumerate(feature_groups.items()):
        plt.subplot(1, 3, i + 1)
        sns.boxplot(data=df[features])
        plt.title(f'Boxplot of {title}')
        plt.xlabel(title)
        plt.ylabel('Values')
        plt.xticks(ticks=range(len(features)), labels=features)

    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(15, 5))

    for i, (title, features) in enumerate(feature_groups.items()):
        plt.subplot(1, 3, i + 1)
        sns.violinplot(data=df[features], palette='Set2')
        plt.title(f'Violin Plot of {title}')
        plt.xlabel(title)
        plt.ylabel('Values')
        plt.xticks(ticks=range(len(features)), labels=features)

    plt.tight_layout()
    plt.show()