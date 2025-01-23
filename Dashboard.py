import streamlit as st
import pandas as pd
import plotly.express as px

# Reads both CSV sheets for data
data1 = pd.read_csv("crimestormQ.csv")
data2 = pd.read_csv("crimenostormQ.csv")

#Plots our initial lines by defining fig1 and fig2 as plotly lines
fig1 = px.line(data1, x="Date", y="Loss") 
fig2 = px.line(data2, x="Date", y="Loss")

# Title for graph 1
fig1.update_yaxes(range=[0, 3500]) # Sets range to 3500 to match fig2
fig1.update_layout(title={
  "Claims during Storms",
  'xanchor': 'center'})
fig1.update_layout(yaxis_title="Total Loss in Dollars") # Updates the Y Axis to say "Total Loss in Dollars" instead of default column title
st.plotly_chart(fig1)

# Title for graph 2
st.subheader("Claims During Clear Weather")

fig2.update_yaxes(range=[0, 3500]) # Sets range to 3500 to match fig1
fig2.update_layout(yaxis_title="Total Loss in Dollars") # Updates the Y Axis to say "Total Loss in Dollars" instead of default column title
st.plotly_chart(fig2)
