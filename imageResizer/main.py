#!/usr/bin/env python3

import cv2
img = cv2.imread("img1.jpg", cv2.IMREAD_UNCHANGED)

scale_percent = 20

new_width = int(img.shape[1] * scale_percent / 100)
new_height = int(img.shape[0] * scale_percent / 100)

output = cv2.resize(img, (new_width, new_height))

cv2.imwrite("scenic view.jpg", output)