

"""
Segmenting Body Tones using HSV Color Space
"""
import cv2


def remake(img, color='c'):
    imgC = img.copy()
    imgHsv = cv2.cvtColor(imgC, cv2.COLOR_BGR2HSV) 
    lower = (0, 30, 125) #(1, 30, 0)
    upper = (255, 155, 255) #(15, 255, 255)
    mask = cv2.inRange(imgHsv, lower , upper) #Skin tone
    img = cv2.bitwise_and(imgC, imgC, mask=mask)
    if color == 'c':
    	return img
    if color == 'g':
    	img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    	return img

if __name__ == '__main__':
	path = r"C:\Input_Folder\test.png"
	image = cv2.imread(path)
	BodyTones = remake(image)
	cv2.imshow('BodyTones',BodyTones); 
	cv2.waitKey(1)


