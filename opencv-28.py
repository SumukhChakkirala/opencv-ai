import cv2 #works in bgr rest of universe works in rgb
import mediapipe as mp

width=1280
height=720
cam=cv2.VideoCapture(2)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

#hands = mp.solutions.hands.Hands(False,2,.5,.5)  #(isitStaticImage?,maxHands,Trackingconfidence=.5,Trackingconfidence=.5,), analyse hands
#always initialize below way above statement gives typeError
hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) 

mpDraw = mp.solutions.drawing_utils     #annotate frame with the data


while True:
    myHands=[]
    ignore,  frame = cam.read()
    frame = cv2.resize(frame,(width,height))
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)  # result is a very complex data structure
    print(results)
    if results.multi_hand_landmarks != None:
        print("hand found")
        for handLandMarks in results.multi_hand_landmarks:
            myHand = []
            print(handLandMarks) #has x,y,z coordinates for all 21 points on the hand
            mpDraw.draw_landmarks(frame,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS)
            for Landmarks in handLandMarks.landmark:
                print((Landmarks.x,Landmarks.y))
                myHand.append((int(Landmarks.x*width),int(Landmarks.y*height)))
            print('')
            cv2.circle(frame,myHand[10],25,(255,0,0),-1)
            # cv2.circle(frame,(300.0,300.0),25,(255,0,0),-1) wrong because location must be an integer 
            myHands.append(myHand)
            print(myHands)
            print(' ')

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()