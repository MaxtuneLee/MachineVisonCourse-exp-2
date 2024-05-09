import cv2
import matplotlib.pyplot as plt

src_img = cv2.imread('img.png')

mean_filter = cv2.blur(src_img, (5, 5))
gaussian_filter = cv2.GaussianBlur(src_img, (5, 5), 0)
median_filter = cv2.medianBlur(src_img, 5)
bilateral_filter = cv2.bilateralFilter(src_img, 10, 100, 100)

plt.figure(figsize=(10, 10))

plt.subplot(3, 3, 1)
plt.imshow(cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(3, 3, 2)
plt.imshow(cv2.cvtColor(mean_filter, cv2.COLOR_BGR2RGB))
plt.title('Mean Filter')

plt.subplot(3, 3, 3)
plt.imshow(cv2.cvtColor(gaussian_filter, cv2.COLOR_BGR2RGB))
plt.title('Gaussian Filter')

plt.subplot(3, 3, 4)
plt.imshow(cv2.cvtColor(median_filter, cv2.COLOR_BGR2RGB))
plt.title('Median Filter')

plt.subplot(3, 3, 5)
plt.imshow(cv2.cvtColor(bilateral_filter, cv2.COLOR_BGR2RGB))
plt.title('Bilateral Filter')

plt.show()