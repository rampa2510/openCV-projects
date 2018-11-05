import cv2 # we import the necessary modules

cap = cv2.VideoCapture(0) # this will open the webcam

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # we initialise the face cascade
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') # we initialise the eye cascade
phone_cascade = cv2.CascadeClassifier('Phone_Cascade.xml') # we initialise the phone cascade
while True: # this loop will be used to create a video
    ret,img = cap.read() # this will retuen a boolean value and the frame
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # convert each frame to grayscale
    phone = phone_cascade.detectMultiScale(gray,10,5) # to detect phone
    faces = face_cascade.detectMultiScale(gray,1.2,6) # to detect face
    for (px,py,pw,ph) in phone: # for drwaing a rectangle on the phone
        cv2.rectangle(img,(px,py),(px+pw,py+ph),(0,0,255),2)
    for (x,y,w,h) in faces: # for face
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        roi_gray = gray[y:y+h,x:x+w] # we create the region of intrest our face
        roi_color = img[y:y+h,x:x+h] # this will be used to draw rectangle

        eyes = eye_cascade.detectMultiScale(roi_gray) # to detect eyes

        for (ex,ey,ew,eh) in eyes: #to draw rectangle on eyes
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()