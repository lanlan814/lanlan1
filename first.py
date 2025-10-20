import streamlit as st
import pandas as pd
st.title("👻学生小陈👻 数字档案")
st.title("基础信息")
st.text("学号：23031310101    精神状态：癫狂👿  实操能力：微弱 ")
st.markdown(':green[今日想法：今天不学习 明天收垃圾]')
st.markdown('## 个人爱好')
st.markdown('''1.吃饭🥗  2. 睡觉✅ 3. 看电影😎 4.撸猫🐱
''')
st.markdown('# 养猫MVP结算展示')
st.image("D:/1111.jpg",caption="🐱🐱🐱这是我的魔法猫咪悠米，今年1岁了🐱🐱🐱")
st.markdown('# MBTI人格类型')
st.markdown('*:green[活动者]*')
st.markdown('*我对您的工作不感兴趣。我想知道您的痛苦--以及您是否敢于梦想满足自己的内心渴望。*')
st.subheader('能力评估')
c1, c2, c3 = st.columns(3)
c1.metric(label="社交能力", value="150%", delta="50%")
c2.metric(label="收集信息", value="80%", delta="15%")
c3.metric(label="python实操能力解锁进度", value="15%", delta="5%")
data = {
    '10月':['开开心心上课','坚持健身','完成下半年推优入团工作'],
    '11月':['开开心心上课','坚持健身','准备换届'],
    '12月':['开开心心上课','坚持健身','准备放假！！'],
}
st.subheader('💻本年剩余计划')
index = pd.Series(['01', '02', '03'], name='序号')
df = pd.DataFrame(data, index=index)
st.dataframe(df)
st.subheader('🤕今日代码学习展示')
python_code = '''def hello():
    print("你好，Streamlit！")
'''
st.code(python_code, line_numbers=True)
