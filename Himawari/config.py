"""
MIT License

Copyright (c) 2022 Arsh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Create a new config.py or rename this to config.py file in same dir and
# import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open(f"{os.getcwd()}/Himawari/{config}", "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    # dont change
    LOGGER = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    LOAD = "ChatBot"
    NO_LOAD = ""  # put some module name here if you do not want it to load
    MONGO_DB = "wolfwood"
    BOT_API_URL = "https://api.telegram.org/bot"

    # you can change these
    DEL_CMDS = False  # set it to true if you want the "/" commands to be deleted
    INFOPIC = True  # picture while doing /info
    STRICT_GBAN = True  # IF YOU WANT TO ENABLE GBAN SYSTEM
    API_ID = 19099900  # api id from my.telegram.org
    API_HASH = "2b445de78e5baf012a0793e60bd4fbf5"  # api hash from my.telegram.org
    # mongo database link (necessary)
    MONGO_DB_URL = "mongodb+srv://sonu55:sonu55@cluster0.vqztrvk.mongodb.net/?retryWrites=true&w=majority"
    DB_URL = "postgresql://kunalgaikwad932244:tIQq5nmiW7KY@ep-little-wood-723080.ap-southeast-1.aws.neon.tech/neondb"  # postgres sql database link
    # redis database url from redislabs.com
    REDIS_URL = "redis://default:neko69@redis-18084.c289.us-west-1-2.ec2.cloud.redislabs.com:18084/Neko-Free-db"
    TOKEN = "5827224610:AAGftR84QtQ6rMr7_r2a7zPPjg1SrG755yA"  # bot token from @BotFather
    DEV_USERS = [6198858059]  # developers id
    SUDO_USERS = [9656]  # sudo users id
    SUPPORT_USERS = [1909]  # support user ids
    WHITELIST_USERS = [2112, 1212]  # commas for multiple ids
    EVENT_LOGS = -1001596651023  # channel id for gban logs
    OWNER_ID = 6198858059  # owner id in integer
    ERROR_LOGS = -1001596651023  # support group id
    BOT_NAME = "wolfwood"  # your bot name
    ARQ_API_KEY = "SLSFXSsdUXNSMH-ARQ"  # ARQ api key from @ARQRobot
    ARQ_API_URL = "arq.hamker.dev"  # arq link
    SUPPORT_CHAT = "MissCamelliaSupport"  # support group username without @
    UPDATES_CHANNEL = "MissCamelliaUpdate"  # Updates/News Channel username without @
    BOT_USERNAME = "Wolfwood_xBot"  # bot username without @
    REM_BG_API_KEY = "K2dsdsYma6cZx"  # not necessary
    # spamwatch api token from @SpamWatchBot
    SPAMWATCH_API = "J968E_20LgxrKjsdN24cqYtD~gNRTbU"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
