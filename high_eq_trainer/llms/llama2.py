from ..utils.llama_cpp_helper import request_llama_cpp
from .base import register_llm


def ask_llama2_chat(message, url="http://localhost:8000/completion"):
    chat_prompt_prefix = "[INST] <<SYS>>\n{{  You are a helpful assistant.  }}\n<</SYS>>\n\n{{  "
    chat_prompt_suffix = "  }}[/INST]"
    content = request_llama_cpp(url, {
        "prompt": chat_prompt_prefix+message+chat_prompt_suffix,
        "n_predict": 128,
    })
    content = content.replace(chat_prompt_prefix, "")
    content = content.replace(chat_prompt_suffix, "").strip()
    return content


register_llm('llama-2-7b-chat', ask_llama2_chat)


def ask_llama2(message, url="http://localhost:8001/completion"):
    chat_prompt_prefix = ""
    chat_prompt_suffix = ""
    content = request_llama_cpp(url, {
        "prompt": chat_prompt_prefix+message+chat_prompt_suffix,
        "n_predict": 128,
    })
    content = content.replace(chat_prompt_prefix, "")
    content = content.replace(chat_prompt_suffix, "").strip()
    return content


register_llm('llama-2-7b', ask_llama2)


def ask_yi_chat(message, url="http://localhost:8020/completion"):
    chat_prompt_prefix = "[INST] <<SYS>>\n{{  You are a helpful assistant.  }}\n<</SYS>>\n\n{{  "
    chat_prompt_suffix = "  }}[/INST]"
    content = request_llama_cpp(url, {
        "prompt": chat_prompt_prefix+message+chat_prompt_suffix,
        "n_predict": 128,
    })
    content = content.replace(chat_prompt_prefix, "")
    content = content.replace(chat_prompt_suffix, "").strip()
    return content


# register_llm('yi-6b-chat', ask_yi_chat)
