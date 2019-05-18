# Alex's super-light IP cam viewer, by recalling the static jpg with OpenCV

import urllib
import cv2
import numpy as np
import sys

inp = sys.argv[1:]
inp = int(inp[0])
print(inp)

if inp == 0:
	# The back camera provides a succession of jpgs to grab and display
	# while True:
	# 	imgResp = urllib.urlopen(url)
	# 	imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
	# 	img = cv2.imdecode(imgNp,-1)
	# 	cv2.imshow('test',img)
	# 	if ord('q')==cv2.waitKey(10):
	# 		exit(0)
	 url = 'RTSP_STREAM_URL_1_GOES_HERE'
	 cap = cv2.VideoCapture(url)
	 while(True):
	 	ret, frame = cap.read()
	 	cv2.imshow('VIDEO',frame)
	 	if cv2.waitKey(1) & 0xFF == ord('q'):
	 		break


elif inp == 1:
	# The front camera provides an rtsp stream
	 url = 'RTSP_STREAM_URL_2_GOES_HERE'

	 cap = cv2.VideoCapture(url)
	 while(True):
	 	ret, frame = cap.read()
	 	cv2.imshow('VIDEO',frame)
	 	if cv2.waitKey(1) & 0xFF == ord('q'):
	 		break

cap.release()
cv2.destroyAllWindows()

