# %% [markdown]
# # Tasty Food Recommender

# %% [markdown]
# ## Do stworzenia Tasty Food Recommendera (dalej TFR) użyliśmy następujących bibliotek

# %%
import pandas as pd # praca na bazie danych
import numpy as np # operacje matematyczne
import random as rn # funkcja sample do wybierania losowych rekordów z bazy
import matplotlib.pyplot as plt # wykresy
import seaborn as sns # wykresy
import time # obliczenie czasu wykonywania kodu

pd.set_option('display.max_rows', 10)

# %%
start_time = time.time()

# %% [markdown]
# ## Przed rozpoczęciem działania algorytmu TFR tworzymy kopię bazy i usuwamy z niej niepotrzebne kolumny

# %%
recipesDatabase = pd.read_csv(r"dishes_with_mapped_tags.csv")
recipesDatabaseWithNames = recipesDatabase.drop(columns=['index', 'id_', 'slug', 'video_url', 'thumbnail_url', 'tags', 'cook_time', 'prep_time', 'total_time', 'ratings_negative', 'ratings_positive', 'score', 'protein', 'fat', 'calories', 'sugar', 'carbohydrates', 'fiber'])

# %% [markdown]
# ### Oczyszczona baza prezentuje się następująco

# %%
recipesDatabaseWithNames.head()

# %%
recipesDatabaseWithNames.describe()

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
    def dropColumns(x, threshold_percentage):
        x = x.select_dtypes(exclude=["object"])
        count_ones = x.sum()
        percent_ones = count_ones / len(x)
        
        columns_to_drop = percent_ones[percent_ones > threshold_percentage].index
        x_dropped = x.drop(columns_to_drop, axis=1)

        return x_dropped
    
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
    def pickRecommendations(restOfDatabase, chosenByUser, quantity):
        restOfDatabase['sums'] = SoftSet.addSumsColumn(restOfDatabase, chosenByUser)
        restOfDatabase = restOfDatabase.sort_values(by="sums", ascending=False)
        
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
    @staticmethod
    def showVectorPlot(chosenByUser, recommendations):
        meanVector = SoftSet.meanVector(chosenByUser)
        recommendationsSetMeanVector = SoftSet.meanVector(recommendations)
        vector = np.abs(np.subtract(meanVector, recommendationsSetMeanVector))

        # Data for meanVector
        x = np.arange(0, len(meanVector))
        y_mean = np.array(meanVector)

        # Data for validatingSetMeanVector
        y_validating = np.array(recommendationsSetMeanVector)
        
        y_vector = np.array(vector)
        
        sns.reset_orig()

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.title("User choices vs TFR recommendations")
        plt.xlabel("Number of categories")
        plt.ylabel("Sums")
        plt.ylim(0, 1)
        plt.plot(x, y_mean, color="#ff7f0e", linestyle='dashed', label="User choices")
        plt.plot(x, y_validating, color="#2ca02c", linestyle='dashed', label="TFR recommendations")
        plt.plot(x, y_vector, color="#1f77b4", label="absolute")
        plt.legend()
        plt.show()

# %% [markdown]
# ### Najpierw usuwamy kolumny zawierające dane w formacie tekstowym i te zawierające więcej niż 3% jedynek i wyświetlamy 5 pierwszych rekordów tego zbioru poniżej:

# %%
df = recipesDatabaseWithNames.copy()
df = DataProcessing.dropColumns(df, 0.03)
df.head()

# %% [markdown]
# ## Rozpoczyna się działanie algorytmu

# %% [markdown]
# ### Dzielimy zbiór na dwa zbiory chosenByUser, restOfDatabase, przy czym pierwszy jest losową próbką 40 rekordów. Wyświetlamy tenże zbiór poniżej:

# %%
chosenByUser, restOfDatabase = DataProcessing.pickSample(df, 40)

# %%
chosenByUserWithNames = chosenByUser.copy()
chosenByUserWithNames['name'] = recipesDatabaseWithNames['name']
print("Recipes chosen by the user:")
ShowStatistics.reorderColumns(chosenByUserWithNames).head()

# %% [markdown]
# ### Wyszukujemy z reszty zbioru 40 rekordów, które będą naszymi rekomendacjami, wyświetlamy pierwsze 5 rekordów poniżej:

# %%
recommendations = SoftSet.pickRecommendations(restOfDatabase, chosenByUser, 40)

# %%
recommendationsWithNames = recommendations.copy()
recommendationsWithNames['name'] = recipesDatabaseWithNames['name']
print("Recipes chosen by the recommender:")
ShowStatistics.reorderColumns(recommendationsWithNames).head()

# %% [markdown]
# ### Na koniec obliczamy dokładność rekomendacji porównując średnie wektory ze zbiorów chosenByUser oraz recommendations:

# %%
acc = ShowStatistics.calculateAccuracy(chosenByUser, recommendations)
print("The accuracy is", round(acc*100, 2), "%")

# %% [markdown]
# ### Dodatkowo tworzymy jeszcze wykres ukazujący porównanie wyborów użytkownika z TFR:

# %%
ShowStatistics.showVectorPlot(chosenByUser, recommendations)

# %% [markdown]
# ### Czas wykonania kodu po całym jednym uruchomieniu to...

# %%
end_time = time.time()
elapsed_time = end_time - start_time
print("Code execution time: {:.2f} seconds".format(elapsed_time))


