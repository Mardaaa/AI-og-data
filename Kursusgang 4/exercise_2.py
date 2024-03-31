import os
import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report


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

def correlation_matrix(df):
    matrix = df.corr()
    sns.heatmap(matrix, cmap="Greens", annot=True)
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

    """Ved style er der flest Cream Ale, men der er rigtig mange unikke værdier.
     For at undgå curse of dimensionality, så fjernes style kolonnen"""
    df.drop('Style', axis='columns',inplace=True)
    print(df.columns)

    ##### Unique values #####
    print(len(df['Name'].unique())) # Der er fucking mange unikke værdier ved name. Det droppes
    df.drop('Name',axis='columns',inplace=True)


    ##### Check correlation of missing values and non-missing #######3
    df_copy = df.copy() # Make a copy of dataframe
    df_copy = df_copy.notnull().astype(int)
    # Confirm it has been done correctly
    # print(df_copy.isnull().sum())
    # print(df_copy.head())
    correlation_matrix(df_copy) # Visualize the correlation matrix


    ##### Visualize histogram of missing values #####
    # visualize_histogram_of_missing_values(df)

    ##### Correlation Matrix #####
    # correlation_matrix_of_missing_values(df)
    """ PrimingMethod og PrimingAmount er positivt correlaterede. De andre har ikke korrelation til hinanden. 
    Dette kan være en indikation på MAR. Der er mange MV af de to. Drop dem"""
    # df.drop(['PrimingMethod','PrimingAmount','UserId'], axis='columns', inplace=True)
    # print(df.info())


    # # ##### Handle missing values #####
    # features = ['PrimaryTemp','PitchRate','MashThickness','BoilGravity']
    # # new_df = mean_missing_values(df, features)
    # new_df = median_missing_values(df, features)
    # print(new_df.isna().sum())

    # # ##### Visualize histogram #####
    # # visualize_histogram(mean_df,'Style')


    # ##### Confirm missing values have been fixed #####
    # # print(new_df.isna().sum())
    # # print(new_df.columns)

    # ##### Check how many unique values the categorical values have #######
    # # print(new_df.info())
    # # print(len(new_df['BrewMethod'].unique())) # There's 4 unique values
    # # print(len(new_df['SugarScale'].unique())) # There's 2 uniquel values
    
    # ##### One-hot encode categorical values #######
    # new_df = pd.get_dummies(new_df, columns=['BrewMethod', 'SugarScale'])
    # print(new_df.info())

    # ###### Split dataset ############3
    # X = new_df.drop('BrewMethod_All Grain', axis=1)
    # y = new_df['BrewMethod_All Grain']

    # X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
    # # print(len(X_train))
    # # print(len(X_test))

    # ############## Train KNN classifier ############
    # knn = KNeighborsClassifier(n_neighbors=10)
    # knn.fit(X_train, y_train)

    # ############## Make predictions ##########
    # predictions = knn.predict(X_test)

    # ############## Visualize CM ############
    # cm = confusion_matrix(y_test, predictions)
    # print(cm)
    # clf_score = classification_report(y_test, predictions)
    # print(clf_score)
    
    # """
    # Der opnås en tand bedre resultater, hvis der benyttes median imputation
    # """



if __name__ == '__main__':
    main()