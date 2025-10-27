import streamlit as st

st.title('主页')
st.subheader('🏍点击左侧页面导航至其他实训作业')
images = [
    {'url':"https://github.com/lanlan814/lanlan1/raw/main/2121.png", 'parm':"求放过"},
    {'url':"https://github.com/lanlan814/lanlan1/raw/main/1212.jpg", 'parm':"求求放过"}
    ]
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

def last_Img():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(images)

def next_Img():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)

st.image(images[st.session_state['ind']]['url'], caption=images[st.session_state['ind']]['parm'])
st.button('上一张', on_click=last_Img, use_container_width=True)
st.button('下一张', on_click=next_Img, use_container_width=True)
