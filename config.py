import os
from dotenv import load_dotenv

load_dotenv()

COMPOSIO_API_KEY = os.getenv('COMPOSIO_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')