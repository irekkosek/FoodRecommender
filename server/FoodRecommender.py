# %% [markdown]
# # Tasty Food Recommender

# %% [markdown]
# ## Do stworzenia Tasty Food Recommendera (dalej TFR) użyliśmy następujących bibliotek

# %%
from calendar import c
from doctest import debug
from operator import index
from re import S
from tokenize import String
from typing import Sequence
from h11 import Data
import pandas as pd # praca na bazie danych
import numpy as np # operacje matematyczne
import random as rn # funkcja sample do wybierania losowych rekordów z bazy
import time # obliczenie czasu wykonywania kodu
from pathlib import Path





# # %%
# recipesDatabaseWithNames.describe()

# %% [markdown]
# ## Następnie implementujemy klasę DataProcessing zawierającą metody:
# ### pickSample(x, quantity) - wybiera ze zbioru x losowe rekordy w liczbie quantity i zwraca dwa zbiory: sample oraz restOfDatabase, czyli próbkę i resztę zbioru x (bez próbki)
# ### dropColumns(x, threshold_percentage) - usuwa ze zbioru x kolumny zawierające procent jedynek większy niż zadane threshold_percentage, usuwa kolumny zawierające obiekty (tekst). Zwraca zbiór
# ### normalization(x) - normalizuje zbiór x normalizacją min-max

# %%
class DataProcessing:
    @staticmethod
    def pickSample(x, quantity):
        sample = x.sample(quantity)
        restOfDatabase = x.drop(sample.index)
        
        return sample, restOfDatabase
    
    @staticmethod
    def dropColumns(x, threshold_percentage, debug=False):
        x_without_id = x.select_dtypes(exclude=["object"])
        x_without_id = x_without_id.drop(columns=['id'])

        count_ones = x_without_id.sum()
        percent_ones = count_ones / len(x_without_id)
        
        columns_to_drop = percent_ones[percent_ones > threshold_percentage].index
        print(f'columns to drop: {columns_to_drop}') if debug else None
        x.drop(columns_to_drop, axis=1, inplace=True)
        print(f'x.columns: {len(x.columns)}') if debug else None
        print(f'x.columns: {x.columns}') if debug else None
        return x
    
    @staticmethod
    def normalization(x):
        columnNames = x.columns.tolist()
  
        for column in columnNames:
            data = x.loc[:, column]
            maximum = max(data)
            minimum = min(data)
            for row in range(0, len(x), 1):
                xprim = (x.at[row, column] - minimum)/(maximum - minimum)
                x.at[row, column] = xprim

# %% [markdown]
# ## Implementujemy również klasę SoftSet, zawierającą metody:
# ### meanVector(df) - tworzy wektor średni z wyborów użytkownika poprzez zsumowanie wszystkich elementów z kolumn i podzielenie ich przez długość tych kolumn
# ### addSumsColumn(restOfDatabase, chosenByUser) - tworzy kolumnę sum stworzonych poprzez mnożenie każdego elementu z kolumn restOfDatabase przez wektor meanVector
# ### pickRecommendations(restOfDatabase, chosenByUser, quantity) - zwraca pierwsze kilka rekordów (te z najwyższym wynikiem w kolumnie "sums") w liczbie quantity

# %%
class SoftSet:
    @staticmethod
    def meanVector(df):
        meanVector = []
        for column in df:
            columnValues = df[column].values
            meanVector.append(round(sum(columnValues)/len(columnValues), 2))
        return meanVector
    @staticmethod
    def addSumsColumn(restOfDatabase, chosenByUser):
        meanVector = SoftSet.meanVector(chosenByUser)
        sums = []
        for i in restOfDatabase.values:
            j = 0
            sum = 0
            for element in i:
                sum += element*meanVector[j]
                j += 1
            sums.append(sum)
        return sums
    @staticmethod
    def pickRecommendations(restOfDatabase, chosenByUser, quantity, debug=False):
        restOfDatabase['sums'] = SoftSet.addSumsColumn(restOfDatabase, chosenByUser)
        restOfDatabase = restOfDatabase.sort_values(by="sums", ascending=False)
        if debug:
            return restOfDatabase.iloc[:, :].head(quantity)
        return restOfDatabase.iloc[:, :-1].head(quantity)

