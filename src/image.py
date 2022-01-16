"""
sample image to ascii
"""
import cv2

CHARS = " ,.-~;:=!*#%@"

img = cv2.imread('/home/bsch0111/Desktop/airshare/sample.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

new_width = 100
h, w =img.shape
nh = int(h/w * new_width )

img = cv2.resize(img, (new_width*2, nh))

for row in img: #이미지를 행별로 출력
    for pixel in row: #이미지를 픽셀 별로 출력 0~255 -> CHARS
        index = int(pixel/256*(len(CHARS)))
        print(CHARS[index], end='')
    print()
