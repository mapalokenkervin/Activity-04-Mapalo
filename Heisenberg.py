import cv2

print("Heisenberg...")

filePath = 'heisenberg.jpg'
img = cv2.imread(filePath, 1)
cv2.imshow("Heisenberg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()