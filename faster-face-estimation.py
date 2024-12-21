# mediapipe detects faces the quickest without drop in fps(we could use haarCascade/face_recognition as well)


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

findfaces = mp.solutions.face_detection.FaceDetection()
drawFace = mp.solutions.drawing_utils

while True:
    ignore,  frame = cam.read()
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = findfaces.process(frameRGB)
    print(results.detections[0].location_data.relative_bounding_box)
    if results.detections != None:
        for face in results.detections:     # picking one face if there are many
            #drawFace.draw_detection(frame,face)   inbuilt mediapipe draw
            box = face.location_data.relative_bounding_box
            topLeft = (int(box.xmin*width),int(box.ymin*height))
            bottomRight = (int((box.xmin+box.width)*width),int((box.ymin+box.height)*height))
            cv2.rectangle(frame,topLeft,bottomRight,(255,255,0),2)   # we can customize the draw using opencv

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()