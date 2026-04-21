import os
from dotenv import load_dotenv
from inference_sdk import InferenceHTTPClient

load_dotenv()

API_KEY = os.getenv("ROBOFLOW_API_KEY")

CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key=API_KEY
)

MODEL_ID = "my-first-project-ma20w/1"

def predict(frame):
    result = CLIENT.infer(frame, model_id=MODEL_ID)

    preds = result.get("predictions", [])

    if len(preds) > 0:
        top = preds[0]
        return top["class"], top["confidence"]

    return None, 0