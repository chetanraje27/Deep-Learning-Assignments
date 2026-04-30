from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from fastapi.middleware.cors import CORSMiddleware

# Load model and files
model = load_model("model.h5")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("max_len.pkl", "rb") as f:
    max_len = pickle.load(f)

app = FastAPI()

# ✅ CORS (IMPORTANT for UI connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request format
class InputText(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "LSTM Next Word Prediction API Running"}

# Prediction function
def predict_next_word(text):
    token_list = tokenizer.texts_to_sequences([text])[0]
    if len(token_list) == 0:
        return "Input words not in vocabulary"

    token_list = pad_sequences([token_list], maxlen=max_len-1, padding='pre')

    predicted = model.predict(token_list, verbose=0)
    predicted_index = np.argmax(predicted)

    return tokenizer.index_word.get(predicted_index, "Not Found")

# API endpoint
@app.post("/predict")
def predict(input: InputText):
    result = predict_next_word(input.text)
    return {
        "input": input.text,
        "next_word": result
    }