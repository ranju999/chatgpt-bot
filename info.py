# ©️biisal jai shree krishna 😎
from os import environ
from dotenv import load_dotenv

load_dotenv()

API_ID = environ.get("API_ID" , "12380656")
API_HASH = environ.get("API_HASH" , "d927c13beaaf5110f25c505b7c071273")
BOT_TOKEN = environ.get("BOT_TOKEN" , "7328112987:AAE-m8fhi09-5GtdiSI0Lii8Qvpkg7Snnfs")
ADMIN = int(environ.get("ADMIN" , "5977931010"))
CHAT_GROUP = int(environ.get("CHAT_GROUP", "-1002028053413"))
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1002114619001")
MONGO_URL = environ.get("MONGO_URL" , "mongodb+srv://ranjuvishwakarma50:aman@cluster0.uvah8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
AUTH_CHANNEL = int(
    environ.get("AUTH_CHANNEL", "-1002114619001")
)
FSUB = environ.get("FSUB", True)
STICKERS_IDS = (
    "CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME"
).split()
COOL_TIMER = 20  # keep this atleast 20
ONLY_SCAN_IN_GRP = environ.get(
    "ONLY_SCAN_IN_GRP", True
)  # If IMG_SCAN_IN_GRP is set to True, image scanning is restricted to your support group only. If it's False, the image scanning feature can be used anywhere.
REACTIONS = ["❤️‍🔥", "⚡", "🔥"]
