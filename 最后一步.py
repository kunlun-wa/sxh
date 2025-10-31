import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import altair as alt
import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
page = st.sidebar.selectbox("选择页面", ["简介页面", "专业数据分析","成绩预测"])
st.title("🎓学生成绩分析与预测系统")
if page == "简介页面":
    c1,c2=st.columns([1,1])
    with c1:
        
        
        st.markdown('***')

        st.header("📖项目概述")
        st.write("""
        本项目是一个基于Excel的数字生成的软件平台，了解专业数据、开发数据和考试流程。
        """)


        st.header("主要特点")
        st.markdown("""
        - **🗒️数据可视化**：多维度数据可视化与数据
        - **🗒️作业时间**：在作业时间内自动完成
        - **🗒️数据管理**：基于文档库进行数据处理
        - **🗒️考前模拟**：数据可视化与数字化生成
        """)

        st.markdown('***')
    with c2:
        
        st.image('D:/streamlit_env/11.png')
    # 项目目标
    st.header("项目目标")
    a1,a2,a3=st.columns(3)
    with a1:
        st.subheader("📋目标一")
        st.write("分析影响因素")
        st.markdown("""
        - 识别关键学习指标
        - 探索成绩相关因素
        - 提供数据支持决策
        """)

    with a2:
        st.subheader("📉目标二")
        st.write("可视化展示")
        st.markdown("""
        - 专业对比分析
        - 性别差异研究
        - 学习模式识别
        """)

    with a3:
        st.subheader("📊目标三")
        st.write("成绩预测")
        st.markdown("""
        - 机器学习模型
        - 个性化预测
     
        """)
    st.markdown('***')
    # 技术架构
    st.subheader("🛠️技术架构")
    b1,b2,b3,b4=st.columns(4)
    with b1:
         st.write("前端框架")
         st.write("stremlit")
    with b2:
         st.write("数据处理")
         st.write("andas")
         st.write("Nunpy")
    with b3:
         st.write("可视化")
         st.write("plotly")
         st.write("Matplotlib")
    with b4:
         st.write("数据处理")
         st.write("scikit-learn")
    


