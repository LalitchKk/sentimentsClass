import joblib
import numpy as np
from keras.preprocessing.sequence import pad_sequences

# model = keras.models.load_model(open(r'model_lstm.h5', 'rb'))
# model = keras.models.load_model(r'D:\1-2566\AICLASS\Project\sentimetsClass\model_lstm_v2.h5')

# tokenizer = joblib.load(open(r'D:\1-2566\AICLASS\Project\sentimetsClass\tokennizer.pkl','rb'))



def predictClass(model,tokenizer,text):
    vector = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=300)
    class_predictions = model.predict(vector)
    # predicted_class = np.argmax(class_predictions)
    predicted_class = np.argmax(class_predictions) 
    print(predicted_class)
    print(class_predictions)
    print(text)

    if predicted_class == 2:
        str="Negative"
    elif predicted_class == 1:
        str="Neutral"
    elif predicted_class == 0:
        str="Positive"
    elif predicted_class == 3:
        str="Irregular"
    return {"result":str}

