import streamlit as st
import numpy as np
import joblib
regressor = joblib.load('regressor.pkl')


def run_ml():
    st.subheader('감기 진료 예측')

    
    temp = st.number_input('최저기온을 입력해주세요',-18.0,30.0)

    
    day_temp = st.number_input('일교차를 입력해주세요',1.50000 ,18.50000)

    
    rain = st.number_input('강수량을 입력해주세요',0,140)

    
    wet = st.number_input('습도를 입력해주세요',17.900000,98.100000)

    
    wind = st.slider('풍속을 선택해주세요', 0.0,6.4, 0.1)

    
    press = st.slider('현지기압을 선택해주세요', 981.5 , 1026.8 )

    new_data=np.array([temp,rain,wind,wet,press,day_temp])
    new_data=new_data.reshape(1,6)
    regressor = joblib.load('regressor.pkl')
    y_pred=regressor.predict(new_data)
    y_pred= round(y_pred[0])

    st.info('예측한 잠재적 감기환자는 {}명 입니다.'.format(y_pred,","))


