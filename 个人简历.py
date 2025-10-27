import streamlit as st
from datetime import datetime, time

st.set_page_config(page_title="王者简历生成器", page_icon="", layout="wide")
c1,c2,c3=st.columns(3)
with c1:
    st.subheader('王者个人简历')
    st.markdown('***')
    
    st.write('性别')
    check_1 = st.checkbox('男', value=True)
    check_2 = st.checkbox('女')
    check_3 = st.checkbox('男女共同体')

    song = st.text_input('职位：', '对抗路')

    song = st.text_input('姓名：', '亚瑟')

    st.text_input('段位', placeholder='最强王者')

    st.subheader('账号密码')
    st.text_input('账号', value='123456')
    st.text_input('密码', value='123456', type='password')

    date = st.date_input("入坑日期", value=None)

    w1 = st.time_input("打王者时间")
    options_2 = st.multiselect(
        '爱好',
        ['偷小鸡', '蹭中路线', '支援', '打野', '打小乔'],
        ['偷小鸡'],
        max_selections=2)
    age = st.slider('王者年龄', 0, 10, 7)

    values = st.slider(
        '呐之力数值',
        0.0, 100.0)

    st.text_area(label='个人名言：', placeholder='"真的猛士，敢于直面惨淡的人生，敢于正视淋漓的鲜血。这是怎样的哀痛者和" \
            "幸福者？然而造化又常常为庸人设计，以时间的流驶，来洗涤旧迹，仅使留下" \
            "淡红的血色和微漠的悲哀。在这淡红的血色和微漠的悲哀中，又给人暂得偷生" \
            "，维持着这似人非人的世界。我不知道这样的世界何时是一个尽头"')
    avatatr=st.file_uploader('上传头像',type=['jpg','png'])
    
with c2:
    st.subheader('王者个人简历')
    st.markdown('***')
    st.header('亚瑟')
    st.image("https://ts1.tc.mm.bing.net/th/id/OIP-C.CIvjLd29bmr8x_hB4N4hWQHaEK?rs=1&pid=ImgDetMain&o=7&rm=3.jpg")
    st.write('职位：对抗路')
    st.write('家地址：王者峡谷')
    st.write('王者年龄：7年')
with c3:
    
    st.markdown('***')
    st.write('性别：男')
    st.write('段位：宇宙王者')
    st.write('巅峰分：1000000000')
