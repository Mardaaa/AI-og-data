import os
import pandas as pd


path = os.path.join(os.path.dirname(__name__), 'recipeData.csv')

df = pd.read_csv(path)

print(df.head())