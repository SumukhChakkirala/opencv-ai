import cv2
import mediapipe as mp
print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(2)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

pose = mp.solutions.pose.Pose(static_image_mode=False, model_complexity=1, 
                               enable_segmentation=True, smooth_landmarks=True, 
                               min_detection_confidence=0.5, min_tracking_confidence=0.5)

mpdraw = mp.solutions.drawing_utils


while True:
    ignore,  frame = cam.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = pose.process(frameRGB)
    landmarks=[]
    if results.pose_landmarks!= None:
        mpdraw.draw_landmarks(frame,results.pose_landmarks,mp.solutions.pose.POSE_CONNECTIONS)
        for lm in results.pose_landmarks.landmark:
            #print((lm.x,lm.y))
            landmarks.append((int(lm.x*width),int(lm.y*height)))
        
        print(landmarks)
        cv2.circle(frame,landmarks[0],4,(255,255,0),-1)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()