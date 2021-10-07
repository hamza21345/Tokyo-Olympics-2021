import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

def visualise():
    df=pd.read_excel(filepath)
    px.bar(dataframe=df,x='Name',y='Discipline',color='Type 1')
    return df