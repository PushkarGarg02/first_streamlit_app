import streamlit
import pandas as pd

my_fruit_lists = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.multiselect("Pick some fruits:", list(my_fruit_lists.index))
streamlit.dataframe(my_fruit_lists)


