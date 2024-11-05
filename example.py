import streamlit as st
import pandas as pd

df = pd.read_csv("data-editor-paste-demo - Sheet1.csv")
df = pd.DataFrame(df)
df.columns = ['Names', 'Age', 'Sex', 'Work']

with st.sidebar:
    color = st.color_picker("Pick A Background Color", "#3A6783")
    st.markdown('<style>[data-testid="stAppViewContainer"]{background-color:' + color + ';} .st-emotion-cache-6wgtf7 {border-width: 3px; border-color: #000;} [data-testid="stSidebar"] {background-color: rgba(0, 0, 0, 0.90);} </style>', unsafe_allow_html=True)
    
    options = st.multiselect("Select a category",['Names', 'Age', 'Sex', 'Work'])
# Título de la aplicación
st.title('My first Web App with Streamlit')


st.data_editor(df[options])
st.bar_chart(df[options])