import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel

#Reading the Movies dataset file
movies = pd.read_csv('tmdb_5000_movies.csv')

movies = movies[movies['overview'].notna()]

movies = movies.drop(['production_companies','production_countries','release_date','spoken_languages','status','genres','id','budget','homepage','tagline','keywords','original_language','title'],axis=1)

movies['original_title'] = movies['original_title'].apply(lambda x:x.lower())
tfidf = TfidfVectorizer(min_df=3,ngram_range=(1,3),analyzer='word',stop_words='english')
tf_matrix = tfidf.fit_transform(movies['overview'])
sgm = sigmoid_kernel(tf_matrix,tf_matrix)
indices = pd.Series(movies.index,index=movies['original_title']).drop_duplicates()

def recommend(name,sig=sgm):
    idx = indices[name]
    movie_scores = list(enumerate(sig[idx]))
    movie_scores = sorted(movie_scores,key = lambda x:x[1],reverse=True)
    top_10_similar_movies_indices = movie_scores[1:11]
    movies_indices = [i[0] for i in top_10_similar_movies_indices]
    return movies['original_title'].iloc[movies_indices]
