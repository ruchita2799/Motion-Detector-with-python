#importing package open cv for live monitoring and inbuilt winsound for playing alarm
import cv2
import winsound
cam = cv2.VideoCapture(0) #variable cam assigned task to capture video
while cam.isOpened(): #loop will work until cam opened
    ret, frame1 = cam.read() 
    ret, frame2 = cam.read()
    #for finding motion, diffrence inbetween the stable object and the same object moving is needed
    diff = cv2.absdiff(frame1, frame2) #diffrence between two frames calculated i.e stable and moving
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY) #converting the colored motion detected in grey using RGB2GRAY
    blur = cv2.GaussianBlur(gray, (5, 5), 0) #the motion in gray to turn blur using Gaussian blur for more broad casting of video
    _,thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) #for ignoring noises and sharpning and accuracy of the motion
    dilated = cv2.dilate(thresh, None, iterations=3) #dilation for clear viewing and accuracy
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #for a broad rectangle for motion spotting i.e contouring
  
    for c in contours:
        if cv2.contourArea(c) < 5000:  #specifing a range below which no motion will be captured
            continue
        x, y, w, h = cv2.boundingRect(c)  #x,y axis , width and height will be specified
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2) #description for contour rectangle 
        winsound.PlaySound('alert.wav', winsound.SND_ASYNC) #audio will play when motion detected
    if cv2.waitKey(10) == ord('r'): #key r will break the loop and close cam
        break
    cv2.imshow('Hp Rc cam', frame1)
    exit