import streamlit as st

st.set_page_config(page_title='英雄联盟原画', page_icon='⚜️')
images = [
    {'url': "https://cdn.oneesports.gg/cdn-data/2023/06/LeagueofLegends_SoulFighterLux_Skin_SplashArt.jpg", 'parm': '斗魂拉克丝'},
    {'url': "https://www.vpesports.com/wp-content/uploads/2025/10/Sett-in-League-of-Legends.png", 'parm': '灵魂莲华腕豪'},
    {'url': "http://img.netbian.com/file/2024/0212/114343vbsL7.jpg", 'parm': '青花瓷艾瑞莉娅'},
    {'url': "https://staticg.sportskeeda.com/editor/2022/11/41681-16684477596143-1920.jpg", 'parm': '北极星戴安娜'},
    {'url': "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Aphelios_0.jpg", 'parm': '原皮厄斐琉斯'},
    {'url': "https://img.52desk.com/tp/85ec7bc9825fdf66913c5531c14675b1.jpg",'parm':'原皮女坦'},
    {'url': "https://img.clinicmed.net/uploadimg/image/20200819/20200819150723_98557.jpg", 'parm': '原皮永恩'}
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
