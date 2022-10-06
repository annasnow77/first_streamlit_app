import streamlit

streamlit.title('My Parents New Healthy Dajner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range-Eggs')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# add a pick list for the fruits in smoothie
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display Fruit table
streamlit.dataframe(fruits_to_show)

#display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "apple")


#take json reponse and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output as table
streamlit.dataframe(fruityvice_normalized)
