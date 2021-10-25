import cv2
import time
import numpy as np


frame = cv2.VideoWriter_fourcc(*'XVID')
img = cv2.VideoWriter('output.avi', frame, 20.0, (640, 480))

frame = cv2.resize(frame, (640, 480))
img = cv2. resize(img, (640, 480))

cap = cv2.VideoCapture(0)


time.sleep(2)
bg = 0


for i in range(60):
    ret, bg = cap.read()

bg = np.flip(bg, axis=1)


while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    
    img = np.flip(img, axis=1)

    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    

    l_black = np.array([30, 30, 0])
    u_black = np.array([104, 153, 70])
    mask_2 = cv2.inRange(frame, l_black, u_black)


    

    #mask_2 = cv2.bitwise_not(mask_1)

    
    res_1 = cv2.bitwise_and(img, img, mask=mask_2)

    
    #res_2 = cv2.bitwise_and(frame, frame, mask=mask_1)

    
    final_output = cv2.addWeighted(res_1, 1, 0)
    output_file.write(final_output)

    f = frame - res_1
    f = np.where(f == 0, img, f)
    
    cv2.imshow("magic", final_output)
    cv2.waitKey(1)


cap.release()
out.release()
cv2.destroyAllWindows()