import streamlit as st
import pandas as pd
import plotly.express as px
import requests as rq

# Reads both CSV sheets for data
data1 = pd.read_csv("crimestormQ.csv")
data2 = pd.read_csv("crimenostormQ.csv")
desc = open("Description.txt", "r")

#Plots our initial lines by defining fig1 and fig2 as plotly lines
fig1 = px.line(data1, x="Date", y="Loss") 
fig2 = px.line(data2, x="Date", y="Loss")

fig1.update_yaxes(range=[0, 3500]) # Sets range to 3500 to match fig2
fig1.update_layout(title_text="Claims During Stormy Weather", title_x=0.4) # Titles the graph and moves the title closer to center
fig1.update_layout(yaxis_title="Total Loss in Dollars") # Updates the Y Axis to say "Total Loss in Dollars" instead of default column title
st.plotly_chart(fig1)

fig2.update_yaxes(range=[0, 3500]) # Sets range to 3500 to match fig1
fig2.update_layout(title_text="Claims During Clear Weather", title_x=0.4) # Titles the graph and moves the title closer to center
fig2.update_layout(yaxis_title="Total Loss in Dollars") # Updates the Y Axis to say "Total Loss in Dollars" instead of default column title
st.plotly_chart(fig2)

st.markdown("<h1 style='text-align: center; color: grey; '>Description</h1>")
st.write(desc.read())
