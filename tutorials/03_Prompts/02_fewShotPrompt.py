from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from common.logger import logger
from common.llms import dashscope_LLM

example_prompt = PromptTemplate.from_template("""
姓氏:{surnames}
名人:{Celebrities}
""")

example_data = [
    {"surnames": "诸葛", "Celebrities": "诸葛亮"},
    {"surnames": "张", "Celebrities": "张翼"},
    {"surnames": "朱", "Celebrities": "朱然"},
    {"surnames": "关", "Celebrities": "关羽"},
    {"surnames": "赵", "Celebrities": "赵云"},
    {"surnames": "司马", "Celebrities": "司马懿"},
    {"surnames": "周", "Celebrities": "周瑜"},
    {"surnames": "张", "Celebrities": "张飞"},
    {"surnames": "纪", "Celebrities": "纪灵"},
    {"surnames": "牛", "Celebrities": "牛金"},
    {"surnames": "王", "Celebrities": "王平"},
]

few_shot_prompt = FewShotPromptTemplate(
    examples=example_data,
    example_prompt=example_prompt,
    input_variables=["surnames"],
    prefix="请根据以下示例，输出对应姓氏的三国时期的名人姓名：",
    suffix="姓氏:{surnames}\n名人:"
)

prompt_str = few_shot_prompt.format(surnames="李")
logger.info(f"生成的Few-Shot Prompt: {prompt_str}")
response = dashscope_LLM.invoke([HumanMessage(content=prompt_str)])
logger.info(f"response: {response.content}")
