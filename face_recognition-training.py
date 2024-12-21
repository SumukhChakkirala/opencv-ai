import os
import cv2
import face_recognition as FR
import pickle

knownEncodings = []
names = []
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
imagedir = '/home/sumukhchakkirala/Documents/opencv-ai/demoImages/known'

# face = FR.load_image_file()
# faceloc = FR.face_locations(face)
# faceEncoding = FR.face_encodings(face)

for root,dirs,files in os.walk(imagedir):
    #print(root)
    #print(dirs)
    #print(files)
    for file in files:
        #fullpath = os.path.join(root,file)
        fullpath = os.path.join(root,file)
        print(fullpath)

        #face recognition 

        face = FR.load_image_file(fullpath)
        faceloc = FR.face_locations(face)[0]
        faceEncoding = FR.face_encodings(face)[0]

        name = os.path.splitext(file)[0]
        names.append(name)
        knownEncodings.append(faceEncoding)

print(names)
print(knownEncodings)
with open('/home/sumukhchakkirala/Documents/opencv-ai/train.pk1','wb') as f:
    pickle.dump(names,f)
    pickle.dump(knownEncodings,f)


# unknownFace = FR.load_image_file('/home/sumukhchakkirala/Documents/opencv-ai/demoImages/unknown/u1.jpg')
# unknownFaceBGR = cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)

# faceLocations = FR.face_locations(unknownFace)
# unknownEncodings = FR.face_encodings(unknownFace,faceLocations)



# for faceLocation, unknownEncoding in zip(faceLocations,unknownEncodings):
#     top,right,bottom,left = faceLocation
#     print(faceLocation)
#     cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(255,0,0),3)
#     name = 'unknown Person'
#     matches = FR.compare_faces(knownEncodings,unknownEncoding)
#     print(matches)
#     if True in matches:
#         matchIndex = matches.index(True)
#         print(matchIndex)
#         print(names[matchIndex])
#         name = names[matchIndex]
#     cv2.putText(unknownFaceBGR,name,(left,top),font,0.5,(255,0,0),2)
# cv2.imshow('frame',unknownFaceBGR)
# cv2.waitKey(10000)

# print(names)