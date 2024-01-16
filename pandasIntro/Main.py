import pandas as pd

print(pd.__version__)

# Pandas mainly uses 2 data structures: DataFrame and Series:
# a DataFrame has the form of spreadsheet or SQL table
# A series is a 1D array that can hold any data type.

# Alex the analyst lesson:
pd.read_csv(r"/Users/johnpennington/Desktop/Data Analysis/Pandas/countries of the world.csv")
# ^ You add the r at the beginning to specify raw text. It populates the DataFrame with text.
