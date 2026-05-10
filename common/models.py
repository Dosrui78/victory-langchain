import os
from langchain_openai import ChatOpenAI
from config.config_data import *

def get_model(provider: str = "qwen", model_name: str = None):
    """
    模型工厂函数
    :param provider: 模型供应商，可选 'qwen', 'openai', 'deepseek' 等
    :param model_name: 具体模型名称，如果不传则使用 config 中的默认值
    """
    if provider == "qwen":
        return ChatOpenAI(
            model_name=model_name or MODEL_NAME,    
            temperature=TEMPERATURE,
            api_key=QWEN_API_KEY,
            base_url=QWEN_BASE_URL
        )
    
    elif provider == "openai":
        return ChatOpenAI(
            model_name=model_name or "gpt-4o", 
            temperature=TEMPERATURE,
            api_key=OPENAI_API_KEY,
            base_url=OPENAI_BASE_URL
        )
    
    # 后续可以继续扩展，比如 deepseek
    elif provider == "deepseek":
        return ChatOpenAI(
            model_name=model_name or "deepseek-chat",
            temperature=TEMPERATURE,
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url="https://api.deepseek.com"
        )
    
    else:
        raise ValueError(f"不支持的模型供应商: {provider}")

# common/models.py 底部

# 只有当对应的 Key 存在时才创建实例
dashscope_LLM = get_model("qwen") if QWEN_API_KEY else None

# 注意：这里我们检查 OPENAI_API_KEY 是否存在
openai_LLM = get_model("openai") if OPENAI_API_KEY else None

# 检查 DEEPSEEK_API_KEY 是否存在
deepseek_LLM = get_model("deepseek") if os.getenv("DEEPSEEK_API_KEY") else None
