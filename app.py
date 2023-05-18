import streamlit as st
import pandas as pd

@st.cache_data   # 수정된 부분
def load_data():
    data = pd.read_csv('bus_stop.csv')
    data = data.rename(columns={'위도': 'latitude', '경도': 'longitude'})  # 수정된 부분
    return data

data = load_data()

st.title('대한민국 버스 정류장 정보 조회')

# 사용자로부터 도시명을 입력받습니다.
cities = data['도시명'].unique()
city = st.selectbox('도시를 선택하세요.', cities)

# 사용자로부터 정류장명을 입력받습니다.
bus_stops = data[data['도시명'] == city]['정류장명'].unique()
bus_stop = st.selectbox('정류장을 선택하세요.', bus_stops)

# 선택된 도시와 정류장에 해당하는 정보를 필터링합니다.
filtered_data = data[(data['도시명'] == city) & (data['정류장명'] == bus_stop)]

# 필터링된 정보를 표시합니다.
st.write(filtered_data)

# 필터링된 정보의 위치를 지도에 표시합니다.
st.map(filtered_data)

#도시별 정류장 수를 bar chart로 보여줍니다.
city_counts = data['도시명'].value_counts()
st.bar_chart(city_counts)
