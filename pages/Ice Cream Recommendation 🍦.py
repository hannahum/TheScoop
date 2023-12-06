import streamlit as st
import Recommender
from PIL import Image
import pandas as pd
import random

df = pd.read_csv("/Users/hannahum/PycharmProjects/The Scoop/combined/products.csv")
reviews = pd.read_csv("/Users/hannahum/PycharmProjects/The Scoop/combined/reviews.csv")
reviews['title'] = reviews['title'].fillna('')

title = st.title('Find Your Scoop 🔍')
st.markdown(
    """
    Choose one of the categories to start your search for the scoop just right for you!  
"""
)
st.image('random.png')

def button_control(button_key):
    if button_key not in st.session_state:
        st.session_state[button_key] = False
    return st.session_state[button_key]

def cravings_page():
    st.title("Recommendations by Cravings 💭")
    st.markdown(
        """
        Welcome to Recommendations by Cravings! \n
        Enter your latest cravings below and we'll provide you with ice cream flavors tailored to your taste!
    """
    )
    user_input = st.text_input('')
    if user_input:
        recs = Recommender.craving_recommendations(user_input)
        for i in range(len(recs)):
            if (i == 0):
                st.write("\n \n")
                st.write("\n \n")
            name = df['name'].iloc[recs[i]]
            st.write(f"**{name}**")
            key = df['key'].iloc[recs[i]]
            image_path = f"/Users/hannahum/PycharmProjects/The Scoop/combined/images/{key}.png"
            image = Image.open(image_path)
            st.image(image)
            brand = df['brand'].iloc[recs[i]]
            if (brand == "hd"):
                st.write("**Brand:** Häagen-Dazs")
            elif (brand == "bj"):
                st.write("**Brand:** Ben & Jerry's")
            elif (brand == "talenti"):
                st.write("**Brand:** Talenti")
            elif (brand == "breyers"):
                st.write("**Brand:** Breyers")

            rating = df['rating'].iloc[recs[i]]
            st.write(f"**Rating:** {rating}")

            description = df['description'].iloc[recs[i]]
            st.write(f'**Description:** {description}')

            rev_authors = []
            rev_dates = []
            rev_titles = []
            rev_text = []
            for j in range(len(reviews)):
                if (reviews['key'][j] == key):
                    rev_authors.append(reviews['author'].iloc[j])
                    rev_dates.append(reviews['date'].iloc[j])
                    rev_titles.append(reviews['title'].iloc[j])
                    rev_text.append(reviews['text'].iloc[j])

            review_crav_button_state = button_control('review_crav_button')
            review_crav_button = st.button('View Reviews', key=rev_authors)
            if review_crav_button:
                review_crav_button_state = not review_crav_button_state
            if review_crav_button_state:
                random_indices = random.sample(range(len(rev_authors)), 8)
                for k in range(len(random_indices)):
                    st.write("\n \n")
                    st.write(f'**User:** {rev_authors[random_indices[k]]}')
                    st.write(f'**Date:** {rev_dates[random_indices[k]]}')
                    st.write(f'_{rev_titles[random_indices[k]]}_')
                    st.write(f'"{rev_text[random_indices[k]]}"')
                    st.write("\n \n")
                review_crav_button_state = st.empty()
                review_crav_button = review_crav_button_state.button('Hide Reviews')
            ingredients = df['ingredients'].iloc[recs[i]]
            ingred_crav_button_state = button_control('ingred_crav_button')
            ingred_crav_button = st.button('View Ingredients', key=recs[i])
            if ingred_crav_button:
                ingred_crav_button_state = not ingred_crav_button_state
            if ingred_crav_button_state:
                st.write(ingredients)
            st.write("\n \n")
            st.write("\n \n")

