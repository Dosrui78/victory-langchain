from langchain.agents import create_agent
from langchain.agents.middleware import (
    # 装饰器
    before_agent, after_agent, before_model, after_model,
    wrap_model_call, wrap_tool_call, AgentState, Runtime
)
from common.llms import dashscope_LLM as model
from langchain_core.tools import tool

@tool(description="获取天气信息，传入城市名称字符串，返回字符串天气信息")
def get_weather(city) -> str:
    # 这里是一个模拟的函数，实际应用中可以调用天气API获取天气信息
    return "晴天。"


"""
1.agent执行前
2.agent执行后
3.model执行前
4.mode1执行后
5.工具执行中
6.模型执行中
"""

@before_agent
def log_before_agent(state: AgentState, runtime: Runtime) -> None:
    # agent执行前会调用这个函数并传入state和runtime两个对象
    print(f"[before agent]agent启动，并附带{len(state["messages"])}消息")

@after_agent
def log_after_agent(state: AgentState, runtime: Runtime) -> None:
    print(f"[after agent]agent结束，并附带{len(state["messages"])}消息")

@before_model
def log_before_model(state: AgentState, runtime: Runtime) -> None:
    print(f"[before model]model即将调用，并附带{len(state["messages"])}消息")

@after_model
def log_after_model(state: AgentState, runtime: Runtime) -> None:
    print(f"[after model]mode调用结束，并附带{len(state["messages"])}消息")

@wrap_model_call
def model_call_hook(request, handler):
    print("模型调用啦！")
    return handler(request)

@wrap_tool_call
def monitor_tool(request, handler):
    print(f"工具执行：{request.tool_call['name']}")
    print(f"工具执行传入参数：{request.tool_call['args']}")

    return handler(request)


agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="你是一个会说话的人，可以回答用户的问题。", 
    middleware=[log_before_agent, log_after_agent, log_before_model, log_after_model, model_call_hook, monitor_tool]
)

res = agent.invoke({"messages": [{"role": "user", "content": "深圳今天的天气如何（如何呀，如何穿衣？）"}]})
print(res)