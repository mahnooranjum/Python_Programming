# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 10:00:16 2023

@author: MAQ
"""


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import streamlit as st
# import seaborn as sns
# import altair as alt?
# from constants import *
import plotly.express as px
import plotly.graph_objects as go
st.set_page_config(page_title="Dashboard",
                   page_icon = ":bar_chart:",
                   layout = "wide")


def get_stats(summary1: pd.DataFrame,\
              summary2: pd.DataFrame,\
                  stat: str,\
                      feature: str) -> list[float] | list[int]:
    return [summary1.loc[stat,feature], summary2.loc[stat,feature]]


def run_app():
    df1 = None
    df2 = None
    global PATH_1
    global PATH_2
    st.title("Dataset Comparison Dashboard")
    st.caption("Compare two datasets with the same schemas")
    st.sidebar.header("Navigate")
    page = st.sidebar.selectbox("Select page", ["About", "Show Summary" ,"View Data", "Visualize"])
    # st.sidebar.header("Train file:")
    myslot1 = st.sidebar.empty()
    myslot2 = st.sidebar.empty()
    myslot3 = st.sidebar.empty()
    st.sidebar.write("***")
    st.sidebar.header("Datasets")
    PATH_1 = st.sidebar.file_uploader("Upload train file")
    # st.sidebar.header("Test file:")
    PATH_2 = st.sidebar.file_uploader("Upload test file")
    if PATH_1 is not None:
        df1 = pd.read_csv(PATH_1)
    if PATH_2 is not None:
        df2 = pd.read_csv(PATH_2)
    if page == "About":

        st.header("About")
        st.text("This dashboard compares two different datasets with the same schemas")

    if page == "Show Summary":
        st.sidebar.header("Select")
        st.header("Show Summary")
        if df2 is not None and df1 is not None:
            
            print1 = myslot1.checkbox("Show train data summary")
            print2 = myslot2.checkbox("Show test data summary")
            summary1 = df1.describe()
            summary2 = df2.describe()
            if print1:
                st.dataframe(summary1)
            if print2:
                st.dataframe(summary2)   
    if page == "View Data":
        
        st.header("View Data")
        if df2 is not None and df1 is not None:
            print_datasets = myslot1.checkbox("Show datasets")
            if print_datasets:
                st.header("Train Dataset")
                st.dataframe(df1)
                st.header("Test Dataset")
                st.dataframe(df2)
    if page == "Visualize":
        st.header("Visualize")
        if df2 is not None and df1 is not None:
            
            features = list(df2.columns)
            features = [feature for feature in features if df2.dtypes[feature] != "object"]
            
            feature = myslot1.selectbox("Select feature", features)
            type_of_chart = myslot2.radio("Select chart", ["histogram", "2d-histogram"])
            clicked=myslot3.button("Visualize")
    
            
            if clicked:
    
                df = pd.DataFrame({f"train_{feature}":df1[feature],f"test_{feature}": df2[feature] })
            
                if type_of_chart == "2d-histogram":
                    chart = px.density_heatmap(df,\
                                               x=f"train_{feature}",\
                                                   y=f"test_{feature}",\
                                                               text_auto=True)
                    st.plotly_chart(chart, use_container_width=True)
                    
                if type_of_chart == "histogram":
                    fig = go.Figure()
                    fig.add_trace(go.Histogram(x=df[f"train_{feature}"],name="train"))
                    fig.add_trace(go.Histogram(x=df[f"test_{feature}"], name="test"))      
                    st.plotly_chart(fig,use_container_width=True)
                
    

    
    # st.table

    

run_app()
    
# if __name__ == "__main__":
#     run_app()