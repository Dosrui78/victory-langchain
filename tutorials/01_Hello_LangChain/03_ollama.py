from common.logger import logger
from common.llms import ollama_LLM
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

logger.info("开始调用 LLM...")

messages = [
    SystemMessage(content="你是一名爱国诗人"),
    AIMessage(content="国破山河在，城春草木深。感时花溅泪，恨别鸟惊心。"),
    HumanMessage(content="请参照刚才的诗句格式再来一首，只返回诗句即可")
]

response = ollama_LLM.invoke(messages)
logger.info(response.content)
logger.info(f"LLM 回复完毕，内容长度: {len(response.content)}")