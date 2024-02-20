from ..utils.llama_cpp_helper import request_llama_cpp
from .base import register_llm

# CHAT_PROMPT_PREFIX = "[INST] <<SYS>>\nYou are a helpful assistant. 你是一个乐于助人的助手。\n<</SYS>>\n\n"
# CHAT_PROMPT_SUFFIX = "[/INST]"
CHAT_PROMPT_PREFIX = ""
CHAT_PROMPT_SUFFIX = ""


def ask_yi_no_prompt(message, url="http://localhost:8020/completion"):
    content = request_llama_cpp(url, {
        "prompt": CHAT_PROMPT_PREFIX+message+CHAT_PROMPT_SUFFIX,
        "n_predict": 256,
    })
    content = content.replace(CHAT_PROMPT_PREFIX, "")
    content = content.replace(CHAT_PROMPT_SUFFIX, "").strip()
    return content


register_llm('yi-no-prompt-6b', ask_yi_no_prompt)
