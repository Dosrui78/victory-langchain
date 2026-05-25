from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from common.logger import logger
from common.llms import dashscope_LLM


str_parser = StrOutputParser()
json_parser = JsonOutputParser()

first_prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}，请起名，并封装为JSON格式返回给我，"
    "要求key是name，value就是起的名字。请严格按照格式要求返回，不要有其他内容。"
)

second_prompt = PromptTemplate.from_template("请对这个名字{name}进行点评，并给出评分（1-100）。")

chain = first_prompt | dashscope_LLM | json_parser | second_prompt | dashscope_LLM | str_parser
for chunk in chain.stream({"lastname": "李", "gender": "男"}):
    logger.info(f"{chunk}")
