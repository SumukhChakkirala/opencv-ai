import os
import cv2
import face_recognition as FR
print(cv2.__version__)

imageDir = '/home/sumukhchakkirala/Documents/opencv-ai/demoImages/known'

for root,dirs,files in os.walk(imageDir):  #present directory, directories in the present, files in the present
    print('my working folder :',root)
    print("dirs in root: ", dirs)
    print("files in root: ", files)
    print('')
    for file in files:
        #fullfilepath = root+'/'+file
        fullfilepath = os.path.join(root,file)
        #print('your guy is ',fullfilepath)
        name = os.path.splitext(file)[0]  #Split the extension from a pathname. Returns: ('example', '.txt')
        print(name)
        myPicture = FR.load_image_file(fullfilepath)
        myPicture = cv2.cvtColor(myPicture,cv2.COLOR_RGB2BGR)
        cv2.imshow('frame', myPicture)
        cv2.waitKey(2500)
        cv2.destroyAllWindows()
