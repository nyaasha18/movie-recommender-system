import streamlit as st
import pickle
import pandas as pd
import requests
import time
import base64


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=579838c6c47b42beb375ba5de2eafabc&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


@st.cache(suppress_st_warning=True)
def recommend(movie):
    time.sleep(2)
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),
    reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://external-preview.redd.it/Z-mdOCdgw53wluJKQdklW2-WwJEcd3zXoER3YNl-euI.jpg?auto=webp&s=9da2a0406734c547c7bc489c5fa20b091c7ee86c");
             background-size: cover;
             background-color: rgba(225, 225, 225, 0.7);
             background-blend-mode: overlay;
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
set_bg_hack_url()

st.title('NAY DAY')
st.header('**Movie Recommendation System**')
selected_movie_name = st.selectbox(
    'Which is your favorite movie?',
    movies['title'].values)


if st.button('Recommend'):
    names, posters = (recommend(selected_movie_name))

    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(
        10)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])
    with col7:
        st.text(names[6])
        st.image(posters[6])
    with col8:
        st.text(names[7])
        st.image(posters[7])
    with col9:
        st.text(names[8])
        st.image(posters[8])
    with col10:
        st.text(names[9])
        st.image(posters[9])
