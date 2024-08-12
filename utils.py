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


def post(query, api, bot_id, user_id, url=COZE_URL):
    import pdb; pdb.set_trace()
    headers = make_headers(api)
    data = make_data(query, bot_id, user_id)
    response = requests.post(url, headers=headers, json=data)
    import pdb; pdb.set_trace()
    print()
    # for line in response.iter_lines():
    #     if line:
    #         decoded_line = line.decode('utf-8')
    #         json_data = json.loads(decoded_line.split("data:")[-1])

    #         if json_data['event'] == 'done':
    #             break
    #         else:
    #             if json_data['message']['type'] == 'answer':
    #                 yield json_data['message']['content']