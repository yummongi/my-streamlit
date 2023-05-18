import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    data = pd.read_csv('bus_stop.csv')
    data = data.rename(columns={'위도': 'latitude', '경도': 'longitude'})
    return data

data = load_data()

st.title('대한민국 버스 정류장 정보 조회')
st.markdown('버스정보시스템(BIS)이 구축된 지자체 중 국가대중교통정보센터(TAGO)와 연계된 139개 지자체의 버스정류장 위치정보 데이터입니다.')


cities = data['도시명'].unique()
city = st.selectbox('도시를 선택하세요.', cities)


bus_stops = data[data['도시명'] == city]['정류장명'].unique()
bus_stop = st.selectbox('정류장을 선택하세요.', bus_stops)

filtered_data = data[(data['도시명'] == city) & (data['정류장명'] == bus_stop)]


st.write(filtered_data)

st.map(filtered_data)


city_counts = data['도시명'].value_counts()
st.bar_chart(city_counts)
