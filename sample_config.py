import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = "5223204003:AAEGlin3QwEO5Mu_mbMqYF9s1nksixBHX0Q"

    # The Telegram API things
    # Get these values from my.telegram.org
    APP_ID = 3796974
    API_HASH = "9511d0112631f9990337eb724d1a7d0d"

    # Array to store users who are authorized to use the bot
    AUTH_USERS = 1464063686

    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    # Sql Database url
    DB_URI = "postgres://oiqzxhmozopjla:0c6c78f00a7cda54cbd9cd89673cea333438390f5834f65c49d5950a67e0b5b2@ec2-3-219-204-29.compute-1.amazonaws.com:5432/dffs7h7bclul7b"
    
