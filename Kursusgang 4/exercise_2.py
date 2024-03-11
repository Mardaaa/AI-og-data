import os
import pandas as pd


def load_data(file_name):
    try:
        path = os.path.join(os.path.dirname(__file__), f'{file_name}')
    except Exception as e:
        print(f"There has occurred an error: {e}")
    else:
        df = pd.read_csv(path, encoding='ISO-8859-1').set_index('BeerID')
    return df


    


def main():
    df = load_data('recipeData.csv')
    
    ##### Drop URL column #####
    df.drop('URL',axis=1, inplace=True)
    print(df.head())


    ##### Find missing values #####
    missing_values = df.isnull().sum()
    print(missing_values)

if __name__ == '__main__':
    main()