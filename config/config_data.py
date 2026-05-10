import os
from dotenv import load_dotenv 
# 自动加载 .env 文件 
load_dotenv() 

# 从环境变量中获取配置项
TEMPERATURE = 0
QWEN_API_KEY = os.getenv("QWEN_API_KEY")
QWEN_BASE_URL = os.getenv("QWEN_BASE_URL")
MODEL_NAME = "qwen3.5-35b-a3b"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")
