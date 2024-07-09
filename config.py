import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("26977508"))
API_HASH = getenv("396589629e6705c592bc7fe891dc6e37")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7086208542:AAFwBRviwAd2lxUak_SUXaRmB52fiG4Ku8k")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://autorenameparadox:UhGvf4nc1A6FLHO7@cluster0.lhvx0w9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002083355293"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6193451722))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Zeno79/Anon-music-bot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Paradox_support_group")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/animes_Paradox_gang")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("BQGKGXYASfP5a_n33fKERgjn9VbdN0u8f3CJE4X0fgA0DGj5hQoyncmnEHk4O3E45JQgoK0DlowSxsIpamhRFckVpH9LlwTt6ET8u0QdshxDD3FVFOL3Ol71-ix5i5EqYd5pfP403u9I6PoVOPDeI-3ZFA4of1hLPRv60muLnssRd1jsp9CtV2wRF2sNKEdVfncn2AlB7TN5TkptOocTZqVIkwjtf9A_YCcPzGTbtHlTNjIEW0SKPOvYjgns5maIeMxghwlQGmAwB9v_0O2H7WtztiXKSnteHGVBGOlErvIdNJiYK2Yr83PXmK8A9lVFeV6ShmMAYCmT6UF5crmuYGq9pOX_-AAAAAGV_HpMAA")
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


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/afc1d9385391735fb663b.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/afc1d9385391735fb663b.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/afc1d9385391735fb663b.jpg"
STATS_IMG_URL = "https://graph.org/fileafc1d9385391735fb663b.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/fileafc1d9385391735fb663b.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/fileafc1d9385391735fb663b.jpg"
STREAM_IMG_URL = "https://graph.org/fileafc1d9385391735fb663b.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/fileafc1d9385391735fb663b.jpg"
YOUTUBE_IMG_URL = "https://graph.org/fileafc1d9385391735fb663b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/fileafc1d9385391735fb663b.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/fileafc1d9385391735fb663b.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/fileafc1d9385391735fb663b.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
