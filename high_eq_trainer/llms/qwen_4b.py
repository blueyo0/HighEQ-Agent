from ..utils.llama_cpp_helper import request_llama_cpp
from .base import register_llm


def ask_qwen_4b(message, url="http://localhost:8031/completion"):
    content = request_llama_cpp(url, {
        "prompt": message,
        "n_predict": 128,
        "temperature": 0.3,
        "top_p": 0.3,
        "repeat_penalty": 1.05,
    })
    return content.strip()


register_llm('qwen-chat-4b', ask_qwen_4b)
