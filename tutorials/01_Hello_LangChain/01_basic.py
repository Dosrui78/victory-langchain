from common.logger import logger
from common.llms import dashscope_LLM
from langchain_core.messages import HumanMessage

logger.info("开始调用 LLM...")
response = dashscope_LLM.invoke([HumanMessage(content="你好，请介绍一下你自己")])
logger.info(f"LLM 回复完毕，内容长度: {len(response.content)}")