import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

@st.cache_data
def load_data():
    data = pd.read_csv('bus_stop.csv')
    return data

data = load_data()

st.title('대한민국 버스 정류장 정보 조회')
st.image('bus_image.png') 
st.header('조회를 시작하세요!')

# 도시명 입력
cities = data['도시명'].unique()
city = st.sidebar.selectbox('도시를 선택하세요.', cities)

# 정류장명 입력
bus_stops = data[data['도시명'] == city]['정류장명'].unique()
bus_stop = st.sidebar.selectbox('정류장을 선택하세요.', bus_stops)

# 선택된 도시 정류장에 해당하는 정보를 필터
filtered_data = data[(data['도시명'] == city) & (data['정류장명'] == bus_stop)]

# 필터링 정보를 표시
if st.button('조회'):
    st.subheader(f"{city}의 {bus_stop} 정보")
    st.write(filtered_data)

# 필터링된 정보의 위치를 지도에 표시
if st.checkbox('지도에 표시'):
    st.map(filtered_data[['위도', '경도']])

# 도시별 정류장 수 바 차트
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
