import os
import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno
import seaborn as sns


def load_data(file_name):
    try:
        path = os.path.join(os.path.dirname(__file__), f'{file_name}')
    except Exception as e:
        print(f"There has occurred an error: {e}")
    else:
        df = pd.read_csv(path, encoding='ISO-8859-1').set_index('BeerID')
    return df


def visualize_histogram_of_missing_values(df):
    msno.bar(df, figsize=(12, 6), fontsize=12, color='steelblue')
    plt.title('Histogram of values in dataframe')
    plt.show()

def correlation_matrix_of_missing_values(df):
    msno.heatmap(df, figsize=(10,8),fontsize=10)
    plt.show()

def mean_missing_values(df, int_features):
    for feature in int_features:
        df[feature] = df[feature].fillna(df[feature].mean())
    return df

def median_missing_values(df, int_features):
    for feature in int_features:
        df[feature] = df[feature].fillna(df[feature].median())
    return df
    
def visualize_histogram(df, feature):
    plt.figure(figsize=(8, 6))
    plt.hist(df[feature].dropna(), bins=20, color='skyblue', edgecolor='black')  # Drop NaN values before plotting
    plt.title(f'Histogram of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()



def main():
    df = load_data('recipeData.csv')
    print(df['UserId'])

    ##### Drop URL column #####
    df.drop('URL',axis=1, inplace=True)
    print(df.head())


    ##### Find missing values #####
    missing_values = df.isnull().sum()
    print(missing_values)

    ##### Visualize histogram of missing values #####
    # visualize_histogram_of_missing_values(df)

    ##### Correlation Matrix #####
    correlation_matrix_of_missing_values(df)
    """ PrimingMethod og PrimingAmount er positivt correlaterede. De andre har ikke korrelation til hinanden. 
    Dette kan være en indikation på NMAR. Der er mange MV af de to. Drop dem"""
    df.drop(['PrimingMethod','PrimingAmount','UserId'], axis='columns', inplace=True)
    print(df.info())


    # ##### Handle missing values #####
    # features = ['PrimaryTemp','PitchRate','MashThickness','BoilGravity']
    # mean_df = mean_missing_values(df, features)
    # print(mean_df.isna().sum())

    # ##### Visualize histogram #####
    # # visualize_histogram(mean_df,'Style')
    # """Ved style er der flest Cream Ale, men der er rigtig mange unikke værdier.
    #  For at undgå curse of dimensionality, så fjernes style kolonnen"""
    # mean_df.drop('Style', axis='columns',inplace=True)
    # print(mean_df.columns)

    # ##### Unique values #####
    # print(len(mean_df['Name'].unique())) # Der er fucking mange unikke værdier ved name. Det droppes
    # mean_df.drop('Name',axis='columns',inplace=True)

    # ##### Confirm missing values have been fixed #####
    # print(mean_df.isna().sum())
    # print(mean_df.columns)

    # print(mean_df.info())
    # print(len(mean_df['BrewMethod'].unique()))

if __name__ == '__main__':
    main()