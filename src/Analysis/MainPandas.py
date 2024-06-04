import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
from src.Preprocessing.WorkPandas import*
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
