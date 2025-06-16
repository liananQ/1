import streamlit as st
import pandas as pd

st.set_page_config(page_title='视频',page_icon='🎬')



st.header('🎬视频播放器')

if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

audio_obj = [{
    'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
    'name':'rabbiot',
    'time':'时长：0:10'},
    {
        'url':'https://www.w3schools.com/html/movie.mp4',
        'name':'Bear',
        'time':'时长：0:12'},
    {
        'url':'https://media.w3.org/2010/05/sintel/trailer.mp4',
        'name':'The Blender Foundation',
        'time':'时长：0:52'}]
# 显示视频名称作为标题
st.markdown(f"{audio_obj[st.session_state['ind']]['name']}")
st.markdown(f"{audio_obj[st.session_state['ind']]['time']}")

# 显示视频
st.video(audio_obj[st.session_state['ind']]['url'])

def nextVideo():
    # 点击下一张按钮要做的事
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(audio_obj)

def lastVideo():
    # 点击上一张按钮要做的事
    st.session_state['ind'] = (st.session_state['ind'] - 1)% len(audio_obj)
    
    

c1, c2 = st.columns(2)

with c1:
    st.button('上一个', on_click=lastVideo, use_container_width=True)

with c2:
    st.button('下一个', on_click=nextVideo, use_container_width=True)


















