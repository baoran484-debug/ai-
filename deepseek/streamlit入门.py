import streamlit as st

st.set_page_config(
    page_title="感动中国十大人物", 
    page_icon=":star:", 
    layout="wide",
    menu_items={
        'Get Help': 'https://www.baidu.com',
        'Report a bug': 'https://www.yandex.com',
        'About': "这是一个感动中国十大人物的展示页面，使用Streamlit框架开发，展示了尹思源的事迹和相关信息。"
    }
)
st.title("感动中国十大人物")
st.header("这是一个内蒙的汉子")
st.subheader("他二十年来一直在，每天三次，已经两万多次了")
st.write("这是尹思源，来自乌兰浩特，有着左手王的称号")
st.image("./resources/ysy.jpg")
student_data = {
    "姓名": ["尹思源","王大爷","李大爷"],
    "年龄": [50, 80, 75],
    "事迹": ["每天三次坚持锻炼，已经两万多次了","每天坚持锻炼，已经三万多次了","每天坚持锻炼，已经一万多次了"]

}
st.table(student_data)
name = st.text_input("请输入姓名")
st.write(f"你输入的姓名是：{name}")
password = st.text_input("请输入密码", type="password")
st.write(f"你输入的密码是：{password}")
gender = st.radio("请选择性别", ["男", "女", "未知"], index=0)
st.write(f"你选择的性别是：{gender}")
