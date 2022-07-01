import streamlit as st
import pandas as pd

st.title('My Parents new healthy diner')

st.header('Breakfast Menu')

st.text('🐔 Hard Boiled Eggs')
st.text('🥑🍞 Kale + Spinach Sandwich')
st.text('Free Range Egg Omelette')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

st.dataframe(my_fruit_list)


