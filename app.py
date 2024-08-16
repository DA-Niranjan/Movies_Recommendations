import os
import sys
import streamlit as st 
import pickle
import requests 

movies = pickle.load(open('movies.pkl', 'rb'))
movies_title = movies['title'].values

with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

def fetch_poster(movie_title):
    data = requests.get("http://www.omdbapi.com/?apikey=c9eb1bb2&t={}".format(movie_title))
    # data = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = data.json()
    return data["Poster"]

def recommend(text):
    movies_index = movies[movies["title"] == text].index[0]
    distances = similarity[movies_index]
    closet = sorted(list(enumerate(distances)), reverse=True, key= lambda x : x[1])
    movies_poster = [fetch_poster((movies.iloc[i[0]]['title'])) for i in closet[1:6]]
    movies_names = [(movies.iloc[i[0]]['title']) for i in closet[1:6]]
    return movies_names, movies_poster
    

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
                        "Type or select a movie from the dropdown",
                        movies_title,
                    )

if st.button("Recommend"):
    movies_names, movies_poster = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5, vertical_alignment = "top")

    with col1:
        st.markdown(movies_names[0])
        st.image(movies_poster[0])
        
    with col2:
        st.markdown(movies_names[1])
        st.image(movies_poster[1])
        
    with col3:
        st.markdown(movies_names[2])
        st.image(movies_poster[2])
        
    with col4:
        st.markdown(movies_names[3])
        st.image(movies_poster[3])
        
    with col5:
        st.markdown(movies_names[4])
        st.image(movies_poster[4])
    
    
    # for i in recommendation:
    #     st.write(i)

# st.write("You selected:", option)