import streamlit as st 
import pandas as pd
import pickle
import requests

#function to fetch posters for movies
def movie_poster(movie_id):
     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=4381838f8cbc45c5bc27256b84720b0d&language=en-US'.format(movie_id))
     posters = response.json()
     poster_path ='http://image.tmdb.org/t/p/w500/'+ posters['poster_path']
     return  poster_path

#function for recommending movies
def recommend(movie):
    index = movie_df[movie_df['title']==movie].index[0]
    distance = similarity[index]
    movie_list = sorted(list(enumerate(distance)),reverse =True, key=(lambda x: x[1]))
    recommended_movie=[]
    poster=[]
    for i in movie_list[1:6]:
         movie_id=movie_df.iloc[i[0]].movie_id
         recommended_movie.append(movie_df.iloc[i[0]].title)
         poster.append(movie_poster(movie_id))
    return recommended_movie,poster


st.title('Movie Recommendation System')

movies_dictionary=pickle.load(open('movie.pkl','rb'))
movie_df = pd.DataFrame(movies_dictionary)
similarity =pickle.load(open('similarity.pkl','rb'))

selected_movie = st.selectbox(
     'Select a movie from the given list',movie_df['title'].values)

st.write('You selected:', selected_movie)

if st.button('Recommended movies:'):
     movie_name,posters=recommend(selected_movie)
     col1, col2, col3,col4,col5 = st.columns(5)

     with col1:
          st.text(movie_name[0])
          st.image(posters[0])
     with col2:
          st.text(movie_name[1])
          st.image(posters[1])
     with col3:
          st.text(movie_name[2]) 
          st.image(posters[2])

     with col4:
          st.text(movie_name[3])
          st.image(posters[3])

     with col5:
          st.text(movie_name[4])
          st.image(posters[4])

     
     










































# """ import base64
# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
#         background-size: cover
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
#     )
# add_bg_from_local('bg.jpg')  
#  """
