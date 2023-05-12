import pandas as pd
import streamlit as st
import plotly.express as px

st.header('Price by Type of vehicle')

fig = px.histogram(df, x = ['price'], color = 'type')
st.write(fig)