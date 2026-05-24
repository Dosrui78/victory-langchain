import os
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from config.config_data import *
from common.logger import logger
from langchain_core.callbacks import BaseCallbackHandler

class ModelLoggingHandler(BaseCallbackHandler):
    """自定义回调：在模型开始运行时打印模型名"""
    def on_llm_start(self, serialized, prompts, **kwargs):
        # 从 invocation_params 中提取模型名称
        params = kwargs.get("invocation_params", {})
        model_name = params.get("model_name", "未知模型")
        logger.info(f"🚀 正在发送请求到模型: {model_name}")


def _require_api_key(provider: str, api_key):
    """确保传入 ChatOpenAI 的 key 是非空字符串，避免底层 SDK 报错过深。"""
    if not isinstance(api_key, str):
        raise ValueError(
            f"{provider} API Key 必须是字符串，当前收到: {type(api_key).__name__}"
        )

    api_key = api_key.strip()
    if not api_key:
        raise ValueError(f"{provider} API Key 未配置，请检查 .env 或环境变量")

    return api_key



def get_model(provider: str = "qwen", model_name: str = None):
    """基础模型初始化函数"""
    # 实例化回调处理器
    callbacks = [ModelLoggingHandler()]
    
    if provider == "qwen":
        return ChatOpenAI(
            model_name=model_name or DEFAULT_QWEN_MODEL,
            temperature=TEMPERATURE,
            api_key=_require_api_key("Qwen", QWEN_API_KEY),
            base_url=QWEN_BASE_URL,
            callbacks=callbacks
        )
    elif provider == "openai":
        return ChatOpenAI(
            model_name=model_name or "gpt-4o",
            temperature=TEMPERATURE,
            api_key=_require_api_key("OpenAI", OPENAI_API_KEY),
            base_url=OPENAI_BASE_URL,
            callbacks=callbacks
        )
    elif provider == "deepseek":
        return ChatOpenAI(
            model_name=model_name or "deepseek-chat",
            temperature=TEMPERATURE,
            api_key=_require_api_key("DeepSeek", os.getenv("DEEPSEEK_API_KEY")),
            base_url="https://api.deepseek.com",
            callbacks=callbacks
        )
    elif provider == "ollama":
        return ChatOllama(
            model=model_name or Ollama_MODEL, 
            base_url=Ollama_BASE_URL,
            callbacks=callbacks
        )
    else:
        raise ValueError(f"不支持的供应商: {provider}")

def get_fallback_llm(model_names: list, provider: str = "qwen"):
    """
    创建一个具备自动切换功能的 LLM 链
    """
    if not model_names:
        raise ValueError("模型列表不能为空")

    # 1. 批量初始化所有模型
    llm_instances = [get_model(provider, name) for name in model_names]

    # 2. 将第一个作为主模型，后续作为备份
    main_llm = llm_instances[0]
    fallback_llms = llm_instances[1:]

    # 打印启动日志
    logger.info(f"✅ 已配置模型链路: {model_names[0]} (主) -> {' -> '.join(model_names[1:])} (备)")
    
    return main_llm.with_fallbacks(fallback_llms)

# --- 实际调用实例 ---

# 获取一个“永不宕机”的模型实例
dashscope_LLM = get_fallback_llm(QWEN_MODEL_LIST, provider="qwen")

# 其他模型检查 Key 存在性
openai_LLM = get_model("openai") if OPENAI_API_KEY else None
deepseek_LLM = get_model("deepseek") if os.getenv("DEEPSEEK_API_KEY") else None
ollama_LLM = get_model("ollama")
