import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()
 
# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID","22858011"))
API_HASH = getenv("API_HASH","f780b6a5873656b62d2c5a9f8be50bdc")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","5966375685:AAE4ivL6HbVQII4ml5AleUCAStiSwHk9wuA")
BOT_NAME = getenv("BOT_NAME","Music Terex")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://proceed58:proceed58@cluster0.p5s9ym5.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 480))

# Chat id of a group for logging bot s activities
LOGGER_ID = int(getenv("LOGGER_ID","-1001921300683"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID","5868423807"))

## Fill these variables if you re deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/terexip/music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

CHANNEL_NAME = getenv("CHANNEL_NAME", "Music Terex")
CHANNEL_LINK = getenv("CHANNEL_LINK", "https://t.me/Source_terex")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Ii_ebots")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist s track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION","BAFcyRsAFNaXXvLw-Jd-ZABDmF8xQ63ETW-Z8edS75g-PaVwZXszBTf2VR_rSNc0op2r9Z-3obWChoxhxbaeEwGd4ZjIZEY6_koJTKDKppQIekNXZd2VawhpwHv7g21zyAJG93AnsIVCslKbypggGGi67gZDmju-Lckmyx18YUC3nLqzQrcAfEmixRYYJk_66007JurgrzO-6llVBlczBRJFRJ3dYJ_YNtysKOaAJLhr6rMOjivGUjGA1qvRzMlccGj_lYWJAZ71pQDZtO-Ad2EjcgEePLwpf63X5189gU69q8WpcPC-VlXxofgMRdchk1pOCUUOb-544t8N3knU1wqlDvbhywAAAAFy5KzmAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL")
PING_IMG_URL = "https://telegra.ph/file/e29510f6e263bb5264cfb.jpg"
PLAYLIST_IMG_URL = "https://telegra.ph/file/e29510f6e263bb5264cfb.jpg"
STATS_IMG_URL = "https://telegra.ph/file/e29510f6e263bb5264cfb.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/e29510f6e263bb5264cfb.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/e29510f6e263bb5264cfb.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/e29510f6e263bb5264cfb.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/e29510f6e263bb5264cfb.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/e29510f6e263bb5264cfb.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/e29510f6e263bb5264cfb.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/e29510f6e263bb5264cfb.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/e29510f6e263bb5264cfb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if CHANNEL_LINK:
    if not re.match("(?:http|https)://", CHANNEL_LINK):
        raise SystemExit(
            "[ERROR] - Your CHANNEL_LINK url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
