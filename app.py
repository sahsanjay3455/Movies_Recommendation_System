import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=bb54f55eb68a5d3e87a44e4a6da7414c&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in movie_list:
         movie_id = movies.iloc[i[0]].movie_id
         recommended_movie_posters.append(fetch_poster(movie_id))
         recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('welcome to sanjay website movies')
st.title('Movies Recommender System')

selected_movie_name=st.selectbox('Plz choose your movies which you like most',movies['title'].values)

if st.button('Show Recommendation'):
    names,posters= recommend(selected_movie_name)

    col1,col2,col3,col4,col5=st.columns(5)
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


