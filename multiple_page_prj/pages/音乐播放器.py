import streamlit as st

st.title('实训作业5：音乐播放器')

import streamlit as st

st.set_page_config(page_title='个人歌单', page_icon='🎵')

music = [
    {
        'url': "https://music.163.com/song/media/outer/url?id=2666095018.mp3",
        'name': "日落",
        'singer': "歌手：孙燕姿",
        'time': "时长：4:09",
        'photo': "https://p1.music.126.net/Z6rUwSkXwS_cn8AB7KqBaw==/109951170378435887.jpg"
    },
    {
        'url': "https://music.163.com/song/media/outer/url?id=40140636.mp3",
        'name': "习惯失恋(Live In Hong Kong/2015)",
        'singer': "歌手：容祖儿",
        'time': "时长：4:00",
        'photo': "https://p2.music.126.net/7mAfTwgkh4Hd8P6B9nj4_A==/109951170708307621.jpg"
    },
    {
        'url': "https://music.163.com/song/media/outer/url?id=34578286.mp3",
        'name': "载我回家",
        'singer': "歌手：张悬",
        'time': "时长：3:41",
        'photo': "https://p2.music.126.net/cpoUinrExafBHL5Nv5iDHQ==/109951166361218466.jpg"
    }
]

if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

def last_audio():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(music)

def next_audio():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(music)

a1, a2 = st.columns([1, 2])

with a1:
    st.image(music[st.session_state['ind']]['photo'])
with a2:
    st.title(music[st.session_state['ind']]['name'])
    st.header(music[st.session_state['ind']]['singer'])
    st.text(music[st.session_state['ind']]['time'])
    st.audio(music[st.session_state['ind']]['url'], autoplay=True)

c1,c2 = st.columns(2)
with c1:
    st.button('上一首', on_click=last_audio, use_container_width=True)
with c2:
    st.button('下一首', on_click=next_audio, use_container_width=True)
