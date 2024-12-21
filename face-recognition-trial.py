import cv2
import face_recognition as FR

font = cv2.FONT_HERSHEY_COMPLEX

donFace = FR.load_image_file('/home/sumukhchakkirala/Documents/opencv-ai/demoImages/known/Donald Trump.jpg')

faceloc = FR.face_locations(donFace)[0]
donFaceEncode = FR.face_encodings(donFace)[0]

donFace = FR.load_image_file('/home/sumukhchakkirala/Documents/opencv-ai/demoImages/known/Donald Trump.jpg')

faceloc = FR.face_locations(donFace)[0]
donFaceEncode = FR.face_encodings(donFace)[0]   

nancyFace = FR.load_image_file('/home/sumukhchakkirala/Documents/opencv-ai/demoImages/known/Nancy Pelosi.jpg')

faceloc = FR.face_locations(nancyFace)[0]
nancyFaceEncode = FR.face_encodings(nancyFace)[0]

knownEncodings = [donFaceEncode,nancyFaceEncode]

names = ['Donald TRUMP','Nancy Pelosi']
unknownFace = FR.load_image_file('/home/sumukhchakkirala/Documents/opencv-ai/demoImages/unknown/u3.jpg')
unknownFaceBGR = cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)

faceLocations = FR.face_locations(unknownFace)
unknownEncodings = FR.face_encodings(unknownFace,faceLocations)

for faceLocation, unknownEncoding in zip(faceLocations,unknownEncodings):
    top,right,bottom,left = faceLocation
    print(faceLocation)
    cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(255,0,0),3)
    name = 'unknown Person'
    matches = FR.compare_faces(knownEncodings,unknownEncoding)
    print(matches)
    if True in matches:
        matchIndex = matches.index(True)
        print(matchIndex)
        print(names[matchIndex])
        name = names[matchIndex]
    cv2.putText(unknownFaceBGR,name,(left,top),font,0.5,(255,0,0),2)

print('encoding is ',knownEncodings)
cv2.imshow('frame',unknownFaceBGR)

cv2.waitKey(5000)  #(top right bottom left)