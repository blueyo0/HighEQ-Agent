from ..utils.llama_cpp_helper import request_llama_cpp
from .base import register_llm

# CHAT_PROMPT_PREFIX = "[INST] <<SYS>>\nYou are a helpful assistant. 你是一个乐于助人的助手。\n<</SYS>>\n\n"
# CHAT_PROMPT_SUFFIX = "[/INST]"
CHAT_PROMPT_PREFIX = ""
CHAT_PROMPT_SUFFIX = ""


def ask_cn_alpaca2_no_prompt(message, url="http://localhost:8010/completion"):
    content = request_llama_cpp(url, {
        "prompt": CHAT_PROMPT_PREFIX+message+CHAT_PROMPT_SUFFIX,
        "n_predict": 1024,
    })
    content = content.replace(CHAT_PROMPT_PREFIX, "")
    content = content.replace(CHAT_PROMPT_SUFFIX, "").strip()
    return content


register_llm('chinese-alpaca-2-no-prompt-7b', ask_cn_alpaca2_no_prompt)
