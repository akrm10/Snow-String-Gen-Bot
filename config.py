from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("21209802"))
API_HASH = getenv("eed1c8387c6ee80009527e07d9d58cc0")

BOT_TOKEN = getenv("6807629743:AAHsnFL_eb9F-egK2yjvvxVgKWIcQIhpNDA")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

OWNER_ID = int(getenv("OWNER_ID", 6716174264))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Kdramaland_Official")
