import streamlit as st 
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


def run_eda():

    df = pd.read_csv('wether_seoul.csv',index_col=0)
    df_plt = df.loc[(df['년'] != 2014) & (df['년'] != 2022)]
    list = df.columns[2:-2]
    selec1 = st.selectbox('', list )
    selec2 = st.radio('선택', df.columns[-2:])
    
    fig = plt.figure()
    
    if selec1 == '발생건수(건)' :
        x = df_plt .groupby(selec2)[selec1].sum().index
        y= df_plt .groupby(selec2)[selec1].sum()
    else:
        x = df_plt .groupby(selec2)[selec1].mean().index
        y= df_plt .groupby(selec2)[selec1].mean()

    plt.plot(x,y)
    st.pyplot(fig)


    year_list = ['전체','2022','2021','2020','2019','2018','2017','2016','2015','2014']


    year_selec =  st.selectbox('선택', year_list)

    if year_selec == '전체' :
        df_frame = df.iloc[:,:-2]
        st.dataframe(df_frame.loc[df_frame['발생건수(건)'] == df_frame['발생건수(건)'].max(),] )
        st.dataframe(df_frame.loc[df_frame['발생건수(건)'] == df_frame['발생건수(건)'].min(),] )