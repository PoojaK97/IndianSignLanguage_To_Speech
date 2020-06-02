import cv2
import cnnFilters
import cnnModel
from PIL import Image
import time
import numpy as np
from keras import backend
import operator
import json
from gtts import gTTS
import os

x0 = 400
y0 = 200
height = 200
width = 200

frame = Image.open('./AdaptiveThresholdModeDataSet/You36.png')
model=cnnModel.createCNNModel(0)
#roi = cnnFilters.adaptiveThresholdMode(frame, x0, y0, width, height)

language = 'en'
backend.common.set_image_dim_ordering('th')
#change output array according to data

output = ["House","Aboard","Baby","Bowl", "Friend","IorMe","Money","Opposite","Prisoner","You"]

get_output= None

def predictSign(frame,model):

    global output
    global prev
    global cur
    image = np.array(frame).flatten()
    image = image.reshape(cnnModel.img_channels, cnnModel.img_x,cnnModel.img_y)
    image = image.astype('float32')
    image = image / 255
    image = image.reshape(1, cnnModel.img_channels, cnnModel.img_x,cnnModel.img_y)
    prob_array = model.predict_proba(image)
    # print (prob_array)
    prob_map = {}
    index = 0
    for items in output:
        prob_map[items] = prob_array[0][index] * 100
        index += 1
        #print(str(index)+str(items)+str(prob_map[items]))
    guess = max(prob_map.items(), key=operator.itemgetter(1))[0]
    prob  = prob_map[guess]


    with open('output.txt', 'w') as outfile:
        json.dump(prob_map, outfile)
    print(str(guess) + " " + str(prob))
    return str(guess)


predictSign(frame,model)
