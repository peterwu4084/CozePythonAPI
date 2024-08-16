import json

import requests

from constants import COZE_URL


def make_headers(api):
    headers = {
        'Authorization': f'Bearer {api}',
        'Content-Type': 'application/json',
    }
    return headers


def make_data(query, bot_id, user_id):
    data = {
        "bot_id": bot_id,
        "user_id": user_id,
        "stream": False,
        "auto_save_history": True,
        "additional_messages":[
            {
                "role": "user",
                "content": query,
                "content_type": "text"
            }
        ]
    }
    return data


def chat(query, api, bot_id, user_id, url=COZE_URL):
    headers = make_headers(api)
    data = make_data(query, bot_id, user_id)
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        content= dict(reason=response.reason, status_code=response.status_code)
    else:
        content = json.loads(response.content)
        content['status_code'] = response.status_code
    return content


def get_chat_info(chat_id, conversation_id, api, url=COZE_URL):
    headers = make_headers(api)
    response = requests.get(f'{url}/retrieve?chat_id={chat_id}&conversation_id={conversation_id}', headers=headers)
    if response.status_code != 200:
        content= dict(reason=response.reason, status_code=response.status_code)
    else:
        content = json.loads(response.content)
        content['status_code'] = response.status_code
    return content


def get_chat_msg(chat_id, conversation_id, api, url=COZE_URL):
    headers = make_headers(api)
    response = requests.post(f'{url}/message/list?chat_id={chat_id}&conversation_id={conversation_id}', headers=headers)
    if response.status_code != 200:
        content= dict(reason=response.reason, status_code=response.status_code)
    else:
        content = json.loads(response.content)
        content['status_code'] = response.status_code
    return content