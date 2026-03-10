# Movie Recommendation System (Python)

## About the Project

This project is a simple movie recommendation system built using Python. The idea is to recommend movies that are similar to a movie selected by the user. Many popular platforms like Netflix and Amazon use recommendation systems to suggest content to users, and this project is a basic attempt to understand how such systems work.

The recommendation in this project is based on **movie genres**. If two movies share similar genres, they are considered similar and may be recommended to the user.

## Technologies Used

- Python
- Pandas
- Scikit-learn

## How the Project Works

1. A dataset containing movie titles and their genres is loaded using **Pandas**.
2. The genre text is converted into numerical form using **CountVectorizer**.
3. **Cosine similarity** is used to calculate how similar the movies are to each other.
4. When a movie is selected, the program finds other movies with the highest similarity score.
5. The top similar movies are displayed as recommendations.

## Example

If the user selects the movie **Avatar**, the system may recommend movies such as:

- Avengers
- Iron Man
- Interstellar

These movies are suggested because they share similar genres.

## How to Run the Project

1. Install the required libraries:

   pip install pandas scikit-learn

2. Run the Python file:

   python movie_recommender.py

3. The program will recommend movies based on similarity.

## Purpose of the Project

The goal of this project was to understand the basic concept of **recommendation systems** and how similarity between items can be calculated using simple machine learning techniques.

This is a beginner-level project created as part of learning Python and basic machine learning concepts.
