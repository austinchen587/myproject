import os
from openai import OpenAI

# 将API Key直接传入，不通过环境变量
api_key = "sk-93bd1beb96d2486f987f3efc2f7b0a04"

# 创建OpenAI客户端
client = OpenAI(
    api_key=api_key,  # 直接传入API Key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 你的API服务URL
)

# 请求生成聊天回复
completion = client.chat.completions.create(
    model="qwen-plus",  # 模型名称，按需更换
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': '你是谁？'}  # 用户输入的问题
    ]
)

# 打印返回的聊天结果
print(completion.model_dump_json())  # 以JSON格式输出聊天结果