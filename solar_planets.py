import cv2

img = cv2.imread("solar-system.jpg")
#cv2.imshow("Output", img)

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255))

cv2.putText(img,
            "Mercury",
            (80,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255))

cv2.putText(img,
            "Venus",
            (185,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255))

cv2.putText(img,
            "Earth",
            (280,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255))

cv2.putText(img,
            "Mars",
            (380,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255))

cv2.putText(img,
            "Jupitar",
            (525,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255))

cv2.putText(img,
            "Saturn",
            (765,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255))

cv2.putText(img,
            "Uranus",
            (945,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255))

cv2.putText(img,
            "Neptun",
            (1100,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,255,255))

cv2.imwrite("Solar_Systemwithname.jpg",img)
cv2.waitKey(0)