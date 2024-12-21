import cv2
import mediapipe as mp

width=1280
height=720
cam=cv2.VideoCapture(2)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mpdraw = mp.solutions.drawing_utils

def parseLandmarks(frame):
    myHands = []
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    if results.multi_hand_landmarks != None:
        for handlandmarks in results.multi_hand_landmarks:
            myHand =[]
            mpdraw.draw_landmarks(frame,handlandmarks,mp.solutions.hands.HAND_CONNECTIONS)
            for landmark in handlandmarks.landmark:
                myHand.append(((int(landmark.x*width),int(landmark.y*height))))
            
             # cv2.circle(frame,(300.0,300.0),25,(255,0,0),-1) wrong because location must be an integer 
            myHands.append(myHand)
    return myHands




while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame, (width,height))
    myhands = parseLandmarks(frame)
    for hand in myhands:
        cv2.circle(frame,hand[2],25,(255,0,0),-1)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
