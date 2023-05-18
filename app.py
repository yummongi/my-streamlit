import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일에서 데이터를 불러옵니다.
@st.cache
def load_data():
    data = pd.read_csv('bus_stop.csv')
    return data

data = load_data()

st.title('대한민국 버스 정류장 정보 조회')

# 사용자로부터 도시명을 입력받기
cities = data['도시명'].unique()
city = st.selectbox('도시를 선택하세요.', cities)

# 선택된 도시에 해당하는 정보를 필터
filtered_data = data[data['도시명'] == city]

# 사용자로부터 정류장명을 입력
bus_stops = filtered_data['정류장명'].unique()
bus_stop = st.selectbox('정류장을 선택하세요.', bus_stops)

# 선택된 도시와 정류장에 해당하는 정보 필터
selected_data = filtered_data[filtered_data['정류장명'] == bus_stop]

# 필터링된 정보를 표시
st.write(selected_data)

# 필터링된 정보의 위치를 지도에 표시
st.map(selected_data)

# 각 정류장의 버스 수를 계산
bus_counts = filtered_data['정류장명'].value_counts()

# 막대 그래프를 생성
plt.figure(figsize=(10,5))
plt.bar(bus_counts.index, bus_counts.values)
plt.xlabel('정류장명')
plt.ylabel('버스 수')
plt.title(f'{city}의 정류장별 버스 수')
plt.xticks(rotation=90)
plt.tight_layout()

# 막대 그래프를표시합니다.
st.pyplot(plt.gcf())
