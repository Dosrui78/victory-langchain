import os
from dotenv import load_dotenv 
# 自动加载 .env 文件 
load_dotenv() 

# 从环境变量中获取配置项
TEMPERATURE = 0
QWEN_API_KEY = os.getenv("QWEN_API_KEY")
QWEN_BASE_URL = os.getenv("QWEN_BASE_URL")

# 模型列表（依次尝试，失败则切换到下一个）
DEFAULT_QWEN_MODEL = "qwen3.5-122b-a10b"
QWEN_MODEL_LIST = ["deepseek-v4-flash", "qwen3.5-35b-a3b", "qwen3.5-plus", "glm-5.1", "qwen3.6-plus-2026-04-02", "qwen3.6-plus", "MiniMax-M2.5", "qwen3.6-max-preview"]

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")
