import streamlit as st
import pandas as pd
import plotly.express as px

data1 = pd.read_csv("crimestormQ.csv")
data2 = pd.read_csv("crimenostormQ.csv")

st.title("Crimes during storms and clear weather")

st.dataframe(data1)
st.dataframe(data2)

fig1 = px.line(data1, x="Date", y="Loss")

st.subheader("Claims During Storms")
st.plotly_chart(fig1)

st.subheader("Claims During Clear Weather")
st.plotly_chart(fig2)
