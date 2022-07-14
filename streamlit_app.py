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

fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

st.dataframe(fruits_to_show)

st.header('Fruityvice Fruit Added!')
fruit_choice = st.text_input('What fruit would you like information about?', 'kiwi')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#st.text(fruityvice_response.json())


# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
st.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone() -- Fetch just one row
my_data_row = my_cur.fetchall() ## fetch all rows
#st.text("Hello from Snowflake:")
#st.text("The fruit load list contains:")
st.header("The fruit load list contains:")
#st.text(my_data_row)
st.dataframe(my_data_row)

add_my_fruit = st.text_input('What fruit would you like to add?', 'kiwi')
st.text('',add_my_fruit)
