import streamlit as st
from PIL import Image
import pandas as pd
import random

df = pd.read_csv("/Users/hannahum/PycharmProjects/The Scoop/combined/products.csv")
bj = pd.read_csv("/Users/hannahum/PycharmProjects/The Scoop/bj/bj_products.csv")
breyers = pd.read_csv("/Users/hannahum/PycharmProjects/The Scoop/breyers/breyers_products.csv")
hd = pd.read_csv("/Users/hannahum/PycharmProjects/The Scoop/hd/hd_products.csv")
talenti = pd.read_csv("/Users/hannahum/PycharmProjects/The Scoop/talenti/talenti_products.csv")
reviews = pd.read_csv("/Users/hannahum/PycharmProjects/The Scoop/combined/reviews.csv")
reviews['title'] = reviews['title'].fillna('')

title = st.title('Catalog 🗂️')

def button_control(button_key):
    if button_key not in st.session_state:
        st.session_state[button_key] = False
    return st.session_state[button_key]

def display_ingredients(flavor_index, df):
    ingredients = df['ingredients'].iloc[flavor_index]
    st.write(ingredients)

def default_list():
    st.subheader("Explore All")
    indices_list = []
    for i in range(len(df)):
        indices_list.append(i)
    shuffled_flavors = pd.Series(indices_list).sample(frac=1).reset_index(drop=True)
    for i in range(len(df)):
        if (i == 0):
            st.write("\n \n")
        name = df['name'].iloc[shuffled_flavors[i]]
        st.markdown(f"**__{name}__**", unsafe_allow_html=True)
        key = df['key'].iloc[shuffled_flavors[i]]
        image_path = f"/Users/hannahum/PycharmProjects/The Scoop/combined/images/{key}.png"
        image = Image.open(image_path)
        st.image(image)

        brand = df['brand'].iloc[shuffled_flavors[i]]
        if (brand == "hd"):
            st.write("**Brand:** Häagen-Dazs")
        elif (brand == "bj"):
            st.write("**Brand:** Ben & Jerry's")
        elif (brand == "talenti"):
            st.write("**Brand:** Talenti")
        elif (brand == "breyers"):
            st.write("**Brand:** Breyers")

        rating = df['rating'].iloc[shuffled_flavors[i]]
        st.write(f"**Rating:** {rating}")

        description = df['description'].iloc[shuffled_flavors[i]]
        st.write(f'**Description:** {description}')

        ingredients = df['ingredients'].iloc[shuffled_flavors[i]]
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
    st.write("\n \n")

def brand_page():
    st.subheader("Explore Flavors by Brand")
    bj_button = st.button("Ben & Jerry's")
    breyers_button = st.button("Breyers")
    hd_button = st.button("Häagen-Dazs")
    talenti_button = st.button("Talenti")
    st.write("\n \n")
    if (bj_button):
        st.subheader("Ben & Jerry's")
        for i in range(len(bj)):
            if (i == 0):
                st.write("\n \n")
            name = bj['name'].iloc[i]
            st.write(f"**{name}**")
            key = bj['key'].iloc[i]
            image_path = f"/Users/hannahum/PycharmProjects/The Scoop/bj/bj_images/{key}.png"
            image = Image.open(image_path)
            st.image(image)
            rating = bj['rating'].iloc[i]
            st.write(f"**Rating:** {rating}")
            description = bj['description'].iloc[i]
            st.write(f'**Description:** {description}')
            ingredients = df['ingredients'].iloc[i]
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
        st.write("\n \n")
    if(breyers_button):
        st.subheader("Breyers")
        for i in range(len(breyers)):
            name = breyers['name'].iloc[i]
            st.write(f"**{name}**")
            key = breyers['key'].iloc[i]
            image_path = f"/Users/hannahum/PycharmProjects/The Scoop/breyers/breyers_images/{key}.png"
            image = Image.open(image_path)
            st.image(image)
            rating = breyers['rating'].iloc[i]
            st.write(f"**Rating:** {rating}")
            description = breyers['description'].iloc[i]
            st.write(f'**Description:** {description}')
            ingredients = df['ingredients'].iloc[i]
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
        st.write("\n \n")
    if(hd_button):
        st.subheader("Häagen-Dazs")
        for i in range(len(hd)):
            name = hd['name'].iloc[i]
            st.write(f"**{name}**")
            key = hd['key'].iloc[i]
            image_path = f"/Users/hannahum/PycharmProjects/The Scoop/hd/hd_images/{key}.png"
            image = Image.open(image_path)
            st.image(image)
            rating = hd['rating'].iloc[i]
            st.write(f"**Rating:** {rating}")
            description = hd['description'].iloc[i]
            st.write(f'**Description:** {description}')
            ingredients = df['ingredients'].iloc[i]
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
    if(talenti_button):
        st.subheader("Talenti")
        for i in range(len(talenti)):
            name = talenti['name'].iloc[i]
            st.write(f"**{name}**")
            key = talenti['key'].iloc[i]
            image_path = f"/Users/hannahum/PycharmProjects/The Scoop/talenti/talenti_images/{key}.png"
            image = Image.open(image_path)
            st.image(image)
            rating = talenti['rating'].iloc[i]
            st.write(f"**Rating:** {rating}")
            description = talenti['description'].iloc[i]
            st.write(f'**Description:** {description}')
            ingredients = df['ingredients'].iloc[i]
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
        st.write("\n \n")

