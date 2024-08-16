from time import sleep

from constants import BOT_ID, COZE_API, COZE_URL, USER_ID
from utils import chat, get_chat_info, get_chat_msg


def chat_with_coze(query, api, bot_id, user_id, url, repeat=5, sleep_time=5):

    for i in range(repeat):
        content = chat(query, api, bot_id, user_id, url)
        if content['status_code'] == 200:
            break
        sleep(sleep_time)
    else:
        return content
    chat_id = content['data']['id']
    conversation_id = content['data']['conversation_id']

    for i in range(repeat):
        content = get_chat_info(chat_id, conversation_id, api, url)
        if content['status_code'] == 200:
            if content['data']['status'] == 'completed':
                break
        sleep(sleep_time)
    else:
        return content
    
    for i in range(repeat):
        content = get_chat_msg(chat_id, conversation_id, api, url)
        if content['status_code'] == 200:
            break
        sleep(sleep_time)
    return content


if __name__ == '__main__':
    # write your program here
    pass
