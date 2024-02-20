from ..utils.llama_cpp_helper import request_llama_cpp
from .base import register_llm

CHAT_PROMPT_PREFIX = "[INST] <<SYS>> You are a helpful assistant. 你是一个乐于助人的助手。<</SYS>> "
CHAT_PROMPT_SUFFIX = "[/INST]"
# CHAT_PROMPT_PREFIX = ""
# CHAT_PROMPT_SUFFIX = ""


def ask_cn_alpaca2(message, url="http://localhost:8010/completion"):
    content = request_llama_cpp(url, {
        "prompt": CHAT_PROMPT_PREFIX+message+CHAT_PROMPT_SUFFIX,
        "n_predict": 128,
    })
    content = content.replace(CHAT_PROMPT_PREFIX, "")
    content = content.replace(CHAT_PROMPT_SUFFIX, "").strip()
    return content


register_llm('chinese-alpaca-2-7b', ask_cn_alpaca2)
