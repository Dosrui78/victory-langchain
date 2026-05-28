import os
import json
from typing import List, Sequence
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import BaseMessage, message_to_dict, messages_from_dict
from common.llms import dashscope_LLM as model

class FileMessageHistory:
    def __init__(self, session_id: str, storage_path: str):
        self.session_id = session_id
        self.storage_path = storage_path
        self.file_path = os.path.join(self.storage_path, f"{session_id}.json")
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def add_messages(self, message: Sequence[BaseMessage]):
        all_messages = list(self.messages)
        all_messages.extend(message)

        new_messages = [message_to_dict(msg) for msg in all_messages]
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(new_messages, f)

    @property
    def messages(self) -> list[BaseMessage]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                messages = json.load(f)
                return messages_from_dict(messages)
        except FileNotFoundError:
            return []
        
    def clear(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([], f)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个会说话的人，可以回答用户的问题。请根据会话历史内容回答问题。对话历史："),
        MessagesPlaceholder("chat_history"),
        ("human", "请回答这个问题：{input}"),
    ]
)

def get_history(session_id: str):
    return FileMessageHistory(session_id, "./chat_history")

def print_prompt(full_prompt):
    print("=" * 20, full_prompt.to_string(), "=" * 20)
    return full_prompt

base_chain = prompt | print_prompt | model | StrOutputParser()

chain_with_memory = RunnableWithMessageHistory(
    base_chain, 
    get_history, 
    input_messages_key="input", 
    history_messages_key="chat_history"
)

session_config = {"configurable": {"session_id": "1"}}

res = chain_with_memory.invoke({"input": "小明有两块钱"}, config=session_config)
print("第一次对话:", res)

res = chain_with_memory.invoke({"input": "小明又有三块钱了"}, config=session_config)
print("第二次对话:", res)

res = chain_with_memory.invoke({"input": "小明现在有多少钱？"}, config=session_config)
print("第三次对话:", res)
