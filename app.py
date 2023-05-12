import pandas as pd
import streamlit as st
import plotly_express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Price by Type of vehicle')

fig_a = px.histogram(df, x = ['price'], color = 'type')
st.write(fig_a)

st.header('Price by Model Year of vehicle')

fig_b = px.histogram(df, x = ['price'], color = 'model_year')
st.write(fig_b)

