import pandas as pd 
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
data = pd.read_csv("train.csv")
fig1 = px.box(data,x="Credit_Score", 
             y="Monthly_Inhand_Salary", 
             color="Credit_Score",
             title="Credit Scores Based on Monthly Inhand Salary", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'orange',
                                 'Good':'green'})
fig1.update_traces(quartilemethod="exclusive")

fig2 = px.box(data,x="Credit_Score", 
             y="Age", 
             color="Credit_Score",
             title="Credit Scores Based on Age", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'orange',
                                 'Good':'green'})
fig2.update_traces(quartilemethod="exclusive")
st.title("Credit Scores Analysis")
st.plotly_chart(fig1)
st.plotly_chart(fig2)
