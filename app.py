import streamlit as st
from PrepareData import loadData
from Visualise import visualise
import plotly.express as px
sidebar=st.sidebar
sidebar.title('2021 Olymics in Tokyo')
selection=sidebar.selectbox('select one',['View Dataset','View Analyse'])
df=loadData('Athletes.xlsx')
df1=loadData('Medals.xlsx')
df2=loadData('EntriesGender.xlsx')
df3=loadData('Teams.xlsx')
def init():
    st.title('2021 Olympics in Tokyo')
    st.subheader('In this project we will analyse the Olympics in Toklyo 2021 And about all the athlete and things related to it ')
    st.image('olympics.png')
    
init()

def showData():
    st.header(' Countries who got Highest Gold medals  ')
    st.markdown('----')
    st.dataframe(df1)
    st.header('Atheletes According to their Discipline')
    st.markdown('----')
    st.dataframe(df)
    st.header('Number of males and females according to Discipline')
    st.markdown('----')
    st.dataframe(df2)
    st.header('Number of events in different discipline')
    st.markdown('---')
    st.dataframe(df3)

def analysedata():
    st.header('Analysis of Highest Medals by Top 50  Countries' )
    st.markdown('---')
#---------------------------------------GOLD medals----------------------------------------------------------------------
    st.subheader('Top 50 Cuntries with Gold medals')
    teamdata=df1.head(50)
    st.plotly_chart(px.bar(data_frame=teamdata,x='Team/NOC',y='Gold',template='seaborn',color='Team/NOC',width=900))
    st.markdown('# ')
##-------------------------------------Silver MEdals--------------------------------------------------------------------
    st.subheader('Top 50 Countries with Silver medals')
    teamdata=df1.head(50)
    st.plotly_chart(px.bar(data_frame=teamdata,x='Team/NOC',y='Silver',template='seaborn',color='Team/NOC',width=900))
    st.markdown('# ')
##---------------------------------------Bronze medals--------------------------------------------------------------------
    st.subheader('Top 50 Countries with Bronze Medals')
    teamdata=df1.head(50)
    st.plotly_chart(px.bar(data_frame=teamdata,x='Team/NOC',y='Bronze',template='seaborn',color='Team/NOC',width=900))
    st.markdown('# ')
##----------------------------------name of coutries according to discipline-----------------------------------------------   
    st.header('NO. of countries according to discipline')
    discdata=df.groupby('Discipline',as_index=False).count()
    st.plotly_chart(px.bar(data_frame=discdata,x='Discipline',y='NOC',template='plotly_dark',color='NOC'))
    st.markdown('# ')
##------------------------------------discipline according to country-------------------------------------------------
    st.subheader('Discipline according to country ')
    NOCdata=df.groupby('NOC',as_index=False).count()
    st.plotly_chart(px.bar(data_frame=NOCdata,x='NOC',y='Discipline',template='plotly_dark',color='Name'))  
##-----------------------------------males according to discipline-----------------------------------------------------
    st.header('no of males and females according to discipline')
    st.markdown('# ')
    st.subheader ('Number of males according to discipline')
    genderdata=df2.head(50)
    st.plotly_chart(px.scatter(data_frame=genderdata,x='Male',y='Discipline',color='Total',height=400))
#------------------------------------NUMBER OF EVENTS ACCORDING TO COUNTRIES-------------------------------
    st.header('NUMBER OF EVENTS ACCORDING TO COUNTRIES')
    eventdata=df3.groupby('NOC',as_index=False).count()
    st.plotly_chart(px.scatter(data_frame=eventdata,x='NOC',y='Event',color='NOC',template='plotly_dark'))
    st.markdown('# ')
    st.subheader('Number of Events discipline wise ')

    st.plotly_chart(px.histogram(data_frame=eventdata,x='Event',y='Discipline',color='NOC',template='plotly_dark'))

if selection=='View Dataset':
    st.balloons()
    showData()
elif selection=='View Analyse':
    st.balloons()
    analysedata()