elif page == "专业数据分析":
    st.set_page_config(page_title="专业数据分析", layout="wide")


    st.title("专业数据分析")
    st.markdown('***')
    st.header("1. 各专业男女性别比例")


    df_student = pd.read_csv("ks.csv")


    gender_count = df_student.groupby(["专业", "性别"]).size().unstack(fill_value=0)

    if gender_count.columns.tolist() == ["男", "女"]:
        gender_count = gender_count[["女", "男"]]


    gender_ratio = (gender_count / gender_count.sum(axis=1).values.reshape(-1, 1) * 100).round(1)

    df_gender = gender_ratio.reset_index()
    df_gender.columns = ["major", "女", "男"]  


    fig_gender = go.Figure()

    fig_gender.add_trace(go.Bar(
        x=df_gender["major"],
        y=df_gender["男"],
        name="男",
        marker_color="#87CEEB"
    ))

    fig_gender.add_trace(go.Bar(
        x=df_gender["major"],
        y=df_gender["女"],
        name="女",
        marker_color="#4169E1"
    ))

    fig_gender.update_layout(
        barmode="group",  
        xaxis_title="专业",  
        yaxis_title="比例(%)", 
        height=400,  
        legend_title="性别",  
        legend=dict(orientation="v", yanchor="top", y=0.99, xanchor="right", x=0.99)  
    )


    col1, col2 = st.columns([2, 1]) 
    with col1:
        
        st.plotly_chart(fig_gender, use_container_width=True)
    with col2:
        
        st.subheader("性别比例数据")
        
        st.dataframe(df_gender.set_index("major"), use_container_width=True)





    st.markdown('***')
    st.header("2.各专业学习指标对比")
    st.caption("各专业平均学习时间与成绩对比")

    df = pd.read_csv("ks.csv")

    metrics = ["每周学习时长（小时）", "期中考试分数", "期末考试分数"]
    df_major = df.groupby("专业")[metrics].mean().round(1).reset_index()
    df_melt = df_major.melt(id_vars="专业", var_name="指标", value_name="数值")


    bar_layer = alt.Chart(df_melt[df_melt["指标"] == "期中考试分数"]).mark_bar(color="#4169E1").encode(
        x=alt.X("专业", axis=alt.Axis(labelAngle=-45)),
        y=alt.Y("数值", title="指标数值"),
        tooltip=["专业", "指标", "数值"]
    )

    line_layer1 = alt.Chart(df_melt[df_melt["指标"] == "每周学习时长（小时）"]).mark_line(point=True, color="#87CEEB").encode(
        x="专业",
        y="数值",
        tooltip=["专业", "指标", "数值"]
    )

    line_layer2 = alt.Chart(df_melt[df_melt["指标"] == "期末考试分数"]).mark_line(point=True, color="#FF6347").encode(
        x="专业",
        y="数值",
        tooltip=["专业", "指标", "数值"]
    )


    chart = bar_layer + line_layer1 + line_layer2
    chart = chart.properties(height=400).configure_axis(titleFontSize=14, labelFontSize=12)

    col1, col2 = st.columns([3, 2])
    with col1:
        st.altair_chart(chart, use_container_width=True, theme="streamlit")
    with col2:
        st.subheader("详细数据")
        st.dataframe(df_major.set_index("专业"), use_container_width=True)


    st.markdown('***')
    st.header("3.各专业出勤率分析")
    st.subheader("出勤率排名")


    df = pd.read_csv("ks.csv")
    df_attendance = df.groupby("专业")["上课出勤率"].mean().reset_index()
    df_attendance["平均出勤率"] = (df_attendance["上课出勤率"] * 100).round(1)
    df_attendance_sorted = df_attendance.sort_values("平均出勤率", ascending=False).reset_index(drop=True)
    df_attendance_sorted["排名"] = df_attendance_sorted.index
    df_result = df_attendance_sorted[["排名", "专业", "平均出勤率"]]


    chart = (
        alt.Chart(df_result)
        .mark_bar()
        .encode(
            x=alt.X("专业", sort="-y", title="专业"),
            y=alt.Y("平均出勤率", title="平均出勤率(%)"),
            color=alt.Color("专业", scale=alt.Scale(scheme="category10")),  
            tooltip=["排名", "专业", "平均出勤率"]
        )
        .properties(height=350)
    )


    col_chart, col_table = st.columns([1, 1])
    with col_chart:
        st.altair_chart(chart, use_container_width=True, theme="streamlit")
    with col_table:
        st.dataframe(df_result.set_index("排名"), use_container_width=True)



    st.markdown('***')
    st.header("4.大数据管理专业专项分析")


    df = pd.read_csv("ks.csv")
    df_bd = df[df["专业"] == "大数据管理"].copy()


    avg_study = df_bd["每周学习时长（小时）"].mean().round(1)
    avg_attend = (df_bd["上课出勤率"].mean() * 100).round(1)
    avg_final = df_bd["期末考试分数"].mean().round(1)
    pass_rate = round((len(df_bd[df_bd["期末考试分数"] >= 60]) / len(df_bd) * 100), 1)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("平均学习时间", f"{avg_study} 小时")
    with col2:
        st.metric("平均出勤率", f"{avg_attend}%")
    with col3:
        st.metric("平均期末成绩", f"{avg_final} 分")
    with col4:
        st.metric("及格率", f"{pass_rate}%")


    st.subheader("大数据管理专业期末成绩箱线图")
    boxplot = (
        alt.Chart(df_bd)
        .mark_boxplot(color="#4169E1", size=60)
        .encode(
            y=alt.Y("专业:N", title="专业", axis=alt.Axis(labelAngle=0)),
            x=alt.X("期末考试分数:Q", title="期末成绩（分）", scale=alt.Scale(domain=[10, 100])),
            tooltip=["期末考试分数"]
        )
        .properties(height=350)
    )
    st.altair_chart(boxplot, use_container_width=True, theme="streamlit")
    st.subheader("大数据管理专业期末成绩分布")
    histogram = (
        alt.Chart(df_bd)
        .mark_bar(color="#87CEEB", opacity=0.8)
        .encode(
            x=alt.X("期末考试分数:Q", title="期末成绩（分）", bin=alt.Bin(maxbins=10)),
            y=alt.Y("count():Q", title="学生人数"),
            tooltip=[alt.Tooltip("期末考试分数:Q", bin=True, title="成绩区间"), "count():Q"]
        )
        .properties(height=350)
    )
    st.altair_chart(histogram, use_container_width=True, theme="streamlit")

elif page== "成绩预测":
    st.set_page_config(page_title="期末成绩预测", page_icon="", layout="wide")
    model = joblib.load("score_predictor.pkl")

    st.markdown('期末成绩预测')
    st.subheader('请输入学生的学习信息，系统将预测其期末成绩并提供学习建议')
    ql,q2 = st.columns([2, 2])
    with ql:
        number = st.text_input('学号',autocomplete='number')
        st.write('性别')
        sex = st.selectbox('性别',['男','女'],label_visibility='collapsed')
        st.write('专业')
        zhuanye = st.selectbox('专业',['人工智能','大数据管理','工商管理','电子商务','财务管理'],label_visibility='collapsed')
        submit = st.button('预测成绩')
    with q2:
        xuexi = st.slider('每周学习时长（小时）',min_value=0.0,max_value=100.0,step=0.1)
        shangke = st.slider('上课出勤率',min_value=0.0,max_value=1.0,step=0.01)
        qizhong=st.slider('期中考试分数',min_value=0.0,max_value=100.0,step=0.1)
        zuoye=st.slider('作业完成率',min_value=0.0,max_value=1.0,step=0.01)
    if submit:
            
        X= [[xuexi, shangke, qizhong, zuoye]]
        pred_score = model. predict(X)[0]
        pred_score = max(0,min(100, pred_score))
        st.subheader('预测结果')
        st.markdown(f'**米预测期末成绩:{pred_score:.2f}分**')
        if pred_score >= 80:
            st.image('https://pic.ibaotu.com/02/18/83/84D888piCxbz.jpg!wac.jpg')
            st.text('恭喜你!成绩优秀!')
        elif pred_score >= 60:
            st.success('成绩合格，继续保持!')
            st.image('https://www.gxgif.com/pic/lz/2025912214743.jpg')
            st.warning('成绩待提高，建议加强学习!')
            st.image('https://www.gxgif.com/pic/lz/2025912215043.jpg')


