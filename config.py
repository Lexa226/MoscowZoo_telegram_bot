from dotenv import load_dotenv
import os


load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
PATRONAGE_URL = "https://moscowzoo.ru/about/guardianship"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
