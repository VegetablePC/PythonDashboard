import streamlit as st
import pandas as pd
import plotly.express as px

data1 = pd.read_csv("crimestormQ.csv")
data2 = pd.read_csv("crimenostormQ.csv")

fig1 = px.line(data1, x="Date", y="Loss")
fig2 = px.line(data2, x="Date", y="Loss")

st.subheader("Claims During Storms")
st.plotly_chart(fig1)

st.subheader("Claims During Clear Weather")
st.plotly_chart(fig2)
