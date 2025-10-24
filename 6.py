import streamlit as st

st.set_page_config(page_title='视频播放器', page_icon='')

videos = 'trailer.mp4'

st.video(videos)

