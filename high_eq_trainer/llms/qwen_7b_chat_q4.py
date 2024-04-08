import os
import sys
os.environ['http_proxy'] = ''
os.environ['https_proxy'] = ''
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# from utils.llama_cpp_helper import request_llama_cpp
# from base import register_llm
from ..utils.llama_cpp_helper import request_llama_cpp
from .base import register_llm

# CHAT_PROMPT_PREFIX = "[INST] <<SYS>>\nYou are a helpful assistant. 你是一个乐于助人的助手。\n<</SYS>>\n\n"
# CHAT_PROMPT_SUFFIX = "[/INST]"
CHAT_PROMPT_PREFIX = ""
CHAT_PROMPT_SUFFIX = ""


def ask_qwen_7b_chat(message, url="http://localhost:8030/completion"):
    content = request_llama_cpp(url, {
        "prompt": CHAT_PROMPT_PREFIX+message+CHAT_PROMPT_SUFFIX,
        "n_predict": 128,
        "temperature": 0.3,
        "top_p": 0.3,
        "repeat_penalty": 1.05,
    })
    content = content.replace(CHAT_PROMPT_PREFIX, "")
    content = content.replace(CHAT_PROMPT_SUFFIX, "").strip()
    return content

register_llm('qwen_7b_chat_q4', ask_qwen_7b_chat)

if __name__ == "__main__":
    url = "http://localhost:8030/completion"
    # 创建一个json对象
    data = {
        "prompt": "用中文回答：中国最高的山是？",
        "n_predict": 128,
    }
    res = request_llama_cpp(url, data)
    print(res)

