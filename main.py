import cv2
import os
import numpy as np
import imutils

image = cv2.imread('E:\\Open CV\\Images\\tiger.jpg')
print(image.shape)


# # READ IMAGE

# img_path = os.path.join('.', 'Images', 'tiger.jpg')
# image = cv2.imread(img_path)

# # image = cv2.imread('E:\\Open CV\\Images\\tiger.jpg')

# # WRITE IMAGE

# cv2.imwrite(os.path.join('.', 'images', 'tiger_out.jpg'), image)

# # VISUALIZE IMAGE

# cv2.imshow('Tiger', image)
# cv2.waitKey(0)


# # READ VIDEO

# vid_path = os.path.join('.', 'Videos', 'dog.mp4')
# vid = cv2.VideoCapture(vid_path)

# # VISUALIZE VIDEO

# ret = True

# while ret:
#     ret, frame = vid.read()

#     if ret:
#         cv2.imshow('DOG', frame)
#         cv2.waitKey(39)

# vid.release()
# cv2.destroyAllWindows()


# # READ WEBCAM

# wc = cv2.VideoCapture(0)

# # VISUALIZE WEBCAM

# while True:
#     ret, frame = wc.read()

#     cv2.imshow('WEBCAM', frame)
#     if cv2.waitKey(40) & 0xFF == ord('q'):
#         break

# wc.release()
# cv2.destroyAllWindows()



# # BASIC OPERATIONS

# # RESIZING AND CROPPING

# img = cv2.imread(os.path.join('.', 'Images', 'zebra.jpg'))
# resized_img = cv2.resize(img, (132, 91))
# cropped_img = img[50:160, 50:250]

# print(img.shape)
# print(resized_img.shape)
# print(cropped_img.shape)

# cv2.imwrite(os.path.join('.', 'Images', 'zebra_resized.jpg'), resized_img)
# cv2.imwrite(os.path.join('.', 'Images', 'Zebra_cropped.jpg'), cropped_img)

# cv2.imshow('ZEBRA', img)
# cv2.imshow('ZEBRA RESIZED', resized_img)
# cv2.imshow('CROPPED ZEBRA', cropped_img)
# cv2.waitKey(0)



# # COLOR SPACES

# img = cv2.imread(os.path.join('.', 'Images', 'rabbit.jpg'))
# r_img = cv2.resize(img, (1080, 1080))

# cv2.imwrite(os.path.join('.', 'Images', 'rabbit_resized.jpg'), r_img)

# img_rgb = cv2.cvtColor(r_img, cv2.COLOR_BGR2RGB)
# img_gray = cv2.cvtColor(r_img, cv2.COLOR_BGR2GRAY)
# img_hsv = cv2.cvtColor(r_img, cv2.COLOR_BGR2HSV)

# cv2.imshow('RABBIT', r_img)
# cv2.imshow('RABBIT_RGB', img_rgb)
# cv2.imshow('RABBIT_GRAY', img_gray)
# cv2.imshow('RABBIT_HSV', img_hsv)
# cv2.waitKey(0)



# # BLURRING

# img = cv2.imread(os.path.join('.', 'Images', 'free_lancer.jpg'))

# k_size = 7
# blurred_img = cv2.blur(img, (k_size, k_size))
# cv2.imwrite(os.path.join('.', 'Images', 'free_lancer_blurred.jpg'), blurred_img)

# gb_img = cv2.GaussianBlur(img, (k_size, k_size), 3 )
# cv2.imwrite(os.path.join('.', 'Images', 'free_lancer_gb.jpg'), gb_img)

# mb_img = cv2.medianBlur(img, k_size)
# cv2.imwrite(os.path.join('.', 'Images', 'free_lancer_mb.jpg'), mb_img)

# cv2.imshow('FREE_LANCER', img)
# cv2.imshow('FREE_LANCER_BLURRED', blurred_img)
# cv2.imshow('FREE_LANCER_GB', gb_img)
# cv2.imshow('FREE_LANCER_MB', mb_img)
# cv2.waitKey(0)



# # THRESHOLDING 

# img = cv2.imread(os.path.join('.', 'Images', 'bear.jpg'))
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ret, threshold_img = cv2.threshold(gray_img, 80, 255, cv2.THRESH_BINARY)

# threshold_img_blur = cv2.blur(threshold_img, (10, 10))
# ret, threshold_img = cv2.threshold(threshold_img_blur, 80, 255, cv2.THRESH_BINARY)

# cv2.imshow('BEAR', img)
# cv2.imshow('BEAR_GRAY', gray_img)
# cv2.imshow('BEAR_TH', threshold_img)
# cv2.waitKey(0)


# img = cv2.imread(os.path.join('.', 'Images', 'handwriting.jpg'))
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # ret, th_img = cv2.threshold(gray_img, 100, 225, cv2.THRESH_BINARY)
# th_img = cv2.adaptiveThreshold(gray_img, 225, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                                cv2.THRESH_BINARY, 21, 30)

# cv2.imshow('HANDWRITING', img)
# cv2.imshow('HANDWRITING_ATH', th_img)
# cv2.waitKey(0)



# # EDGE DETECTION

# img = cv2.imread(os.path.join('.', 'Images', 'bb.jpg'))
# ed_img = cv2.Canny(img, 100, 200)
# ed_img_d = cv2.dilate(ed_img, np.array((5, 5), dtype = np.int8))
# ed_img_e = cv2.erode(ed_img_d, np.array((5, 5), dtype = np.int8))

# cv2.imshow('BASKETBALL PLAYER', img)
# cv2.imshow('BASKETBALL PLAYER_ED', ed_img)
# cv2.imshow('BASKETBALL PLAYER_ED_DIL', ed_img_d)
# cv2.imshow('BASKETBALL ER', ed_img_e)
# cv2.waitKey(0)



# # DRAWING 

# img = cv2.imread(os.path.join('.', 'Images', 'WB.jpg'))
# print(img.shape)

# # LINE
# cv2.line(img, (100, 250), (450, 600), (0, 0, 250), 5)

# # RECTANGLE
# cv2.rectangle(img, (600, 550), (400, 950), (0, 255, 0), -1)

# # CIRCLE
# cv2.circle(img, (500, 550), 20, (255, 0, 0), 3)

# # TEXT
# cv2.putText(img, 'Hello World !', (100, 250), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 0), 5)

# cv2.imshow('WHITE_BOARD', img)
# cv2.waitKey(0)



# # CONTOURS

# img = cv2.imread(os.path.join('.', 'Images', 'birds.jpg'))
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(gray_img, 80, 255, cv2.THRESH_BINARY_INV)

# contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# for contour in contours:
#     # print(cv2.contourArea(contour))
#     if cv2.contourArea(contour) > 50:
#         # cv2.drawContours(img, contour, -1, (0, 0, 250), 1)

#         x1, y1, w, h = cv2.boundingRect(contour)
#         cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 1)

# cv2.imshow('BIRDS', img)
# # cv2.imshow('BIRDS_GRAY', gray_img)
# cv2.imshow('BIRDS_TH', thresh)
# cv2.waitKey(0)

