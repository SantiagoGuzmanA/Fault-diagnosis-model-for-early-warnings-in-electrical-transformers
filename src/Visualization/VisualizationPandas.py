import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
from src.Preprocessing.WorkPandas import*
import matplotlib.pyplot as plt
import seaborn as sns
def plot_histograms(df):
    """
    Plots histograms, density plots, boxplots, and violin plots for different variables in the DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.

    Returns:
    None
    """
    df.hist(figsize=(10, 8))
    plt.title('Histograms of each variable')
    plt.tight_layout()
    plt.savefig('results//figures//Histograms of each variable.png',bbox_inches='tight',pad_inches=0.05)
    #plt.show()

    voltage_features = ["Phase 1 Voltage", "Phase 2 Voltage", "Phase 3 Voltage"]
    current_features = ["Phase 1 Current", "Phase 2 Current", "Phase 3 Current"]
    difference_features = ["1-2 Voltage", "2-3 Voltage", "3-1 Voltage"]

    plt.figure(figsize=(20, 10))

    for feature in voltage_features:
        sns.histplot(data=df, x=feature, kde=False, alpha=0.7, label=feature)

    plt.title('Histogram of Phase Voltage')
    plt.xlabel('Voltage')
    plt.ylabel('Frequency')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig('results//figures//Histogram of Phase Voltage.png',bbox_inches='tight',pad_inches=0.05)
    #plt.show()

    plt.figure(figsize=(20, 10))

    for feature in current_features:
        sns.histplot(data=df, x=feature, kde=True, alpha=0.7, label=feature)

    plt.title('Histogram of Phase Current')
    plt.xlabel('Current')
    plt.ylabel('Frequency')
    plt.legend()
    plt.tight_layout()
    plt.savefig('results//figures//Histogram of Phase Current.png',bbox_inches='tight',pad_inches=0.05)
    #plt.show()

    plt.figure(figsize=(20, 10))

    for feature in difference_features:
        sns.kdeplot(data=df, x=feature, fill=True, alpha=0.5,  linewidth=0.5, label=feature)

    plt.title('Histogram of Voltage Differences')
    plt.xlabel('Voltage Difference')
    plt.ylabel('Frequency')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig('results//figures//Histogram of Voltage Differences.png',bbox_inches='tight',pad_inches=0.05)
    #plt.show()

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
    plt.savefig('results//figures//Density Plot of.png',bbox_inches='tight',pad_inches=0.05)
    #plt.show()

    plt.figure(figsize=(15, 5))

    for i, (title, features) in enumerate(feature_groups.items()):
        plt.subplot(1, 3, i + 1)
        sns.boxplot(data=df[features])
        plt.title(f'Boxplot of {title}')
        plt.xlabel(title)
        plt.ylabel('Values')
        plt.xticks(ticks=range(len(features)), labels=features)

    plt.tight_layout()
    plt.savefig('results//figures//Boxplot of.png',bbox_inches='tight',pad_inches=0.05)
    #plt.show()

    plt.figure(figsize=(15, 5))

    for i, (title, features) in enumerate(feature_groups.items()):
        plt.subplot(1, 3, i + 1)
        sns.violinplot(data=df[features], palette='Set2')
        plt.title(f'Violin Plot of {title}')
        plt.xlabel(title)
        plt.ylabel('Values')
        plt.xticks(ticks=range(len(features)), labels=features)

    plt.tight_layout()
    plt.savefig('results//figures//Violin Plot of.png',bbox_inches='tight',pad_inches=0.05)
    #plt.show()