import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = st.slider('Select a value')
st.write(x, 'sqaured is', x * x)

st.title("this is the app title")
st.header("this is the header")
st.markdown("this is the markdown")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a + a r ^1+ a r^2 + a r^3 ''')

st.sidebar.title("This is written inside the sidbar")
st.sidebar.button("Click")

#bar chart
rand = np.random.normal(1,2,size=20)
fig,ax = plt.subplots()
ax.hist(rand, bins = 15)
st.pyplot(fig)

#add data
import streamlit as st
import pandas as pd

# 데이터를 로드합니다.
@st.cache
def load_data():
    data = pd.read_csv('대기질_데이터.csv') # 이 부분은 실제 데이터 파일의 경로와 일치해야 합니다.
    return data

data = load_data()

# 앱의 타이틀을 설정합니다.
st.title('대한민국 대기질 정보')

# 사용자로부터 도시와 오염 물질을 선택하도록 합니다.
city = st.selectbox('도시를 선택하세요.', data['도시'].unique())
pollutant = st.selectbox('오염 물질을 선택하세요.', ['미세먼지', '초미세먼지', '이산화질소', '오존'])

# 선택된 도시와 오염 물질에 대한 데이터를 필터링합니다.
filtered_data = data[(data['도시'] == city) & (data['오염 물질'] == pollutant)]

# 필터링된 데이터의 통계를 보여줍니다.
st.write(filtered_data.describe())

# 필터링된 데이터를 차트로 보여줍니다.
st.line_chart(filtered_data['농도'])


