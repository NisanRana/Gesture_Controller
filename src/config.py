import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ROBOFLOW_API_KEY")

MODEL_NAME = "my-first-project-ma20w"
MODEL_VERSION = 1

CONFIDENCE = 0.5
COOLDOWN = 1.0