def diet_restrictions_page():
    st.title("Recommendations by Dietary Restrictions 📋")
    st.markdown(
        """
        Welcome to Recommendations by Dietary Restrictions! \n
        Enter your dietary restrictions below and we'll find the perfect scoop for you!
    """
    )
    df['ingredients'] = df['ingredients'].apply(lambda x: [ingredient.strip() for ingredient in x.split(',')])
    selected_options = st.multiselect('Select Dietary Restrictions:', df['ingredients'].explode().unique())

    with st.expander("Filtered Flavors"):
        filtered_flavors = Recommender.display_filtered_flavors(df, selected_options)
        if filtered_flavors is not None and not filtered_flavors.empty:
            for index, row in filtered_flavors.iterrows():
                name = row['name']
                st.subheader(f"**{name}**")
                key = row['key']
                image_path = f"/Users/hannahum/PycharmProjects/The Scoop/combined/images/{key}.png"
                image = Image.open(image_path)
                st.image(image)

                brand = row['brand']
                if (brand == "hd"):
                    st.write("**Brand:** Häagen-Dazs")
                elif (brand == "bj"):
                    st.write("**Brand:** Ben & Jerry's")
                elif (brand == "talenti"):
                    st.write("**Brand:** Talenti")
                elif (brand == "breyers"):
                    st.write("**Brand:** Breyers")

                rating = row['rating']
                st.write(f"**Rating:** {rating}")

                description = row['description']
                st.write(f'**Description:** {description}')

                ingredients = row['ingredients']
                st.write(f'**Ingredients:** {ingredients}')
        else:
            st.write("No matching flavors found.")

def random_page():
    st.title("Random Recommendations 🎲")
    st.markdown(
        """
        Welcome to Random Recommendations! \n
        Click 'Generate' to explore new flavors!
    """
    )
    generate = st.button('Generate')
    if generate:
        recs = Recommender.random_recommendations()
        for i in range(len(recs)):
            if (i == 0):
                st.write("\n \n")
                st.write("\n \n")
            name = df['name'].iloc[recs[i]]
            st.write(f"**{name}**")
            key = df['key'].iloc[recs[i]]
            image_path = f"/Users/hannahum/PycharmProjects/The Scoop/combined/images/{key}.png"
            image = Image.open(image_path)
            st.image(image)

            brand = df['brand'].iloc[recs[i]]
            if (brand == "hd"):
                st.write(f'**Brand:** Häagen-Dazs')
            elif (brand == "bj"):
                st.write(f"**Brand:** Ben & Jerry's")
            elif (brand == "talenti"):
                st.write(f'**Brand:** Talenti')
            elif (brand == "breyers"):
                st.write(f'**Brand:** Breyers')

            rating = df['rating'].iloc[recs[i]]
            st.write(f"**Rating:** {rating}")

            description = df['description'].iloc[recs[i]]
            st.write(description)

            ingredients = df['ingredients'].iloc[recs[i]]
            st.write(f'**Ingredients:** {ingredients}')

            st.write(f'**Reviews:** \n')
            rev_authors = []
            rev_dates = []
            rev_titles = []
            rev_text = []
            for j in range(len(reviews)):
                if (reviews['key'][j] == key):
                    rev_authors.append(reviews['author'].iloc[j])
                    rev_dates.append(reviews['date'].iloc[j])
                    rev_titles.append(reviews['title'].iloc[j])
                    rev_text.append(reviews['text'].iloc[j])
            random_indices = random.sample(range(len(rev_authors)), 3)
            for k in range(len(random_indices)):
                st.write(f'**User:** {rev_authors[random_indices[k]]}')
                st.write(f'**Date:** {rev_dates[random_indices[k]]}')
                st.write(f'_{rev_titles[random_indices[k]]}_')
                st.write(f'"{rev_text[random_indices[k]]}"')
                st.write("\n \n")
            st.write("\n \n")
            st.write("\n \n")

# Sidebar navigation
page = st.sidebar.radio("Find Your Scoop Based On:", ("Cravings 💭", "Dietary Restrictions 📋", "Random 🎲"))

# Display selected page
if page == "Cravings 💭":
    cravings_page()
elif page == "Dietary Restrictions 📋":
    diet_restrictions_page()
elif page == "Random 🎲":
    random_page()
