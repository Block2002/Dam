import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "12380656"
API_HASH = "d927c13beaaf5110f25c505b7c071273"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "8111667503:AAF5s5GNWdwqCVQT4Eb4cUSEEacGHvGUMls"
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","J_a_c_h_50")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME","Theo_X_Music_bot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME")
# ---------------------------------------------------------


# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://jazibot02:jazibot02@cluster0.s7fhq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002323512184"))

# Get this value from @PURVI_HELP_BOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7909700698))


## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("samdio5")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HRKU-a19e584b-5b15-4b76-b429-258cbfc20a8e")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Block2002/Dam",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Theo_X_Chennal")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Theo_X_Chennal")

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
STRING1 = "BQC86fAAHP0tiHCzoZeEX58Zz_lsQnC3BkvWSIy5ZwgFf-oZYqEJtX6vH5P5hLoEyiS7dWoaIXhuvXmZz2uGl_aC_j8HD7PDweuT9pOL3T_GH76ICsiJQIHdlDp1X7HGrpZE5Fm3VBmhksQ6Do9DWAp5Xfw36WdlRQwseCM0JQ5soTI6Gr5L1eXE_RkgtaDZdb75T_E1cFgAejPx0X5JGgG7Pe6RpAQNuzjex9VZenQgpWQjvfX4DJGNr4Pn1uTmforFT2hua4Fh79GOgRNa-qu5N01a-7hHnDichikjwaP-z_EA0_bAsOiBYLNl4Oh9gk_i_nynFFTcYxttiQUi171lXOGt7gAAAAHK2lK0AA"
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
    "START_IMG_URL", "https://graph.org/file/927acd55615f9446c121c-112b373f0660b195d7.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/70fafc35e1b4b8dae3c70-3ad009c366e7cf9869.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/927acd55615f9446c121c-112b373f0660b195d7.jpg"
STATS_IMG_URL = "https://graph.org/file/70fafc35e1b4b8dae3c70-3ad009c366e7cf9869.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/8e3552aa743ffdb6f18c9.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/8e3552aa743ffdb6f18c9.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


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
