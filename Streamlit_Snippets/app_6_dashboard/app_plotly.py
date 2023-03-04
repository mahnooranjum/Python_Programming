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
from constants import *
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
    df1 = pd.read_csv(PATH_1)
    df2 = pd.read_csv(PATH_2)
    
    summary1 = df1.describe()
    summary2 = df2.describe()
    
    # st.write("Dataset Comparison Dashboard")
    # st.markdown("""
    # """)
    # st.text / st.latex
    st.title("Dataset Comparison Dashboard")
    st.caption("Compare two datasets with the same schemas")
    
        
    features = list(df2.columns)
    st.sidebar.header("Select Feature and Statistic: ")
    feature = st.sidebar.selectbox("Select feature", features)
    type_of_chart = st.sidebar.radio("Select chart", ["histogram", "2d-histogram"])
    clicked=st.sidebar.button("Visualize")
    
    # st.<elem>("Label of the widget",\
    #           help ="Helping tooltip",\
    #               disabled =False,\
    #                   key="identity of widget")
    
    
    if clicked:
        # feature = "Age"
        # type_of_chart = "histogram"
        df = pd.DataFrame({f"train_{feature}":df1[feature],f"gen_{feature}": df2[feature] })
    
        if type_of_chart == "2d-histogram":
            chart = px.density_heatmap(df,\
                                       x=f"train_{feature}",\
                                           y=f"test_{feature}",\
                                                       text_auto=True)
            st.plotly_chart(chart, use_container_width=True)
            
        if type_of_chart == "histogram":
            fig = go.Figure()
            fig.add_trace(go.Histogram(x=df[f"train_{feature}"]))
            fig.add_trace(go.Histogram(x=df[f"test_{feature}"]))      
            st.plotly_chart(fig,use_container_width=True)
        
    
    # st.table
    print_datasets = st.sidebar.checkbox("Show datasets")
    if print_datasets:
        st.header("Train Dataset")
        st.dataframe(summary1)
        st.header("Test Dataset")
        st.dataframe(summary2)
    

run_app()
    
# if __name__ == "__main__":
#     run_app()