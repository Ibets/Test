import requests
import json
import cv2
import time
import threading
import numpy as np

def facedetect(gray, t):
    gray = cv2.resize(gray, (1280 // 4, 720 // 4))
    _, img_encoded = cv2.imencode('.jpg', gray)
    
    # send http request with image and receive response
    try:
	    response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
	    
	    # decode response
	    global faces
	    faces = json.loads(response.text)

	    print("latency:", time.time() - t)
    except:
	    print("no data")



addr = 'http://10.16.10.11'
test_url = addr + '/facedetect'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

while True:
    cap = cv2.VideoCapture('test2.mp4')
    cap.set(cv2.CAP_PROP_FPS, 1);
    fps = cap.get(cv2.CAP_PROP_FPS)

    
    #latency = dict()
    global faces
    faces = None

    while True:
        
        #st = time.time()1
        _, img = cap.read()
        #print(img.shape)
        
        # encode image as jpeg
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        threading.Thread(target=facedetect, args=(gray, time.time())).start()
        
        if faces != None:
            for key, face in faces.items():
                x = int(face['x']) * 4
                y = int(face['y']) * 4
                w = int(face['w']) * 4
                h = int(face['h']) * 4
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
        #fi = time.time()
        #print("f i: ", i, "=>", fi)
        
        #latency[i] = fi - st
        
        cv2.imshow('img', img)
        
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
        
    cap.release()
    cv2.destroyAllWindows()
