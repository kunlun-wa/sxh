import streamlit as st
import pandas as pd

# 定义数据,以便创建数据框
data = {
    '月份':['01月', '02月', '03月'],
    '1号门店':[200, 150, 180],
    '2号门店':[120, 160, 123],
    '3号门店':[110, 100, 160],
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
