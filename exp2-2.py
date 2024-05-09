import cv2
import matplotlib.pyplot as plt
import numpy as np

src_img = cv2.imread('test3.jpg')
src_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)

histogram = cv2.calcHist([src_img], [0], None, [256], [0, 256])

low=10
high=180

# print(histogram)
# auto select r1, r2, s1, s2, from 2-253
areas = []
i = 3
while i < 254:
    start = i
    end = i
    sum = 0
    his = histogram[i]
    if his > 100:
        for j in range(i+1, 254):
            if histogram[j] > 100:
                end = j
                sum += histogram[j]
                i = end
            else:
                break
        areas.append((start, end, sum[0]))
        sum = 0
    i += 1

base = 0
r1, s1 = 0, 0
r2, s2 = 0, 0
for area in areas:
    if area[2] > base:
        base = area[2]
        r1 = area[0]
        s1 = low
        r2 = area[1]
        s2 = high


print("r1: ", areas)


height, width = src_img.shape

rMin = src_img.min()
rMax = src_img.max()

print("Min: ", rMin)
print("Max: ", rMax)

# r1, s1 = 3, 10  # (x1,y1)
# r2, s2 = 70, 180 # (x2,y2)

newImg = np.empty((height, width), np.uint8)
k1 = s1/r1
k2 = (s2-s1)/(r2-r1)
k3 = (255-s2)/(255-r2)

for i in range(height):
    for j in range(width):
        r = src_img[i, j]
        if r <= r1:
            newImg[i, j] = k1*r
        elif r <= r2:
            newImg[i, j] = k2*(r-r1)+s1
        else:
            newImg[i, j] = k3*(r-r2)+s2

plt.figure(figsize=(10, 4))

plt.subplot(2, 3, 1)
plt.axis([0,256,0,256])
x = [0, r1, r2, 255]
y = [0, s1, s2, 255]
plt.plot(x, y)
plt.text(105, 25, "(r1,s1)", fontsize=10)
plt.text(120, 215, "(r2,s2)", fontsize=10)
plt.xlabel("r, Input value")
plt.ylabel("s, Output value")

plt.subplot(2, 3, 2)
plt.imshow(cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(2, 3, 3)
plt.imshow(newImg, cmap='gray')
plt.title('Contrast Stretching')

plt.subplot(2, 3, 4) # histogram of original image
plt.hist(src_img.ravel(), 256, [0, 256])
plt.title('Histogram of Original Image')

plt.show()