import streamlit as st
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
