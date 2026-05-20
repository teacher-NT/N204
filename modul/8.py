
import cv2

# kamera  = cv2.VideoCapture("http://10.80.186.224:8080/video")
kamera  = cv2.VideoCapture(0)
# is_valid, img = kamera.read()
# if is_valid:
#     cv2.imwrite("rasm.png", img)
#     print("Rasm saqlandi")
# else:
#     print("Rasmga olishda xatolik")

while not (cv2.waitKey(1) & 0xfff == 46):
    is_valid, img = kamera.read()
    if is_valid:
        cv2.imshow("Tasvir", img)
    
    # if cv2.waitKey(1) & 0xfff == 46:
    #     break
