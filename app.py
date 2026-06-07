
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SentimentRequest(BaseModel):
    sentences: list[str]

def classify(text: str):
    text = text.lower()

    positive = ["love", "great", "awesome", "excellent",
                "happy", "good", "amazing", "wonderful"]

    negative = ["sad", "terrible", "awful", "hate",
                "bad", "horrible", "worst"]

    if any(word in text for word in positive):
        return "happy"

    if any(word in text for word in negative):
        return "sad"

    return "neutral"

@app.post("/sentiment")
async def sentiment(data: SentimentRequest):
    return {
        "results": [
            {
                "sentence": sentence,
                "sentiment": classify(sentence)
            }
            for sentence in data.sentences
        ]
    }