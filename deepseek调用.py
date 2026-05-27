# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
#创建于大模型交互的客户端对象（DEEPSEEK APPI_KEY是环境变量，DEEPSEEK_API_KEY是你在DeepSeek平台上申请的API Key）
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")
#与ai大模型交互
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是高鹏，一个乐于助人的人工智能助手。"},
        {"role": "user", "content": "你知道自己刚才说了什么吗？"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)