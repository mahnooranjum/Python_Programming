# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 07:09:41 2023

@author: MAQ
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import streamlit as st
# import seaborn as sns
import altair as alt
from constants import *
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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
    
    st.title("Dataset Comparison Dashboard")
    st.caption("Compare two datasets with the same schemas")
    
    # st.table
    print_datasets = False
    if print_datasets:
        st.header("Reference Dataset")
        st.dataframe(summary1)
        st.header("Generated Dataset")
        st.dataframe(summary2)
        
    
    st.sidebar.header("Select Feature and Statistic: ")
    
    
    feature = "Age"
    type_of_chart = "histogram"
    
    if type_of_chart == "2d-histogram":
        chart = alt.Chart(pd.DataFrame({f"train_{feature}":df1[feature],f"test_{feature}": df2[feature] })).mark_rect().encode(
            alt.X(f"train_{feature}", bin=alt.Bin(maxbins=30)),
            alt.Y(f"test_{feature}", bin=alt.Bin(maxbins=30)),
            alt.Color('count():Q', scale=alt.Scale(scheme='redpurple'))
            ).interactive()
        
        st.altair_chart(chart, use_container_width=True)
        
    if type_of_chart == "histogram":
        
        chart = alt.Chart(pd.DataFrame({f"ref_{feature}":df1[feature],f"gen_{feature}": df2[feature] })).mark_bar().encode(
            alt.X(f"ref_{feature}", bin=alt.Bin(maxbins=40)),
            color=alt.Color('count():Q', scale=alt.Scale(scheme='redpurple')),
            y='count()'
        ).interactive()
                
        st.altair_chart(chart,use_container_width=True)
    
    
    

run_app()
    
# if __name__ == "__main__":
#     run_app()