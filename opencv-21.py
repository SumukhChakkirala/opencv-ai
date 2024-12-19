import cv2
print(cv2.__version__)
import time


width = 640
height = 360

cam = cv2.VideoCapture(2)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade = cv2.CascadeClassifier('/home/sumukhchakkirala/Documents/opencv-ai/haar/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('/home/sumukhchakkirala/Documents/opencv-ai/haar/haarcascade_eye.xml') 
smileCascade = cv2.CascadeClassifier('/home/sumukhchakkirala/Documents/opencv-ai/haar/haarcascade_smile.xml')
tstart = time.time()
fps =0

while True:
    ignore, frame = cam.read()
    frameGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray,1.3,5)
    eyes = eyeCascade.detectMultiScale(frameGray,1.3,5)
    smiles = smileCascade.detectMultiScale(frameGray,1.3,5)
    print(smiles)
    print(" ")
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),3)
    for eye in eyes:
        x,y,w,h = eye
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
    for smile in smiles:
        x,y,w,h = smile
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)

    cv2.imshow("window", frame)

    # Wait for 'q' to be pressed to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    tend = time.time()
    looptime = tend -tstart
    if looptime>0:
        current_fps = 1/looptime
        fps = 0.9* fps+ 0.1 *current_fps
    tstart = tend 

    #print(fps)
cam.release()
cv2.destroyAllWindows()
