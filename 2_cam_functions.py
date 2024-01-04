import cv2
import numpy as np

#capturing a webcam/mp4 file
cap = cv2.VideoCapture(0)

#keeps the webcam displaying 
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    #splitting the display into 4 quadrants rotated
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180_COUNTERCLOCKWISE)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Jaejo is Great!', (200, height - 10), font, 1, (0, 0, 0), 2, cv2.LINE_AA)


    #displaying the frame
    cv2.imshow('frame', image)

    #if the key 
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()