# %% [markdown]
# ## Ostatnią klasą jest ShowStatistics, która zawiera metody:
# ### reorderColumns(x) - przesuwa ostatnią kolumnę zbioru na początek
# ### calculateAccuracy(chosenByUser, recommendations) - oblicza dokładność między wektorem średnim z wyborów użytkownika i wektorem średnim z wyborów Recommendera
# ### showVectorPlot(chosenByUser, recommendations) - tworzy wykres pokazując graficznie wektory średnie wyborów użytkownika i Recommendera oraz różnicę między nimi

# %%
class ShowStatistics:
    @staticmethod
    def reorderColumns(x):
        cols = x.columns.tolist()
        cols = cols[-1:] + cols[:-1]
        return x[cols]
    @staticmethod
    def calculateAccuracy(chosenByUser, recommendations):
        meanVector = SoftSet.meanVector(chosenByUser)
        recommendationsSetMeanVector = SoftSet.meanVector(recommendations)
        vector = np.abs(np.subtract(meanVector, recommendationsSetMeanVector))
        acc = sum(vector)/len(vector)
        acc = 1 - acc
        return acc

class FoodRecommender:
    def __init__(self):
        pass
    
    
    def recommend(self, chosenByUser : pd.DataFrame, restOfDatabase : pd.DataFrame,  debug=False) -> pd.Series:
        """
        Recommends items based on user's choices and the remaining database.

        Args:
            chosenByUser (pd.DataFrame): Dataframe containing user's choices with columns like: `id, tags...` .
            restOfDatabase (pd.DataFrame): Dataframe containing the database (does not have to exclude ids contained
            in ChosenByUser). Columns like: `id, tags...` .
            debug (bool, optional): Whether to enable debug mode. Defaults to False.

        Returns:
            pd.Series: Series of strings containing ids the recommended items.
        """
        start_time = time.time()
        # %% [markdown]
        # ## Rozpoczyna się działanie algorytmu

        #drop recepies chosen by user from rest of database
        restOfDatabase.to_csv("restOfDatabase.csv") if debug else None
        chosenByUser.to_csv("chosenByUser.csv") if debug else None
        restOfDatabase = restOfDatabase[~restOfDatabase['id'].isin(chosenByUser['id'])]
        
        restOfDatabaseWithoutIds = restOfDatabase.drop(columns=['id'])
        chosenByUserWithoutIds = chosenByUser.drop(columns=['id'])
 
        restOfDatabaseWithoutIds.to_csv("restOfDatabaseWithoutIds.csv") if debug else None
        chosenByUserWithoutIds.to_csv("chosenByUserWithoutIds.csv") if debug else None
        # %% [markdown]
        # ### Wyszukujemy z reszty zbioru 40 rekordów, które będą naszymi rekomendacjami, wyświetlamy pierwsze 5 rekordów poniżej:

        # %%
        recommendationsWithoutIds = SoftSet.pickRecommendations(restOfDatabaseWithoutIds, chosenByUserWithoutIds, len(restOfDatabaseWithoutIds), debug=debug)
        recommendationsWithoutIds.to_csv("recomendationsWithoutIds.csv") if debug else None

        # %%
        recommendations =  recommendationsWithoutIds.copy()
        recommendations['id'] = restOfDatabase['id']
        recommendations=ShowStatistics.reorderColumns(recommendations)
        recommendations.to_csv("recomendations.csv", index=False) if debug else None

        recommendationsWithoutIds.drop(columns=['sums'], inplace=True)

        # %% [markdown]
        # ### Na koniec obliczamy dokładność rekomendacji porównując średnie wektory ze zbiorów chosenByUser oraz recommendations:
        # %%
        if debug:
            acc = ShowStatistics.calculateAccuracy(chosenByUserWithoutIds, recommendationsWithoutIds)
            print("The accuracy is", round(acc*100, 2), "%")

        # %% [markdown]
        # ### Czas wykonania kodu po całym jednym uruchomieniu to...
        # %%
        if debug:
            end_time = time.time() 
            elapsed_time = end_time - start_time
            print("Code execution time: {:.2f} seconds".format(elapsed_time))
        return recommendations['id']

