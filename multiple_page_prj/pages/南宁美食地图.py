import streamlit as st

st.title('实训作业3：美食地图导航')

import pandas as pd
import numpy as np

st.title("🤩🤩南宁市美食地图导航🤩🤩")
st.title("😋各餐厅评分数据")
data = {
    '门店':['阪一烧肉饭','舒记粉店','重庆小面','莱茉莉','万福小食'],
    '评分':[5.0, 4.2, 5.0, 4.8, 4.7],
    }
df = pd.DataFrame(data)
index = pd.Series([1, 2, 3, 4, 5], name='评分')
st.subheader("各门店评分对比")
st.bar_chart(df, x='门店')
df.set_index('门店', inplace=True)

data = {
    '月份':['01月', '02月', '03月','04月','05月','06月','07月','08月','09月','10月','11月','12月'],
    '阪一烧肉饭':[200, 300, 170, 150, 180, 220, 230, 280, 300, 150, 175, 160],
    '舒记粉店':[250, 180, 150, 180, 120, 150, 180, 160, 150, 170, 180, 175],
    '重庆小面':[150, 100, 180, 175, 190, 210, 220, 210, 240, 240, 200, 120],
    '莱茉莉':[200, 190, 170, 120, 150, 160, 200, 180, 170, 230, 210, 150],
    '万福小食':[200, 180, 170, 170, 180, 190, 200, 210, 180, 190, 110, 120],
    }

df = pd.DataFrame(data)
index = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], name='序号')
df.index = index
st.header("👑各门店本年度销售数据")
st.write(df)
st.header("折线图")
st.subheader("门店月度销售额走势对比")
st.line_chart(df, x='月份')


st.header("👑各门店各月度销售数据对比")
st.write(df)
st.header("条形图对比")

st.subheader("各月份对比")
st.bar_chart(df, x='月份')

df.set_index('月份', inplace=True)

st.subheader("👑门店销售额各月份对比")
st.bar_chart(df, y='阪一烧肉饭')
st.bar_chart(df, y='舒记粉店')
st.bar_chart(df, y='重庆小面')
st.bar_chart(df, y='莱茉莉')
st.bar_chart(df, y='万福小食')

st.header("👑各门店本年度销售数据")
df = pd.DataFrame(data)
index = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], name='序号')
df.index = index
st.write(df)
st.header("面积图对比")
st.subheader("各门店销售额面积图对比")

st.area_chart(df, x='月份')

df.set_index('月份', inplace=True)

st.subheader("各门店对比")
st.area_chart(df, y='阪一烧肉饭')
st.area_chart(df, y=['舒记粉店','万福小食'])


st.header("🍽门店位置分布")
map_data = {
    'latitude':[22.813838,22.798278,22.854184,22.812222,22.810131],
    'longitude':[108.384878,108.337854,108.222595,108.329515,108.329166],
    }
st.map(pd.DataFrame(map_data))
