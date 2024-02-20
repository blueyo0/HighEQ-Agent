import requests
import json


def request_llama_cpp(url, data):
    # 发送POST请求
    response = requests.post(url, json=data)
    if (response.status_code == 200):
        response = json.loads(response.content)
    else:
        raise ConnectionError(f'request failed with {response.status_code}')
    return response['content']


if __name__ == "__main__":
    url = "http://localhost:8080/completion"
    # 创建一个json对象
    data = {
        "prompt": "用中文回答：中国最高的山是？",
        "n_predict": 128,
    }
    res = request_llama_cpp(url, data)
    print(res)
