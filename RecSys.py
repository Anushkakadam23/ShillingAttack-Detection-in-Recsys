# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from surprise import Dataset, Reader
from surprise import SVD, NMF
from surprise import accuracy
from surprise.model_selection import cross_validate, train_test_split, GridSearchCV

# Reading ratings file
ratings = pd.read_csv('ratings.csv', sep=',', encoding='latin-1', usecols=['userId','movieId','rating','timestamp'])

# Reading movies file
movies = pd.read_csv('movies.csv', sep=',', encoding='latin-1', usecols=['movieId','title','genres'])

n_users = ratings.userId.unique().shape[0]
n_movies = ratings.movieId.unique().shape[0]
print('Number of users = ' + str(n_users) + ' | Number of movies = ' + str(n_movies))
#Now we want the format of our ratings matrix to be one row per user and one column per movie.
#To do so, we willl pivot ratings to get that and call the new variable Ratings (with a capital *R).

Ratings = ratings.pivot(index = 'userId', columns ='movieId', values = 'rating').fillna(0)
Ratings.head()
#Last but not least, we need to de-normalize the data (normalize by each users mean) and convert it from a dataframe to a numpy array.

# Load Reader library
reader = Reader()

# Load ratings dataset with Dataset library
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
# Use the SVD algorithm.
svd = SVD()
# Run 5-fold cross-validation and print results
cross_validate(svd, data, measures=["RMSE"], cv=5, verbose=True)

# sample random trainset and testset
# test set is made of 25% of the ratings.
trainset, testset = train_test_split(data, test_size=0.25)
# Train the algorithm on the trainset, and predict ratings for the testset
svd.fit(trainset)
predictions = svd.test(testset)
# Then compute RMSE
accuracy.rmse(predictions)

#We get a mean Root Mean Square Error of 0.87 which is pretty good. Let's now train on the dataset and arrive at predictions.
ratings[ratings['userId'] == 150]
#Now let's use SVD to predict the rating that User with ID 150 will give to a random movie (let's say with Movie ID 1994).
svd.predict(150, 1994)
#For movie with ID 1994, I get an estimated prediction of 3.18210. 
#The recommender system works purely on the basis of an assigned movie ID and tries to predict ratings based on how the other users have predicted the movie.
svd.predict(150, 100)
svd.predict(150, 190)
