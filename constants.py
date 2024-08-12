COZE_API = ''
BOT_ID = '7401061027922051090'

COZE_URL = 'https://api.coze.com/v3/chat'

"""
curl --location --request POST 'https://api.coze.com/v3/chat?conversation_id=7374752000116113452' \
--header 'Authorization: Bearer pat_OYDacMzM3WyOWV3Dtj2bHRMymzxP****' \
--header 'Content-Type: application/json' \
--data-raw '{
    "bot_id": "734829333445931****",
    "user_id": "123456789",
    "stream": false,
    "auto_save_history":true,
    "additional_messages":[
        {
            "role":"user",
            "content":"What a nice day",
            "content_type":"text"
        }
    ]
}'
"""