import streamlit as st
from streamlit_option_menu import option_menu
from app_eda import run_eda
from app_home import run_home

from app_ml import run_ml


def main():
    st.set_page_config(
     page_title="기상정보로 감기환자 예측",
     page_icon="🌦️",
    #  layout="wide",
     initial_sidebar_state="expanded",
     )
    
    url = 'https://www.korea.kr/newsWeb/resources/temp/images/000106/%EC%98%88%EB%B0%A9%EC%A0%91%EC%A2%85.jpg'

    with st.sidebar:
        st.image(url,use_column_width=True)
        menu = option_menu('Menu',['Home','EDA','ML'], icons = ['house-door-fill','bar-chart-line-fill','gear-wide-connected'],menu_icon="caret-down-fill", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#198fc2"},
    })
    



    if menu == 'Home':
        run_home()
    elif menu == 'EDA':
        run_eda()
    elif menu == 'ML':
        run_ml()



if __name__ == '__main__':
    main()
