import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.title('Exploratory Data Analysis')
st.markdown('''Exploratory data analysis is an approach to analyzing data sets to summarize their main 
characteristics, often with visual methods. Particularly, selecting the optimal features for the Machine Learning model
yields low mean square error and a better score''')

with st.sidebar.header('Import your csv'):
    uploaded_file = st.sidebar.file_uploader('Upload your csv file here', type=['csv'])
    
if uploaded_file is not None:
    def load_csv():
        data = pd.read_csv(uploaded_file)
        return data
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('Dataset')
    st.write(df)
    st.header('Pandas Profiling Report')
    st_profile_report(pr)


