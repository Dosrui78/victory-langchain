from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from common.logger import logger
from common.llms import dashscope_LLM

template = """
你是一位经验丰富的地理老师。请查询位于【{province}】的【{city}】对应的车牌代码简称。
如果【{city}】为空（例如直辖市），请直接返回该省份/直辖市每个简称对应的是该市的哪个区。
请简略输出，如果【{city}】不为空，仅仅输出简称即可，若为空用JSON格式输出对应关系"""

prompt = PromptTemplate.from_template(template)
prompt_str = prompt.format(province="北京", city="")
logger.info(f"生成的Prompt: {prompt_str}")

response = dashscope_LLM.invoke([HumanMessage(content=prompt_str)])
logger.info(f"response: {response.content}")
logger.info(f"LLM 回复完毕，内容长度: {len(response.content)}")