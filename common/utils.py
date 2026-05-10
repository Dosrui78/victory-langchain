# common/utils.py
from pathlib import Path
from langchain_core.prompts import load_prompt

def get_prompt_by_name(name: str):
    """
    根据文件名快速获取 configs/prompts/ 下的 prompt
    """
    prompt_path = Path("config") / "prompts" / f"{name}.yaml"
    if not prompt_path.exists():
        raise FileNotFoundError(f"未找到 Prompt 配置文件: {prompt_path}")
    return load_prompt(prompt_path)
