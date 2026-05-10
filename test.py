from langchain.prompts import load_prompt

# 1. 加载 YAML 文件
# 注意：确保安装了 PyYAML 库 (uv add pyyaml)
prompt_template = load_prompt("configs/prompts/translator.yaml")

# 2. 查看加载后的类型
print(type(prompt_template))

# 3. 填充变量并生成 Prompt
formatted_prompt = prompt_template.format_messages(
    language="意大利语",
    text="你好，今天天气真不错。"
)

print(formatted_prompt)
