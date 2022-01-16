"""
sample video to ascii
"""
import cv2

CHARS = " ,.-~;:=!*#%@"
#CHARS = " ,./?;:~!@#%^*(-=_+q"
cap = cv2.VideoCapture('/home/bsch0111/Desktop/airshare/IMG_5431.MP4')

print("\x1b[2J", end='')
while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break # 읽어오고 프레임이 없으면 그만둔다.


    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    new_width = 60
    h, w =img.shape
    nh = int(h/w * new_width )

    img = cv2.resize(img, (new_width*2, nh))

    for row in img: #이미지를 행별로 출력
        for pixel in row: #이미지를 픽셀 별로 출력 0~255 -> CHARS
            index = int(pixel/256*(len(CHARS)))
            print(CHARS[index], end='')
        print()
    print("\x1b[H", end='')
