from langchain_core.runnables import  RunnableSerializable
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from common.llms import dashscope_LLM

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system",  "你是一个边塞诗人，可以作诗。请牢记：你和用户交流时，请用文言文回答。如果用户回复了多行诗句，请用文言文在诗句下方简短评述一下。"),
        MessagesPlaceholder("history"),
        ("human", "好诗好诗，请再来一首唐诗。"),
    ]
)

history_data = [
    ("human", "你来写一首唐诗"),
    ("ai", "床前明月光，疑似地上霜，举头望明月，低头思故乡"),
    ("human", "好诗好诗，再来一首"),
    ("ai", "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
]

# 组成链，要求每一个组件都是Runnable接口的子类
chain: RunnableSerializable = chat_prompt_template | dashscope_LLM

for chunk in chain.stream({"history": history_data}):
    print(chunk.content, end="", flush=True)
