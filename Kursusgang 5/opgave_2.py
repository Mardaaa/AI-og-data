import pandas as pd
import os
import matplotlib.pyplot as plt

path = os.path.join(os.path.dirname(__file__), 'recipeData.csv')
df = pd.read_csv(path, encoding='ISO-8859-1', index_col="BeerID")
print(df.head())

"""
Find features that have MV's
"""
print(df.isna().sum())
    # Style, Name, Boilgravity, MashThickness, PitchRate, PrimaryTemp, PrimingMethod, PrimingAmount, UserID

# Drop cols with missing values
df.dropna(axis=1, inplace=True)
print(df.isna().sum())


"""
Find numerical features
"""
print(df.info())
    # Categorical cols: URL, SugarScale, BrewMethod

# Drop categorical columns
df.drop(['URL','SugarScale','BrewMethod'], axis=1, inplace=True)
print(df.columns)


"""
Visualize numerical features
"""
for i in df.columns:
    fig = plt.figure()
    plt.title(f'Histogram of {i}')
    axis = df[i].plot.hist()
    # plt.show()

# print(df['Color'])
