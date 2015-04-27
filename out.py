import numpy as np
##import matplotlib.pyplot as plt
##import cv2
import time

######cv2.namedWindow("Image")
####
####f = file ('out.txt')
####data = f.read()
####f.close()
####print len(data)
####print data
####print "====================================="
####data = np.asarray(data,dtype=None,order=None)
####print data.size
####print data
####print "====================================="
####data = data.reshape((1,1))
####print data
######print data
######cv2.imshow("Image", a)  
######cv2.waitKey (0) 


##a=np.zeros((10,10))
##b=np.ones((10,10))
##d=np.zeros((10,10))
##c=np.column_stack((a, b,d))
####np.row_stack((top, bottom))
##print c
for i in range(1,196):
       f = file('pyout.txt','wb')
       top = np.zeros((i,200))
       mid = np.column_stack((np.zeros((5,i)),np.ones((5,5)),np.zeros((5,195-i))))
       bottom = np.zeros((200-5-i,200))
       a = np.row_stack((top, mid ,bottom))
       f.write(a)
       f.close()
       print i
       time.sleep(1)





