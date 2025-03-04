# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import re
import os
from os import environ
from Script import script  # Ensure this is a valid import

# Regex for ID Validation
id_pattern = re.compile(r'^.\d+$')

# Function to Check Boolean Environment Variables
def is_enabled(value, default=False):
    return str(value).lower() in ["true", "yes", "1", "enable", "y"]

# Bot Information
API_ID = int(environ.get("API_ID", "25195586"))
API_HASH = environ.get("API_HASH", "32d15d1f3d4f8c1fe7bb21bed28ffb37")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Bot Start Picture
PICS = environ.get('PICS', 'https://graph.org/file/ce1723991756e48c35aa1.jpg').split()

# Admins List Parsing
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1161930116').split()]

# Bot Username
BOT_USERNAME = environ.get("BOT_USERNAME", "Toffeedistributerbot")  # Without @

# Server Port (Ensure Integer)
PORT = int(environ.get("PORT", 8080))

# Clone Mode
CLONE_MODE = is_enabled(environ.get('CLONE_MODE', "False"))

# If Clone Mode is Enabled, Ensure Required Variables are Set
CLONE_DB_URI = environ.get("CLONE_DB_URI", "") if CLONE_MODE else ""
CDB_NAME = environ.get("CDB_NAME", "") if CLONE_MODE else ""

# Database Information (Ensure Proper Credentials)
DB_URI = environ.get("DB_URI", "mongodb+srv://<db_username>:<password>@cluster0.fbqjc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "toffee_distributer")

# Auto Delete Information
AUTO_DELETE_MODE = is_enabled(environ.get('AUTO_DELETE_MODE', "False"))
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30")) if AUTO_DELETE_MODE else 0  # Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800")) if AUTO_DELETE_MODE else 0  # Seconds

# Logging Channel (Ensure Integer)
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "1002309172456"))

# File Caption Handling (Ensure script.CAPTION Exists)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", getattr(script, "CAPTION", "Default Caption"))
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Public File Store Mode
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"))

# Verification Mode
VERIFY_MODE = is_enabled(environ.get('VERIFY_MODE', "True"))
SHORTLINK_URL = environ.get("SHORTLINK_URL", "https://modijiurl.com/") if VERIFY_MODE else ""
SHORTLINK_API = environ.get("SHORTLINK_API", "e905235ae9ef0a396c01e5818e7d6ccdd84d7b04") if VERIFY_MODE else ""
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/toffeedistributer") if VERIFY_MODE else ""

# Website Information
WEBSITE_URL_MODE = is_enabled(environ.get('WEBSITE_URL_MODE', "True"))
WEBSITE_URL = environ.get("WEBSITE_URL", "https://www.blogger.com/u/2/blog/post/edit/2678387556182342654/5084359522687669244") if WEBSITE_URL_MODE else ""

# File Stream Configuration
STREAM_MODE = is_enabled(environ.get('STREAM_MODE', "False"))
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes

# Detect Heroku Environment
ON_HEROKU = 'DYNO' in environ
URL = environ.get("URL", "")

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
