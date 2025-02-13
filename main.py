import cv2
import os

# image = cv2.imread('E:\\Open CV\\Images\\tiger.jpg')
# print(image.shape)


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



# COLOR SPACES

img = cv2.imread(os.path.join(',', 'Images', 'rabbit.jpg'))
cv2.imshow('RABBIT', img)
cv2.waitKey(0)