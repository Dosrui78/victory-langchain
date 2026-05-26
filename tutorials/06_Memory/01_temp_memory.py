from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from common.llms import dashscope_LLM

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system", "你是一个会说话的人，可以回答用户的问题。请根据会话历史内容回答问题。对话历史：",
        ),
        MessagesPlaceholder("history"),
        ("human", "请回答这个问题：{input}"),
    ]
)

session_configs = {}

def get_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_configs:
        session_configs[session_id] = InMemoryChatMessageHistory()
    return session_configs[session_id]

def print_prompt(full_prompt: str):
    print("Full prompt: {}".format(full_prompt.to_string()))
    return full_prompt

base_chain = prompt | print_prompt | dashscope_LLM | StrOutputParser()

chat_with_memory = RunnableWithMessageHistory(
    base_chain, 
    get_history,
    input_messages_key="input",
    history_messages_key="history",
)

session_config = {"configurable": {"session_id": "1"}}

res = chat_with_memory.invoke({"input": "小明有两块钱"}, config=session_config)
print("第一次对话:", res)

res = chat_with_memory.invoke({"input": "小明又有三块钱了"}, config=session_config)
print("第二次对话:", res)

res = chat_with_memory.invoke({"input": "小明现在有多少钱？"}, config=session_config)
print("第三次对话:", res)