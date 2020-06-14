import cv2
import cnnFilters
import time
from gtts import gTTS
import os

x0 = 400
y0 = 200
height = 200
width = 200

def Main():
    global x0, y0
    isQuit=0
    tts = gTTS(text="Change the gesture", lang='en')
    tts.save("dataset.mp3")
    cap = cv2.VideoCapture(0)
    ret = cap.set(3,640) #change width of frame
    ret = cap.set(4,480) #change height of frame
    i=0
    j=0
    #sign array should be in order 
    signnamearray = ["Aboard", "All_Gone", "Baby", "Beside", "Book", "Bowl", "Bridge", "Camp", "Cartridge", 
    "Eight", "Five", "Fond", "Four", "Friend", "Glove", "Hang", "High", "House", "How_Many","IorMe", "Man", "Marry",
    "Meat", "Medal", "Mid-day", "Middle", "Money", "Moon", "Mother", "Nine", "One","Opposite","Prisoner", "Ring", "Rose", "See",
    "Seven", "Short", "Six", "Superior", "Ten", "Thick", "Thin", "Three", "Tobacco", "Two", "Up", "Watch", "Write", "You"]
    while(True):
        ret, frame = cap.read()
        #invert frame
        frame = cv2.flip(frame, 3) 

        roi1 = cnnFilters.adaptiveThresholdMode(frame, x0, y0, width, height)
        roi2 = cnnFilters.siftMode(frame, x0, y0, width, height)
        roi3 = cnnFilters.noFilterMode(frame, x0, y0, width, height)
        cv2.imshow('Sign Language Dataset Capture',frame)

        if not isQuit:
            cv2.imshow('ROI1', roi1)
            cv2.imshow('ROI2', roi2)
            cv2.imshow('ROI3', roi3)

        key = cv2.waitKey(10) & 0xff

        if key == ord('n'):
            '''
            signname = input("Enter a sign name \n")
            '''
            signname = signnamearray[i]
            path1="./AdaptiveThresholdModeDataSet/"
            path2="./SiftModeDataSet/"
            path3="./NoFilterModeDataSet/"
            '''
            timestamp is not used in the final dataset naming
            ts = int(time.time())
            name = signname + str(ts)
            print ("creating image...")
            cv2.imwrite(path1+name + str(j) + "1.png", roi1)
            cv2.imwrite(path2+name + str(j) + "2.png", roi2)
            cv2.imwrite(path3+name + str(j) + "3.png", roi3)
            '''
            print ("creating image...")
            cv2.imwrite(path1+str(signname) + str(j) + ".png", roi1)
            cv2.imwrite(path2+str(signname) + str(j) + ".png", roi2)
            cv2.imwrite(path3+str(signname) + str(j) + ".png", roi3)
            print ("created image: "+str(signname)+ " " + str(j) + " for word " + str(signname))
            j=j+1
            #number of images per sign, 100 for our dataset
            if(j==100):
                i=i+1
                j=0
                #Total number of signs
                if(i==50):
                    break
                os.system("start dataset.mp3")
            time.sleep(0.04 )
        elif key == ord('q'):
            isQuit = not isQuit
        elif key == ord('w'):
            y0 = y0 - 5
        elif key == ord('s'):
            y0 = y0 + 5
        elif key == ord('a'):
            x0 = x0 - 5
        elif key == ord('d'):
            x0 = x0 + 5
        elif key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    Main()