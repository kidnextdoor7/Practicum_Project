import pandas as pd
import streamlit as st
import plotly_express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Price by Type of vehicle')

show_salvage_cars = st.checkbox('Show Salvage Cars')

if not show_salvage_cars:
    df = df[df.condition!='salvage']

fig_a = px.histogram(df, x = ['price'], color = 'condition')
st.write(fig_a)

st.header('Price by Model Year of vehicle')

fig_b = px.scatter(df, x = ['price'], y = 'model_year')
st.write(fig_b)

