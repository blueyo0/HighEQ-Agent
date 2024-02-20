from ..utils.llama_cpp_helper import request_llama_cpp
from .base import register_llm
import os
import openai


def ask_gpt4(message):

    openai.api_type = "azure"
    openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
    openai.api_version = "2023-07-01-preview"
    openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(
        engine="GPT4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ],
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    content = completion.choices[0].message['content']
    return content


register_llm('gpt-4', ask_gpt4)