if __name__ == "__main__":
    pd.set_option('display.max_rows', 10)
    debug = True

    filename="dishes_tags_reworked.csv"
    mod_path = Path(__file__).parent
    dataset_abs_path = (mod_path / filename).resolve()
    recipesDatabase = pd.read_csv(fr'{dataset_abs_path}')

    # %% [markdown]
    # ## Przed rozpoczęciem działania algorytmu TFR tworzymy kopię bazy i usuwamy z niej niepotrzebne kolumny    
    # recipesDatabaseWithNames = recipesDatabase.drop(columns=['id', 'slug', 'video_url', 'thumbnail_url', 'tags', 'cook_time', 'prep_time', 'total_time', 'ratings_negative', 'ratings_positive', 'score', 'protein', 'fat', 'calories', 'sugar', 'carbohydrates', 'fiber'])
    # recipesDatabaseWithNames = recipesDatabase.drop(columns=['id', 'slug', 'video_url', 'thumbnail_url', 'ratings_negative', 'ratings_positive', 'score'])
    recipesDatabaseWithIds = recipesDatabase.drop(columns=["name",'slug', 'video_url', 'thumbnail_url', 'ratings_negative', 'ratings_positive', 'score'])
    print("after dropping columns: ", recipesDatabaseWithIds.columns) if debug else None
    # %% [markdown]
    # ### Najpierw usuwamy kolumny zawierające dane w formacie tekstowym i te zawierające więcej niż 0.3% jedynek i wyświetlamy 5 pierwszych rekordów tego zbioru poniżej:
    recipesDatabaseWithIds=DataProcessing.dropColumns(recipesDatabaseWithIds, 1, debug=debug)

    # %% [markdown]
    # ### Dzielimy zbiór na dwa zbiory chosenByUser, restOfDatabase, przy czym pierwszy jest losową próbką 40 rekordów. Wyświetlamy tenże zbiór poniżej:
    chosenByUser, restOfDatabase = DataProcessing.pickSample(recipesDatabaseWithIds, 40)
    #TODO: input from user instead of random sample
  
  
    recommendations =FoodRecommender().recommend(chosenByUser=chosenByUser, restOfDatabase=restOfDatabase, debug=True)
    chosen_recepies=recipesDatabase[recipesDatabase['id'].isin(chosenByUser['id'])]
    # result=recipesDatabase[recipesDatabase['id'].isin(recommendations)]
    #create empty dataframe result
    # result = pd.DataFrame(columns=recipesDatabase.columns)
    # print("Chosen recepies:")
    # print(chosen_recepies)
    # print("Recommendations:")
    # create dataframe result where id is in order with ids from recommendations
    # recipesDatabase['recommendation_index'] = recipesDatabase['id'].apply(lambda x: recommendations.tolist().index(x) if x in recommendations.tolist() else float('inf'))
    # sorted_recipes = recipesDatabase.sort_values(by='recommendation_index')
    # sorted_recipes = sorted_recipes.reset_index(drop=True)
    # sorted_recipes = sorted_recipes.drop('recommendation_index', axis=1)
    # result = sorted_recipes
    # print(recommendations[:10])
    # print(recommendations[-10:])
    # print(recommendations[0])
    # print( recommendations.to_list().index(recommendations[0]))
    # print(recommendations[recommendations.to_list().index(recommendations[0])])
    # result = recipesDatabase.sort_values(by='id', key=lambda x: recommendations.to_list().index(x) if isinstance(recommendations, pd.Series) else recommendations.tolist().index(x))
    # result=pd.DataFrame(columns=recipesDatabase.columns)
    # result['id'] = recommendations
    # result = result.join(recipesDatabase, on='id')
    # recommendation_index = 0
    # for id in recommendations:
    #     #add row to result
    #     result = result._append(recipesDatabase[recipesDatabase['id']==id], ignore_index = True)
    # print(result)
    # result.to_csv("result.csv", index=False) if debug else None
    #TODO: add sums column to result
# %%
