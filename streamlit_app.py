import streamlit
import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

selected_fruit = streamlit.multiselect("Pick some fruits:", list(my_fruit_list['Fruit']),['Avacado','Strawberries'])
fruits_to_show = my_fruit_list.loc[selected_fruit]
streamlit.dataframe(fruits_to_show)


