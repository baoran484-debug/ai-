import streamlit as st
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
