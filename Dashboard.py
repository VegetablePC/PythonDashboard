import streamlit as st
import pandas as pd
import plotly.express as px

data1 = pd.read_csv("crimestormQ.csv")
data2 = pd.read_csv("crimenostormQ.csv")

fig1 = px.line(data1, x="Date", y="Loss (In Dollars)")
fig2 = px.line(data2, x="Date", y="Loss")

st.subheader("Claims During Storms")
fig1.update_yaxes(range=[0, 3500])
st.plotly_chart(fig1)


st.subheader("Claims During Clear Weather")
fig2.update_yaxes(range=[0, 3500])
st.plotly_chart(fig2)
