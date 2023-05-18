import streamlit as st
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point



@st.cache_data
def load_data():
    data = pd.read_csv('bus_stop.csv')
    data = data.rename(columns={'위도': 'latitude', '경도': 'longitude'})
    return data

data = load_data()

st.title('대한민국 버스 정류장 정보 조회')
st.markdown('버스정보시스템(BIS)이 구축된 지자체 중 국가대중교통정보센터(TAGO)와 연계된 139개 지자체의 버스정류장 위치정보 데이터입니다.')

city_to_search = st.selectbox("정류장명을 검색할 도시를 선택하세요.", data['도시명'].unique())
bus_stop_to_search = st.selectbox("정류장명을 선택하세요.", data[data['도시명'] == city_to_search]['정류장명'].unique())
if bus_stop_to_search:
    bus_stop_data = data[(data['정류장명'] == bus_stop_to_search) & (data['도시명'] == city_to_search)]
    st.write(bus_stop_data)
    st.map(bus_stop_data)  # 버스 정류장을 지도에 표시

if st.checkbox('정류장 간 거리를 계산하시겠습니까?'):
    city_to_calculate_1 = st.selectbox("첫 번째 도시를 선택하세요.", data['도시명'].unique())
    bus_stop_1 = st.selectbox('첫 번째 도시의 정류장을 선택하세요.', data[data['도시명'] == city_to_calculate_1]['정류장명'].unique())

    city_to_calculate_2 = st.selectbox("두 번째 도시를 선택하세요.", data['도시명'].unique())
    bus_stop_2 = st.selectbox('두 번째 도시의 정류장을 선택하세요.', data[data['도시명'] == city_to_calculate_2]['정류장명'].unique())

    location_1 = data[(data['정류장명'] == bus_stop_1) & (data['도시명'] == city_to_calculate_1)][['latitude', 'longitude']].values[0]
    location_2 = data[(data['정류장명'] == bus_stop_2) & (data['도시명'] == city_to_calculate_2)][['latitude', 'longitude']].values[0]

    gs = gpd.GeoSeries([Point(location_1), Point(location_2)])
    distance = gs.distance(gs.shift()).values[1]

    st.write(f"{city_to_calculate_1}의 {bus_stop_1}과(와) {city_to_calculate_2}의 {bus_stop_2} 사이의 거리는 {distance} 입니다.")

    # Create a GeoDataFrame with the two selected bus stops
    gdf = gpd.GeoDataFrame(
        geometry=gpd.points_from_xy([location_1[1], location_2[1]], [location_1[0], location_2[0]]),
        crs="EPSG:4326"
    )

    # Display the map with the two bus stops
    st.map(gdf)


st.subheader('도시별 정류장 수')
city_counts = data['도시명'].value_counts()
st.bar_chart(city_counts)


city = st.selectbox('정류장 분포를 확인하고 싶은 도시를 선택하세요.', data['도시명'].unique())
city_data = data[data['도시명'] == city]
st.map(city_data)

