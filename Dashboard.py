import streamlit as st
import pandas as pd
import plotly.express as px

data1 = pd.read_csv("crimestormQ.csv")
data2 = pd.read_csv("crimenostormQ.csv")

st.title("Crimes during storms and clear weather")

st.dataframe(data1)
st.dataframe(data2)

barfig1 = px.line(data1, x="Date", y="Loss")
barfig2 = px.line(data2, x="Date", y="Loss")

st.subheader("Claims during storms")
st.plotly_chart(barfig1)
st.subheader("Claims during clear weather")
st.plotly_chart(barfig2)
