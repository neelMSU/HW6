import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.graph_objects as go

df=pd.read_csv('diabetes.csv')
st.header("""
For this project I'm going to use the Diabetes Dataset. What I'm trying to find out is most obvious health condition for people with diabetes and also for people with no diabetes.
""")
st.dataframe(df.head())
st.header("Diabetes is one of the most dangerious diesease which does effect person's daily lifestyle. Dealing with such disease should be top priority.")


st.header("With the help of my dataset I will try to find out most probable cause for people with diabetes as well as for those with no diabetes.")

colors = ['gold', 'mediumturquoise']
labels = ['0','1']
values = df['Outcome'].value_counts()/df['Outcome'].shape[0]

# Use `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
fig.update_traces(hoverinfo='label+percent', textinfo='percent', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
fig.update_layout(
    title_text="Outcome")
st.plotly_chart(fig)
