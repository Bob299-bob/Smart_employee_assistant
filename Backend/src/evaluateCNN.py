from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img,img_to_array
import numpy as np

model=load_model('../models/model.h5')


def predict(file):
    img=load_img(file,target_size=(200,200))
    img_arr=img_to_array(img)
    f_img=np.expand_dims(img_arr,axis=0)
    img=f_img/255.0
    Y_pred=model.predict(img)
    confidence=Y_pred[0][0]*100
    if confidence >= 80:
        print("No Mask")
    elif confidence <=20:
        print("Mask")
    else:
        print("Please Enter  valid image")
    return confidence,img

