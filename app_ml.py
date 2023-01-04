import streamlit as st
import numpy as np
import joblib
regressor = joblib.load('data/regressor.pkl')


def run_ml():
    st.subheader('감기 진료 예측')

    temp = st.number_input('최저기온',-18,30)

    day_temp = st.number_input('일교차',1.50000 ,18.50000)

    rain = st.number_input('강수량 입력',0,140)

    wet = st.number_input('평균습도',17.900000,98.100000)

    wind = st.slider('풍속', 0 ,6.4,0.1)

    press = st.slider('평균 현지기압', 981.000000 , 1026.800000 ,0.1)

    new_data=np.array([temp,rain,wind,wet,press,day_temp])
    new_data=new_data.reshape(1,6)
    regressor = joblib.load('regressor.pkl')
    y_pred=regressor.predict(new_data)
    y_pred = round(y_pred[0],1)


