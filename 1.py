import streamlit as st
import pickle
import pandas as pd
page = st.sidebar.selectbox("选择页面", ["简介页面", "预测分类页面"])

if page == "简介页面":
    st.title("企鹅分类器🐧")
    st.header('数据集介绍')
    st.write("帕尔默群岛企鹅数据集是用于数据探索和数据可视化的一个出色的数据集，也可以作为机器学习入门练习，该数据集是由 Gorman 等收集，并发布在一个名为 palmerpenguins 的 R 语言包，以对南极企鹅种类进行分类和研究该数据集记录了 344 行观测数据，包含 3 个不同物种的企鹅：阿德利企鹅、巴布亚企鹅和帽带企鹅的各种信息。")
    st.header('三种企鹅的卡通图像')
    st.image("https://tse3-mm.cn.bing.net/th/id/OIP-C.v3b_DewOkXIzanKImwXWhgHaHa?w=138&h=180&c=7&r=0&o=7&pid=1.7&rm=3.jpg", caption='企鹅')
elif page == "预测分类页面":
    col_form,col,col_logo=st.columns([3,1,2])
    with col_form:
        with st.form('user_inputs'):
            
            island = st.selectbox('企鹅栖息的岛屿',options=['托尔森岛','比斯科群岛','德里姆岛'])
            sex = st.selectbox('性别',options=['雄性','雌性门'])

            bill_length = st.number_input('喙的长度(毫米)',min_value=0.0)
            bill_depth = st.number_input ('喙的深度(毫米)',min_value=0.0)
            flipper_length = st.number_input('翅膀的长度(毫米)',min_value=0.0)
            body_mass = st.number_input('身体质量(克)',min_value=0.0)
            submitted=st.form_submit_button('预测分类')
            st.write('用户输入的数据是:')
            st.text([island, sex, bill_length, bill_depth, flipper_length, body_mass])


        island_biscoe,island_dream,island_torgerson = 0,0,0
        if island =='比斯科群岛':
            
            island_dream = 1
        elif island =='德里姆岛':
            island_dream = 1
        elif island == '托尔森岛':
            island_torgerson = 1

        sex_female, sex_male =0, 0
        if sex =='雄性':
            sex_female = 1
        elif sex =='雄性':
            sex_male = 1
        st.write('转换为数据预处理的格式：')
        format_data = [bill_length, bill_depth, flipper_length, body_mass,island_dream, island_torgerson, island_biscoe, sex_male,sex_female]

        st.text (format_data)

        with open('rfc_model.pkl', 'rb') as f:
            rfc_model = pickle.load(f)
        with open ('output_uniques.pkl', 'rb') as f:
            output_uniques_map = pickle.load(f)

        predict_result_code = rfc_model.predict([format_data])

        predict_result_species = output_uniques_map [predict_result_code] [0]
        st.write('根据您输入的数据，预测该企鹅的物种名称是：',predict_result_species)

        
        with col_logo:
            if not submitted:
                
                st.image("https://tse3-mm.cn.bing.net/th/id/OIP-C.v3b_DewOkXIzanKImwXWhgHaHa?w=138&h=180&c=7&r=0&o=7&pid=1.7&rm=3.jpg", caption='企鹅')
            else:
                st.image("https://img95.699pic.com/photo/60084/9702.jpg_wh860.jpg", caption='企鹅')
                
