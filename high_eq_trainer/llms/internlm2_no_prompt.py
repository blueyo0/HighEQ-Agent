from ..utils.llama_cpp_helper import request_llama_cpp
from .base import register_llm
import openai

# CHAT_PROMPT_PREFIX = "[INST] <<SYS>>\nYou are a helpful assistant. 你是一个乐于助人的助手。\n<</SYS>>\n\n"
# CHAT_PROMPT_SUFFIX = "[/INST]"
CHAT_PROMPT_PREFIX = ""
CHAT_PROMPT_SUFFIX = ""


def ask_internlm2_no_prompt(message, url="http://localhost:8040/completion"):
    content = request_llama_cpp(url, {
        "prompt": CHAT_PROMPT_PREFIX+message+CHAT_PROMPT_SUFFIX,
        "n_predict": 256,
    })
    for split in ["[UNUSED_TOKEN_145]", "<|im_end|>", "</s>"]:
        content = content.split(split)[0]

    content = content.replace(CHAT_PROMPT_PREFIX, "")
    content = content.replace(CHAT_PROMPT_SUFFIX, "").strip()

    # base_url = url
    # client = OpenAI(api_key="123456", organization="random",
    #                 base_url=base_url)
    # content = client.chat.completions.create(model="gpt-4", messages=CHAT_PROMPT_PREFIX+message+CHAT_PROMPT_SUFFIX,
    #                                          temperature=0.1,
    #                                          top_p=0.95,
    #                                          presence_penalty=1.1,
    #                                          stop=["</s>", '<|im_end|>',
    #                                                '[UNUSED_TOKEN_145]'],
    #                                          max_tokens=3072,
    #                                          tools=None,
    #                                          seed=110,
    #                                          stream=True)
    # content = content[-1]

    # openai.api_type = "azure"
    # openai.api_base = url
    # openai.api_version = "2023-07-01-preview"
    # openai.api_key = "123456"
    # completion = openai.ChatCompletion.create(
    #     engine="GPT4",
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant."},
    #         {"role": "user", "content": message}
    #     ],
    #     temperature=0.7,
    #     max_tokens=800,
    #     top_p=0.95,
    #     frequency_penalty=0,
    #     presence_penalty=0,
    #     stop=None
    # )
    # content = completion.choices[0].message['content']

    return content


register_llm('internlm2-chat-no-prompt-7b', ask_internlm2_no_prompt)
