import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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

st.header('Fruityvice Fruit Advice!')

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    
    return fruityvice_normalized

try:
    fruit_choice = st.text_input('What fruit would you like information about?')
    if not fruit_choice:
       st.error("Please select a fruit to get information")
    else:
       
       back_from_function = (get_fruityvice_data(fruit_choice))
       st.dataframe(back_from_function)
        
except URLError as e:
  st.error()
      
#st.stop()

st.header("View our Fruit List - Add your favorites")

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()
    
    
    
if st.button('Get fruit load list'):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone() -- Fetch just one row
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    st.dataframe(my_data_rows)
#st.text("Hello from Snowflake:")
#st.text("The fruit load list contains:")


#st.text(my_data_row)




#my_cur.execute("INSERT INTO fruit_load_list values ('from streamlit')")

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('"+ new_fruit +"')")
        return "Thanks for adding " + new_fruit
    
add_my_fruit = st.text_input('What fruit would you like to add?')
if st.button('Add a fruit to the list'):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    back_from_ins_function = insert_row_snowflake(add_my_fruit)
    my_cnx.close()
    st.text(back_from_ins_function)
