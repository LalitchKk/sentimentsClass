import joblib
import requests
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from tensorflow import keras

from app.code_2 import predictClass

#load model
# model = joblib.load(open(f'model_lstm_v2.h5','rb'))
# tokenizer = joblib.load(open(f'tokennizer','rb'))

#oad model local
model = keras.models.load_model(f'model/model_lstm_v2.h5')
# model = keras.models.load_model(r'D:\1-2566\AICLASS\Project\sentimetsClass\model\model_lstmh5.h5')
tokenizer = joblib.load(open(f'model/tokennizer.pkl','rb'))

# use docker
end_words = 'http://172.17.0.2:80/api/getStopWords'

# end_words = 'http://localhost:8080/api/getStopWords' #local

app = FastAPI()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "This is my api"}

@app.post("/api/sentimentClass")
async def read_str(request:Request):
    item = await request.json()
    stopWords = requests.get(end_words,json=item)
    response = predictClass(model,tokenizer,stopWords.json())
    print(stopWords.json())
    return {"res":response,
            "stop":stopWords.json()}

# text = "im getting borderlands 2 murder"
# response = predictClass(model,tokenizer,text)