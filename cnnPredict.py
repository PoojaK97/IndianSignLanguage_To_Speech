# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 23:17:33 2018
@author: abhi
"""

import cnnModel
import numpy as np
from keras import backend
import operator
import json
from gtts import gTTS
import os

language = 'en'
backend.common.set_image_dim_ordering('th')
#change output array according to data

get_output= None

def predictSign(frame,model):

    global output
    image = np.array(frame).flatten()
    image = image.reshape(cnnModel.img_channels, cnnModel.img_x,cnnModel.img_y)
    image = image.astype('float32')
    image = image / 255
    image = image.reshape(1, cnnModel.img_channels, cnnModel.img_x,cnnModel.img_y)
    prob_array = model.predict_proba(image)
    #print (prob_array)
    prob_map = {}
    index = 0
    for items in output:
        prob_map[items] = prob_array[0][index] * 100
        index += 1
        #print(str(index)+str(items)+str(prob_map[items]))
    guess = max(prob_map.items(), key=operator.itemgetter(1))[0]
    prob  = prob_map[guess]

    if prob > 75.0:
        with open('output.txt', 'w') as outfile:
            json.dump(prob_map, outfile)
        print(str(guess) + " " + str(prob))
        myobj = gTTS(text=guess, lang=language, slow=False)
        myobj.save("out.mp3") 
        os.system("start out.mp3") 
        return str(guess)
    else:
        return "No Output"


