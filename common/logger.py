import logging
import sys
import os
from datetime import datetime

# 获取项目根目录并创建日志文件夹
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

class ColoredFormatter(logging.Formatter):
    """自定义彩色日志格式"""
    
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    blue = "\x1b[34;20m"
    reset = "\x1b[0m"
    format_str = "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format_str + reset,
        logging.INFO: blue + format_str + reset,
        logging.WARNING: yellow + format_str + reset,
        logging.ERROR: red + format_str + reset,
        logging.CRITICAL: bold_red + format_str + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%H:%M:%S')
        return formatter.format(record)

def setup_logger(name="Victory"):
    logger = logging.getLogger(name)
    
    # 避免重复设置
    if logger.handlers:
        return logger
        
    logger.setLevel(logging.INFO)

    # 1. 控制台 Handler (带颜色)
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(ColoredFormatter())
    logger.addHandler(ch)

    # 2. 文件 Handler (纯文本)
    log_filename = os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.log")
    fh = logging.FileHandler(log_filename, encoding='utf-8')
    file_formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s')
    fh.setFormatter(file_formatter)
    logger.addHandler(fh)

    return logger

# 创建全局 logger 实例
logger = setup_logger()
