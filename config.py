# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "29777466"))
API_HASH = getenv("API_HASH", "a04b3df726520026f207079aec2f9879")
BOT_TOKEN = getenv("BOT_TOKEN", "8463395750:AAEZwDq7gVps8YZvfm0g6kLHftQIIKqv3qw")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8399557684").split()))
MONGO_DB = getenv("MONGO_DB", "BQHGXjoABmMxqKLfb7AU86vPtLbNIBGttHEjSDCoV87Ph_UM_WRZ9ZdIxVcN0i4-6CckEo3qSXw7WRa_Zgj-OZjTVWtRtwFEpAmsvbhUHnQzv7u32dpENOs5DTR0mREjfdlPkcgbrQgLv6-BGcTiDgdmTriyYoigC-_gFcNaqYFkBcrtToBAjaf0XJDXgrxGXoeLAYk3PvgiGYw8HTH117tQ0jPpA7P63HTDNbopuL-CjyXlr-nURojIjAJiSGZofqqdRSlIpxg5knjTFE2ejorLsHitaBO7veaijkGg06yN-Yu7mrwX98ZyBfBq62rKK-wXQ5tR20ISEYcc8Qn07RuXGx6oowAAAAA1FSa2AA")
LOG_GROUP = getenv("LOG_GROUP", "-1003164986113")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003164986113"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
