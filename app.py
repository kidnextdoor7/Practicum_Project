import pandas as pd
import streamlit as st
import plotly_express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Price by Type of vehicle')

fig = px.histogram(df, x = ['price'], color = 'type')
st.write(fig)