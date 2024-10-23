import os
from openai import OpenAI
import json

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key="sk-84d065108b544f8385ffc6c9f369cde1",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
completion = client.chat.completions.create(
    model="qwen-plus",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    messages=[
        {'role': 'system', 'content': ''},
        {'role': 'user', 'content': '分析网页中的内容，总结为要点，列出来:  https://mp.weixin.qq.com/s/pvtMdJluiEth4wxM0ypMgA'}],
)

result = completion.model_dump_json()



data = json.loads(result)

print(data['choices'][0]['message']['content'])