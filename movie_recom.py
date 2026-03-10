import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("dataset.csv")

cv = CountVectorizer()
matrix = cv.fit_transform(df["Genre"])

similarity = cosine_similarity(matrix)

def recommend(movie_name):
    index = df[df["Movie"] == movie_name].index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    for i in scores[1:4]:
        print(df.iloc[i[0]].Movie)

recommend("Avatar")