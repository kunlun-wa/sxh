import streamlit as st
import pandas as pd
import numpy as np
# 定义数据,以便创建数据框
data = {
    '月份':['01月', '02月', '03月'],
    '蜜雪冰城':[2002, 150, 180],
    '古茗':[120, 160, 123],
    '梁小糖':[110, 100, 160],
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3,], name='序号')
# 将新索引应用到数据框上
st.index = index
st.dataframe(df)
st.table(df)
st.bar_chart(df)#条形图
st.area_chart(df)#面积图
df = pd.DataFrame(
    np.random.randn(1000, 2) / [20, 50] + [39.9, 116.4],
    columns=['latitude', 'longitude'])
# 设置索引列的名称
df.index.name='序号'

st.subheader('展示部分需要绘制随机点的经纬度')
st.dataframe(df[1:5])

st.subheader('在北京地图上随机画点')
st.map(df)
