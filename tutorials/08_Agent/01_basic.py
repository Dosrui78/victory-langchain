from langchain.agents import create_agent
from common.llms import dashscope_LLM as model
from langchain_core.tools import tool

@tool(description="获取天气信息")
def get_weather() -> str:
    # 这里是一个模拟的函数，实际应用中可以调用天气API获取天气信息
    return "明天的天气是晴天，温度25度。"

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="你是一个会说话的人，可以回答用户的问题。", 
)

res = agent.invoke({
    "messages": [
        {"role": "user", "content": "明天深圳的天气如何？"}
    ]
})

for msg in res["messages"]:
    print(type(msg).__name__, msg.content)


"""
基于外部工具的提供，让大模型拥有了：感知外部世界并影响现实的能力。

丰富的工具集将极大提升大模型的工作性能和业务范畴。
工具越多，Agent 能覆盖的业务场景就越广（从客服问答到库存管理，再到自动化运营），性能和实用性自然会大幅提升。
"""