def rating_page():
    st.subheader("Explore Flavors by Rating")
    highest_button = st.button("Highest Rated")
    lowest_button = st.button("Lowest Rated")
    st.write("\n \n")
    st.write("\n \n")
    if (highest_button):
        sorted_indices = df.sort_values(by='rating', ascending=False)
        for i in range(len(sorted_indices)):
            name = sorted_indices['name'].iloc[i]
            st.write(f"**{name}**")
            key = sorted_indices['key'].iloc[i]
            image_path = f"/Users/hannahum/PycharmProjects/The Scoop/combined/images/{key}.png"
            image = Image.open(image_path)
            st.image(image)
            brand = sorted_indices['brand'].iloc[i]
            if (brand == "hd"):
                st.write("**Brand:** Häagen-Dazs")
            elif (brand == "bj"):
                st.write("**Brand:** Ben & Jerry's")
            elif (brand == "talenti"):
                st.write("**Brand:** Talenti")
            elif (brand == "breyers"):
                st.write("**Brand:** Breyers")

            rating = sorted_indices['rating'].iloc[i]
            st.write(f"**Rating:** {rating}")
            description = sorted_indices['description'].iloc[i]
            st.write(f'**Description:** {description}')
            ingredients = df['ingredients'].iloc[i]
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
        st.write("\n \n")
    if (lowest_button):
        sorted_indices = df.sort_values(by='rating', ascending=True)
        for i in range(len(sorted_indices)):
            name = sorted_indices['name'].iloc[i]
            st.write(f"**{name}**")
            key = sorted_indices['key'].iloc[i]
            image_path = f"/Users/hannahum/PycharmProjects/The Scoop/ice cream dataset/combined/images/{key}.png"
            image = Image.open(image_path)
            st.image(image)
            brand = sorted_indices['brand'].iloc[i]
            if (brand == "hd"):
                st.write("**Brand:** Häagen-Dazs")
            elif (brand == "bj"):
                st.write("**Brand:** Ben & Jerry's")
            elif (brand == "talenti"):
                st.write("**Brand:** Talenti")
            elif (brand == "breyers"):
                st.write("**Brand:** Breyers")

            rating = sorted_indices['rating'].iloc[i]
            st.write(f"**Rating:** {rating}")
            description = sorted_indices['description'].iloc[i]
            st.write(f'**Description:** {description}')
            ingredients = df['ingredients'].iloc[i]
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
            if (len(rev_authors) >= 3):
                random_indices = random.sample(range(len(rev_authors)), 3)
            for k in range(len(random_indices)):
                st.write(f'**User:** {rev_authors[random_indices[k]]}')
                st.write(f'**Date:** {rev_dates[random_indices[k]]}')
                st.write(f'_{rev_titles[random_indices[k]]}_')
                st.write(f'"{rev_text[random_indices[k]]}"')
                st.write("\n \n")
        st.write("\n \n")
        st.write("\n \n")
        st.write("\n \n")

page = st.sidebar.radio("Ice Cream Products Sorted By:", ("All 🌎", "Brand 📍", "Rating ⭐"))
# Display selected page
if page == "All 🌎":
    default_list()
elif page == "Brand 📍":
    brand_page()
elif page == "Rating ⭐":
    rating_page()
