import qrtools, cv2, glob, os

#Initiate qr object
qr = qrtools.QR()

#Check if output folder is present in the Current directory
#If not, create it
if not os.path.exists('output'):
    os.makedirs('output')

#All files in the current directory with .jpg extension
for filename in glob.glob('*.jpg'):

	#If the image contains a qr code, proceed.
	if qr.decode(filename):
		qrcode = qr.data
		#name the output file by the qr text
		name = 'output/' + str(qrcode + '.jpg')
		if name not in glob.glob('output/*.jpg'):

			#Read in the image
			img = cv2.imread(filename)
			#Dimentions of the image
			height, width, depth = img.shape
			orig = img.copy()

			#Convert the image to gray scale for applying canny edge detection
			gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
			gray = cv2.bilateralFilter(gray,11,17,17)
			edged = cv2.Canny(gray,30,200)
			(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
			cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
			screenCnt = None

			#Selecting appropriate contour form the many by rectangle properties and defined limits
			for c in cnts:
				peri = cv2.arcLength(c, True)
				approx = cv2.approxPolyDP(c, 0.02 * peri, True)
				if len(approx) == 4:
					if ((approx[0][0][1] < height/2) and (approx[2][0][1] < height/2) and (approx[0][0][0] > width/2) and (approx[2][0][0] > width/2)):
						screenCnt = approx
						break

			if screenCnt != None:
				#screenCnt is the array of indices of the rectangle, Clockwise from the top left corner
				l1 = screenCnt[0][0][0]
				t1 = screenCnt[0][0][1]
				r1 = screenCnt[2][0][0]
				b1 = screenCnt[2][0][1]
				b1 = b1 - (t1-b1)/2.3

				#Final output image
				image = orig[t1:b1, l1:r1]
				cv2.imwrite(name,image)