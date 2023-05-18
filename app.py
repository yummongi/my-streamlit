import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
from datetime import datetime

plt.rcParams['font.family'] = 'NanumGothic'

@st.cache_data
def load_data():
    return pd.read_csv("bus_stop.csv")

data = load_data()
data = data.rename(columns={'위도': 'lat', '경도': 'lon'})  # 위도, 경도 컬럼 이름 변경

st.title("버스 정류장 정보")
st.markdown("이 웹 앱은 전국의 버스 정류장 정보를 보여줍니다.")


st.markdown("원하는 데이터를 선택하십시오.")
selected_columns = st.multiselect("원하는 컬럼을 선택하세요.", data.columns)

if selected_columns:
    st.dataframe(data[selected_columns])
else:
    st.dataframe(data)


st.subheader("도시별 정류장 수")
city_counts = data['도시명'].value_counts().reset_index()
city_counts.columns = ['도시명', '정류장 수']
fig, ax = plt.subplots()
sns.barplot(x='도시명', y='정류장 수', data=city_counts, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)


st.subheader("정류장 위치")
st.map(data)
