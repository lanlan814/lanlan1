import streamlit as st

st.set_page_config(page_title='🏝罗德岛干员简历生成器',layout='wide')
st.title('🏝罗德岛个人简历生成器')

a1, a2 = st.columns([1, 2])

with a1:
    photo = st.file_uploader("上传干员照片", type=["jpg", "png", "jpeg"])
    name = st.text_input('姓名')
    position = st.text_input('职位')
    phone = st.text_input('电话')
    email = st.text_input('邮箱')
    birth_date = st.date_input('出生日期', value=st.session_state.get('birth_date', None))
    character = st.text_input('特性')
    gender = st.radio('性别', ['男', '女', '其他'], index=0)
    race = st.selectbox('种族', ['龙', '奇美拉', '斐迪亚', '德拉克', '苇林', '乌萨斯', '阿戈尔', '未公开/不公开'])
    infection = st.radio('矿石病感染情况', ['非感染者', '感染者', '未公开/不公开'])
    force = st.selectbox('所属势力', ['罗德岛', '龙门', '哥伦比亚', '莱塔尼亚', '谢拉格', '维多利亚', '企鹅物流', '深海猎人', '乌萨斯', '莱茵生命', '...'])
    combat_exp = st.number_input('战斗经验(年)', min_value=0, max_value=500, value=0)
    my_range = range(1, 50)
    numbers = st.select_slider('源石技艺掌握程度', options=my_range, value=5)
    personal_intro = st.text_area('个人简介')
    personal_1 = st.text_area('档案资料一')
    personal_2 = st.text_area('档案资料二')
    personal_3 = st.text_area('档案资料三')
    personal_4 = st.text_area('档案资料四')

with a2:
    st.header('实时浏览')
    if photo:
        st.image(photo, caption="干员照片", width=300)
    info_col1, info_col2 = st.columns(2)
    with info_col1:
        st.write(f"**姓名:** {name}")
        st.write(f"**职位:** {position}")
        st.write(f"**电话:** {phone if phone else '未填写'}")
        st.write(f"**邮箱:** {email if email else '未填写'}")
        st.write(f"**出生日期:** {birth_date.strftime('%Y/%m/%d') if birth_date else '未填写'}")
        st.write(f"**特性:** {character}")
    with info_col2:
        st.write(f"**性别:** {gender}")
        st.write(f"**种族:** {race}")
        st.write(f"**所属势力:** {force}")
        st.write(f"**矿石病感染情况:** {infection}")
        st.write(f"**战斗经验:** {combat_exp}年")
        st.write(f"**源石技艺掌握程度:** {numbers}")
    st.header("🚓个人简介")
    st.write(personal_intro)
    st.header("档案资料一")
    st.write(personal_1)
    st.header("档案资料二")
    st.write(personal_2)
    st.header("档案资料三")
    st.write(personal_3)
    st.header("档案资料四")
    st.write(personal_4)
    
    




    
