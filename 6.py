import streamlit as st

st.set_page_config(page_title='视频播放器', page_icon='💿')
st.title('💿视频播放')
videos = [
    {
        'url': 'https://github.com/lanlan814/lanlan1/raw/main/1382788056-1-192.mp4',
        'title': '恶搞之家第一季',
        'episode': '1',
        'name': '主演：petter, louis, meg, stweei'
    },
    {
        'url': 'https://github.com/lanlan814/lanlan1/raw/main/29952639028-1-192.mp4',
        'title': '恶搞之家第一季',
        'episode': '2',
        'name': '主演：petter, louis, meg, stweei'
    },
    {
        'url': 'https://github.com/lanlan814/lanlan1/raw/main/trailer.mp4',
        'title': '恶搞之家第一季',
        'episode': '3',
        'name': '主演：petter, louis, meg, stweei'
    }
]

if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

st.video(videos[st.session_state['ind']]['url'])
st.subheader(videos[st.session_state['ind']]['title'] + '第' + videos[st.session_state['ind']]['episode'] + '集')
st.text(videos[st.session_state['ind']]['title'])
st.text(videos[st.session_state['ind']]['name'])

def play(arg):
    st.session_state['ind'] = int(arg)

for i in range(len(videos)):
    st.button('第' + str(i + 1)+ '集', use_container_width=True, on_click=play, args=([i]))


