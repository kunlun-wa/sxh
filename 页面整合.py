import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np

page = st.sidebar.selectbox("选择页面", ["音乐播发器", "王者个人简历", "视频","美食地址","学生档案"])

if page == "音乐播发器":
    st.set_page_config(page_title='音乐',page_icon='🎵')
    music = [
        {'url':'https://music.163.com/song/media/outer/url?id=2757544444.mp3',
         'photo':'http://p1.music.126.net/Snu9SMBRxB9k-OuKS1LbYw==/109951172181785487.jpg?param=130y130',
         'name':'开始懂了'},
        {'url':'https://music.163.com/song/media/outer/url?id=2600493765.mp3',
          'photo':'http://p2.music.126.net/1XNXI-PlmlIQAWSV8MCFxg==/109951163375899858.jpg?param=130y130',
         'name':'Young Again'},
        {'url':'https://music.163.com/song/media/outer/url?id=174956.mp3',
         'photo':'http://p2.music.126.net/a82aXr_eNkbFX0BkXuKvgg==/109951172050962571.jpg?param=130y130',
         'name':'坏女孩'}]
    if 'ind' not in st.session_state:
        st.session_state['ind']=0


    def nextImg():
        st.session_state['ind']=(st.session_state['ind']+1)%len(music)
    def prevImg():
        st.session_state['ind']=(st.session_state['ind']-1)%len(music)
    a1,a2=st.columns([1,2])
    with a1:
        st.image(music[st.session_state['ind']]['photo'])
    with a2:
        st.text(music[st.session_state['ind']]['name'])
   

    st.audio(music[st.session_state['ind']]['url'])
    c1,c2=st.columns(2)
    with c1:
        st.button('上一首',on_click=nextImg,use_container_width=True)
    with c1:
        st.button('下一首',on_click=nextImg,use_container_width=True)


elif page == "王者个人简历":
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

        name = st.text_input('姓名', autocomplete='name')

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
        st.write(f'性别：男')
        st.write('段位：宇宙王者')
        st.write('巅峰分：1000000000')

elif page == "视频":
    st.set_page_config(page_title='视频',page_icon='📽')
    video_url = [
        {'url':'https://v6.huanqiucdn.cn/4394989evodtranscq1500012236/15fe93f15145403703282112615/v.f100830.mp4',
         'title':'新闻联播',
         'episode':'第1集',
         'time':'2025年10月25日'},
        {'url':'https://v6.huanqiucdn.cn/4394989evodtranscq1500012236/d785c9045145403703281789525/v.f100830.mp4',
          'title':'新闻联播',
         'episode':'第2集',
        'time':'2025年10月25日'},
       {'url':'https://v6.huanqiucdn.cn/4394989evodtranscq1500012236/82f434005145403703273697144/v.f100830.mp4',
         'title':'新闻联播',
         'episode':'第3集',
         'time':'2025年10月25日'},
        {'url':'https://v2.cri.cn/cb5a6d96-d0c4-4fd0-a895-b6135667d84a/video/02acc62728ba4179bf3f8d0de80cda42.mp4',
         'title':'新闻联播',
         'episode':'第4集',
         'time':'2025年10月25日'},
        {'url':'https://v6.huanqiucdn.cn/4394989evodtranscq1500012236/c7034c585145403703162061982/v.f100830.mp4',
         'title':'新闻联播',
         'episode':'第5集',
         'time':'2025年10月25日'}
       ]
    if 'ind' not in st.session_state:
        st.session_state['ind']=0
    st.title(video_url[st.session_state['ind']]['title'])
    st.header(video_url[st.session_state['ind']]['episode'])
    st.text(video_url[st.session_state['ind']]['time'])
    st.video(video_url[st.session_state['ind']]['url'])


    df=st.columns(4)
    di=min(4,len(video_url))
    def play(arg):
        st.session_state['ind']=int(arg)
    for i in range(len(video_url)):
        col_index=i%di
        with df[col_index]:
            st.button(f'第{i+1}集',use_container_width=True,on_click=play,args=(i,))
elif page == "美食地址":
    
    st.title('价格表')
    data = {
        '肯德基':[50,48,48,49,47,45,49,51,52,49,52,65],
        '肯德基':[51,56,56,49,57,53,48,51,56,58,59,59],
        '陈健东龙虾馆':[125,126,145,126,158,142,125,156,145,125,125,126],
        '广顺牛巴王粉店':[15,12,12,13,14,16,12,15,14,12,12,15],
        '东门白切鸡':[104,109,165,126,135,156,123,154,124,109,120,123]
    }
    df = pd.DataFrame(data)

    index = pd.Series(['1月', '2月', '3月','4月','5月','6月','7月','8月','9月','10月','11月','12月'],name='月份')
    df.index=index

    st.dataframe(df)

    st.title('价格走势')
    st.line_chart(df)
    st.title('评分')
    st.bar_chart(df)

    map_data={
        'latitude':[22.830435,22.823132,22.822598,22.820689,22.816610],
       'longitude':[108.370938,108.377450,108.378367,108.377514,108.375932]
        }
    st.map(pd.DataFrame(map_data))

elif page == "学生档案":


    st.title("🕶️ 学生 小涵 - 数字档案")




    st.header("🔑 基础信息")

    st.text("学生ID: NEO-2023-001")

    st.markdown("**注册时间**: `2023-10-01 08:30:17` | **精神状态**: ✅ 正常")

    st.markdown("**当前教室**: `实训楼301` | **安全等级**: `绝密`")





    st.header("📊 技能矩阵")

    col1, col2, col3 = st.columns(3)

    col1.metric("C语言", "95%", "2%", help="近期训练提升") 

    col2.metric("Python", "87%", "-1%")

    col3.metric("Java", "68%", "-10%", help="用则进废则退")




    st.subheader("Streamlit课程进度")

    st.progress(28, text="Streamlit课程进度")




    st.header("📝 任务日志")

    mission_data = {

        "日期": ["2023-10-01", "2023-10-05", "2023-10-12"],

        "任务": ["学生数字档案", "课程管理系统", "数据图表展示"],

        "状态": ["✅ 完成", "🕒 进行中", "❌ 未完成"],

        "难度": ["★☆☆☆☆", "★★☆☆☆", "★★★☆☆"]

    }

    mission_df = pd.DataFrame(mission_data)

    st.table(mission_df.style.applymap(

        lambda x: 'color: #0f0' if x == "✅ 完成" else 'color: #ff0')

    )



    st.subheader("🔐 最新代码成果")

    st.code('''def matrix_breach():

        while True:

            if detect_vulnerability():

                exploit()

                return "ACCESS GRANTED"

            else:

                stealth_evade()''', language='python')





    st.write("---")

    st.write("`>> SYSTEM MESSAGE:` 下一个任务目标已解锁...")

    st.write("`>> TARGET:` 课程管理系统")

    st.write("`>> COUNTDOWN:`", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))



    st.markdown("""

    系统状态: 在线

    连接状态: 已加密

    """)



