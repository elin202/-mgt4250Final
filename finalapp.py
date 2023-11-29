import pandas as pd 
import plotly.express as px
import matplotlib.pyplot as plt
data = pd.read_csv("train.csv")
fig = px.box(data,x="Credit_Score", 
             y="Monthly_Inhand_Salary", 
             color="Credit_Score",
             title="Credit Scores Based on Monthly Inhand Salary", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'orange',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()
st.title("Credit Scores and Monthly Inhand Salary")
st.plotly_chart(fig)