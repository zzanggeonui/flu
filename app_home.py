import streamlit as st

def run_home():

    

    st.title('기상정보를 통한 감기 진료건수 예측')
    st.subheader('왼쪽 사이드바에서 원하는 내용을 선택하세요.')
    st.video('https://www.youtube.com/watch?v=OzAe-J9tJXw',start_time=10,format='video/mp4')

    st.write('📝 이 앱은 예상 감기환자를 분석하여 예측 및 차트로 보여주는 앱입니다.')
    st.write('📝 EDA를 눌러보시면 데이터별로 분석된 차트를 확인하실 수 있습니다.')
    st.write('📝 ML은 인공지능이 학습하여 기온,일교차,습도,풍속등으로 예측한 감기환자를 확인하실 수 있습니다.')
    


