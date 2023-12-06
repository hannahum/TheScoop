import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def craving_recommendations(input):
    descriptions = pd.read_csv("/Users/hannahum/PycharmProjects/The Scoop/ice cream dataset/combined/products.csv")

    # Add new row with user input at the end of the Data Frame
    new_row_data = {
        'brand': [pd.NA],
        'key': [pd.NA],
        'name': [pd.NA],
        'subhead': [pd.NA],
        'description': [input],
        'rating': [pd.NA],
        'rating_count': [pd.NA],
        'ingredients': [pd.NA]
    }
    new_row = pd.DataFrame(new_row_data)
    descriptions = pd.concat([descriptions, new_row], ignore_index=True)

    tfidf = TfidfVectorizer(stop_words='english')
    descriptions['description'] = descriptions['description'].fillna('')
    tfidf_matrix = tfidf.fit_transform(descriptions['description'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(descriptions.index, index=descriptions['description']).drop_duplicates()

    # Get index of the flavor that corresponds to inputted name
    idx = indices[input]

    # Get cosine similarity scores of all flavors with the flavor
    sim_scores = []
    for i in range(len(descriptions)):
        sim_scores.append([i, cosine_sim[i][idx]])

    # Sort flavors based on the similarity scores in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar flavors by slicing it to get elements 1-11 as 0 would be the flavor itself
    sim_scores = sim_scores[1:16]

    # Get the flavor indices
    similar_indices = [i[0] for i in sim_scores]

    # Return top 10 most similar flavors to flavor in question
    return similar_indices

def display_filtered_flavors(df, selected_ingredients):
    filtered_flavors = df[~df['ingredients'].apply(lambda x: any(ingredient in selected_ingredients for ingredient in x))]
    if not filtered_flavors.empty:
        return filtered_flavors

def random_recommendations():
    df = pd.read_csv("/Users/hannahum/PycharmProjects/The Scoop/ice cream dataset/combined/products.csv")
    num_rows = len(df)
    random_indices = [random.randint(0, num_rows - 1) for _ in range(10)]
    return random_indices
