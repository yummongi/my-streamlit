import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSV 파일에서 데이터를 불러옵니다.
# 이 부분은 실제 파일 경로에 맞게 수정해야 합니다.
@st.cache
def load_data():
    data = pd.read_csv('bus_stop.csv')
    return data

data = load_data()


st.title('대한민국 버스 정류장 정보 조회')
st.header('버스정보시스템(BIS)이 구축된 지자체 중 국가대중교통정보센터(TAGO)와 연계된 139개 지자체의 버스정류장 위치정보 데이터')
st.subheader('미연계 지자체(15개) : 강릉, 강진, 금산, 나주, 담양, 보령, 부산, 서울, 서천, 예산, 완도, 장성, 증평, 청양, 홍성')
st.image('bus_image.jpg')
st.header('조회를 시작하세요!')

# 사용자로부터 도시명을 입력
cities = data['도시명'].unique()
city = st.sidebar.selectbox('도시를 선택하세요.', cities)

# 사용자로부터 정류장명을 입력
bus_stops = data[data['도시명'] == city]['정류장명'].unique()
bus_stop = st.sidebar.selectbox('정류장을 선택하세요.', bus_stops)

# 선택된 도시와 정류장에 해당하는 정보를 필터링
filtered_data = data[(data['도시명'] == city) & (data['정류장명'] == bus_stop)]

# 필터링된 정보를 표시
if st.button('조회'):
    st.subheader(f"{city}의 {bus_stop} 정보")
    st.write(filtered_data)

# 필터링된 정보의 위치를 지도에 표시
if st.checkbox('지도에 표시'):
    st.map(filtered_data[['위도', '경도']])

# 도시별 정류장 수 bar 차트
if st.checkbox('도시별 정류장 수 표시'):
    city_counts = data['도시명'].value_counts()
    fig, ax = plt.subplots()
    city_counts.plot(kind='bar', ax=ax)
    ax.set_title('도시별 정류장 수')
    st.pyplot(fig)

# linechart 생성
if st.checkbox('도시별 최신 정보수집일시'):
    time_df = data.groupby('도시명')['정보수집일시'].max()
    st.line_chart(time_df)
