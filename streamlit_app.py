import streamlit as st
import pandas as pd

st.title('My Parents new healthy diner')

st.header('Breakfast Menu')

st.text('🐔 Hard Boiled Eggs')
st.text('🥑🍞 Kale + Spinach Sandwich')
st.text('Free Range Egg Omelette')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

st.multiselect("Pick some fruits:", list(my_fruit_list.index))

st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avacado','Strawberries'])

st.dataframe(my_fruit_list)




