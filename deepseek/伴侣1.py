import streamlit as st
import os
from openai import OpenAI
print("重新加载了页面")
st.set_page_config(
    page_title="高鹏", 
    page_icon="🤣", 
    layout="wide",
    initial_sidebar_state="expanded",#设置侧边栏初始状态
    menu_items={
        'Get Help': 'https://www.baidu.com',
        'Report a bug': 'https://www.yandex.com',
        'About': "我是高鹏一个迷人的混蛋"
    }
)

st.logo("./resources/logo.jpg")
system_prompt = """
 你叫%s,你每次回答问题都只能回复几句,要匹配用户的语言,严格符合你的性格
    你的性格是%s
"""
#初始化聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = []
#初始化昵称和性格
if "name" not in st.session_state:
    st.session_state.name = "高鹏"
if "nature" not in st.session_state:
    st.session_state.nature = "一个迷人的混蛋"
#显示聊天记录
for message in st.session_state.messages:#{"role": "user", "content": prompt}形式的消息记录
    if message["role"] == "user":
        st.chat_message("😗").write(message["content"])
    else:
        st.chat_message("👨🏿‍🦲").write(message["content"])

# DeepSeek API Key 支持本地环境变量和 Streamlit Secrets
deepseek_api_key = os.environ.get('DEEPSEEK_API_KEY') or st.secrets.get('DEEPSEEK_API_KEY')
if not deepseek_api_key:
    st.error("请在本地环境变量 DEEPSEEK_API_KEY 或 Streamlit Secrets 中配置 DeepSeek API Key。")
    st.stop()

#创建于大模型交互的客户端对象
client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")
#左侧的侧边栏
with st.sidebar:
    st.subheader("设置")
    #姓名输入框
    name=st.text_input("昵称",placeholder="请输入昵称",value=st.session_state.name)
    if name not in st.session_state.name:
        st.session_state.name = name
    #性格输入框
    nature = st.text_input("性格",placeholder="请输入性格",value=st.session_state.nature)
    if nature not in st.session_state.nature:
        st.session_state.nature = nature
    
    
#输入框
prompt = st.chat_input("请输入你的问题：")
if prompt:
    #将用户输入添加到聊天记录中
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("😗").write(prompt)
    #调用高鹏助手接口获取回答
    response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": system_prompt % (st.session_state.name, st.session_state.nature)},#系统提示，告诉大模型它的名字和性格
        #{"role": "user", "content": prompt},
        *st.session_state.messages#解包聊天记录中的消息，作为输入提供给大模型
    ],
    stream=True,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
    )
    #非流式处理大模型返回的结果
        #st.chat_message("👨🏿‍🦲").write(response.choices[0].message.content)
    #流式处理大模型返回的结果
    response_message = st.empty()#占位符，用于后续更新大模型返回的结果
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("👨🏿‍🦲").write(full_response)#实时更新大模型返回的结果
    #打印大模型返回的结果
    print("大模型返回的结果", full_response)
    #将助手的回答添加到聊天记录中
    st.session_state.messages.append({"role":"assistant", "content": full_response})
    

