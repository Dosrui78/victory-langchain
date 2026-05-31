from langchain.tools import tool
from langchain.agents import create_agent
from common.llms import dashscope_LLM as model


@tool(description="获取股价，传入股票名称，返回字符串信息")
def get_price(name) -> str:
    # 这里是一个模拟的函数，实际应用中可以调用价格API获取价格信息
    return f"股票{name}的价格是20元。"

@tool(description="获取股票信息，传入股票名称，返回字符串信息")
def get_info(name) -> str:
    # 这里是一个模拟的函数，实际应用中可以调用信息API获取信息
    return f"股票{name}是一家A股上市公司， 专注于IT职业教育。"

agent = create_agent(
    model=model,
    tools=[get_price, get_info],
    system_prompt="你是一个智能助手，可以回答股票相关问题，记住请告知我思考过程，让我知道为什么调用某个工具"
)

for chunk in agent.stream(
    {
        "messages": [
            {"role": "user", "content": "传智教育股价多少，并介绍一下"}
        ]
    },
    stream_mode="values"
):
    lastest_message = chunk["messages"][-1]
    if lastest_message.content:
        print(type(lastest_message).__name__, lastest_message.content)
    
    try:
        if lastest_message.tool_calls:
            print(f"工具调用： {[tc['name'] for tc in lastest_message.tool_calls]}")
    except AttributeError as e:
        pass