import streamlit as st
from PrepareData import loadData
from Visualise import visualise
import plotly.express as px
sidebar=st.sidebar
sidebar.title('2021 Olymics in Tokyo')
sidebar.image('olympics3..jpg')
selection=sidebar.selectbox('select one',['View Dataset','View Analyse'])
df=loadData('Athletes.xlsx')
df1=loadData('Medals.xlsx')
df2=loadData('EntriesGender.xlsx')
df3=loadData('Teams.xlsx')
df4=loadData('Coaches.xlsx')
def init():
    st.title('2021 Olympics in Tokyo')
    st.subheader('Hello ,this analysis is all about Tokyo Olympics 2021 .The data sets will help you know everything regarding the games played by different countries. ')
    st.image('olympics.png')
    
init()

def showData():
    st.header(' Countries are arranged  acoording  Highest  medals  ')
    st.markdown('----')
    st.dataframe(df1)
    st.header('Atheletes According to their Sports')
    st.markdown('----')
    st.dataframe(df)
    st.header('Number of males and females according to Sports')
    st.markdown('----')
    st.dataframe(df2)
    st.header('Number of events in different Sports')
    st.markdown('---')
    st.dataframe(df3)
    st.header('Number of coaches with different countries')
    st.markdown('---')
    st.dataframe(df4)

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
    st.header('NO. of countries according to Sports')
    discdata=df.groupby('Discipline',as_index=False).count()
    st.plotly_chart(px.bar(data_frame=discdata,x='Discipline',y='NOC',template='plotly_dark',color='NOC'))
    st.markdown('# ')

##-----------------------------------males according to discipline-----------------------------------------------------
    st.header('Number of Males and Females in different sports')
    st.markdown('# ')
    genderdata=df2.head(50)
    st.plotly_chart(px.scatter(data_frame=genderdata,x='Discipline',y=['Male','Female'],title='NO. OF MALES AND FEMALES IN DIFFERENT SPORTS',color_discrete_sequence=px.colors.sequential.RdBu_r,height=400))
    st.markdown('# ')
    st.subheader('Top 10 Countries with highest number of players')
    st.plotly_chart(px.pie(genderdata.head(10),values='Total',names='Discipline',color_discrete_sequence=px.colors.sequential.Viridis))
#------------------------------------NUMBER OF EVENTS ACCORDING TO COUNTRIES-------------------------------
    st.header('NUMBER OF EVENTS ACCORDING TO COUNTRIES')
    eventdata=df3.groupby('NOC',as_index=False).count()
    st.plotly_chart(px.scatter(data_frame=eventdata,x='NOC',y='Event',color='NOC',template='plotly_dark'))
    st.markdown('# ')
    st.subheader('Number of Events Sports wise ')

    st.plotly_chart(px.histogram(data_frame=eventdata,x='Event',y='Discipline',color='NOC',template='plotly_dark'))
 #-------------------------------------Coaches------------------------------------------   
    st.header(' Coutnries with highest  number  of Coaches ')
    st.subheader('Top 10 countires with higherst number of coaches')
    coachdata=df4.groupby('NOC',as_index=False ).count()
    coachdata.sort_values('Name',ascending=False)
    coachdata.head(10)
    st.plotly_chart(px.pie(coachdata.head(10),values='Name',names='NOC',hover_name='NOC',color_discrete_sequence=px.colors.sequential.RdBu))
    st.markdown('# ')
    st.header('Countries and their number of coaches')
    st.plotly_chart(px.line(coachdata,x='NOC',y='Name',height=500,markers=True,color='Event',color_discrete_sequence=px.colors.sequential.RdBu))


if selection=='View Dataset':
    st.balloons()
    showData()
elif selection=='View Analyse':
    st.balloons()
    analysedata()

