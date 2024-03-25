import pandas as pd
import streamlit as st
import pickle
import requests

def fetch(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2a5066ebbc9c99432e2e34f3f70fabd1'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_list=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_list.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch(movie_id))
    return recommended_list, recommended_movies_posters

movies_list = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title("Movie Recommender System")
selected_movie_name = st.selectbox(
    'Choose the movie',
    movies['title'].values)

if st.button('Recommend similar movies'):
    names, posters=recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(posters[0])
        st.text(names[0])
    with col2:
        st.image(posters[1])
        st.text(names[1])
    with col3:
        st.image(posters[2])
        st.text(names[2])
    with col4:
        st.image(posters[3])
        st.text(names[3])
    with col5:
        st.image(posters[4])
        st.text(names[4])