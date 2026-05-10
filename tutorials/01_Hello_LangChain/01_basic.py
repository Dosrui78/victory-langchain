from common.models import dashscope_LLM
from langchain_core.messages import HumanMessage

response = dashscope_LLM.invoke([HumanMessage(content="你好，请介绍一下你自己")])

print(response)