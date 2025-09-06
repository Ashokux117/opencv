

import cv2
 
# Open the default webcam (0)
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read() 
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


 
    # Display the frame using imshow
    cv2.imshow("Captured Frame", frame)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()  # Close the window

cap.release()
    
    
    

