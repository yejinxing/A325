import base64
import json

import requests

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def send_image_description_request(api_key, image_path):
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "qwen-vl-8k",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "描述一下这张图片"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://ai-gateway.vei.volces.com/v1/chat/completions", headers=headers, json=payload)

    return response.json()

# Example usage:
if __name__ == "__main__":
    api_key = "sk-081cb15c9d884e59a456b7b07a4f9901qipi2rstq3nls9to"
    image_path = "C:\\Users\\33304\\Desktop\\qwen-vl-8k\\qwen-vl-8k\\c08e556507b819915cd20860ce5777ee.jpg"
    response = send_image_description_request(api_key, image_path)

    if "choices" in response and len(response["choices"]) > 0:
        msg = response["choices"][0]
        msg_str = json.dumps(msg, indent=2, ensure_ascii=False)  # ensure_ascii=False to preserve non-ASCII characters
        a=msg_str.encode('utf-8').decode()
        print(a)
