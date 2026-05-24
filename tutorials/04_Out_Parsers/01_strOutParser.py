from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from common.logger import logger
from common.llms import dashscope_LLM


def build_prompt(user_input: str) -> PromptTemplate:
    """构造用于模型调用的 Prompt 模板。"""
    prompt = PromptTemplate.from_template(
        """请根据以下提示，输出一个字符串：
提示: {input}
输出:"""
    )
    return prompt


def main() -> str:
    parser = StrOutputParser()
    prompt = build_prompt(
        "请输出一个关于人工智能的名言，要求简洁且不要解释。"
    )

    logger.info(f"生成的 Prompt:\n{prompt}")

    chain = prompt | dashscope_LLM | parser | dashscope_LLM | parser
    res: str = chain.invoke(HumanMessage(content=prompt.format(input="请输出一个关于人工智能的名言，要求简洁且不要解释。")))

    return res


if __name__ == "__main__":
    print(main())
