from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from common.logger import logger
from common.llms import dashscope_LLM

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个边塞诗人，可以作诗。请牢记：你和用户交流时，请用文言文回答。如果用户回复了多行诗句，请用文言文在诗句下方简短评述一下。",
        ),
        MessagesPlaceholder("history"),
        ("human", "好诗好诗，请再来一首唐诗。"),
    ]
)


history_data = [
    ("human", "你来写一首唐诗"),
    ("ai", "床前明月光，疑似地上霜，举头望明月，低头思故乡。"),
    ("human", "好诗好诗，再来一首"),
    ("ai", "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。"),
]

prompt_str = chat_prompt_template.format_messages(history=history_data)
logger.info(f"生成的Chat Prompt: {prompt_str}")
response = dashscope_LLM.invoke(prompt_str)
logger.info(f"response: {response.content}")