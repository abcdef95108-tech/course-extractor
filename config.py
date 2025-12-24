import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '')
    API_ID = int(os.environ.get("API_ID", '33516244'))
    API_HASH = os.environ.get("API_HASH", 'c1abd0630fcd54d33bc6528ec0955fff')
    AUTH_USER = os.environ.get('AUTH_USERS', '6220046859').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "Obito™"#Here You Can Change with Your Name  or any custom name or title you prefer

