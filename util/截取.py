
import cv2
i = 1
#while(True):
filename = "JT6.jpg"
    #filename = "JT" + str(i) + ".jpg"
image = cv2.imread(filename)
    #image2 = image[597: 417, 485:494, :]
image2 = image[441: 465, 301:378]
    #invite_meanValue = np.mean(srcImg[407: 504, 884:992, :] - invite)
    #filename1 = "template" + str(i) + ".jpg"
cv2.imwrite("2.png", image2)
    #cv2.imshow("image-1", image2)
    #cv2.waitKey(0)
    #i += 1

