import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("📊 데이터 시각화")

# 데이터프레임 생성
df = pd.DataFrame({
    '이름': ['철수', '영희', '민수', '지영'],
    '나이': [25, 30, 35, 28],
    '점수': [85, 92, 78, 95]
})

# 데이터프레임 표시
st.dataframe(df)

# 차트 그리기
st.line_chart(df[['나이', '점수']])

# 막대 차트
st.bar_chart(df.set_index('이름')['점수'])