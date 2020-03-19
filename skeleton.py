import cv2 as cv
import numpy as np
img = cv.imread( 'images.png',0 )
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
px = img[:]
print(img.shape)
for i in range(img.shape[0]):
    for j in range( img.shape[1]):
        if img[i][j] > 150:
            img[i][j] = 255
        else:
            img[i][j] = 0
#cv.imshow('img',img)
#cv.waitKey(0)
def thin1( img ):
    for i in range( 1, img.shape[0]-1 ):
        for j in range( 1, img.shape[1]-1 ):
            if img[i][j] == 0:
                cycle = np.array([ img[i-1][j-1], img[i-1][j], img[i-1][j+1], img[i][j+1], 
                img[i+1][j+1], img[i+1][j], img[i+1][j-1], img[i][j-1] ])
                if (np.sum( cycle ) >= 255*2 and np.sum( cycle ) <= 255*6 
                and (cycle[1]+1)*(cycle[3]+1)*(cycle[5]+1)>1 and (cycle[1]+1)*(cycle[7]+1)*(cycle[3]+1)>1):
                    count = 0
                    f = 0
                    while f != 8:
                        if cycle[f] != cycle[ (f-1) % 8 ]:
                            count+=1
                        f+=1
                    if (count//2)==1:
                        img[i][j] = 255
def thin2( img  ):
    for i in range( 1, img.shape[0]-1 ):
        for j in range( 1, img.shape[1]-1 ):
            if img[i][j] == 0:
                cycle = np.array([ img[i-1][j-1], img[i-1][j], img[i-1][j+1], img[i][j+1], 
                img[i+1][j+1], img[i+1][j], img[i+1][j-1], img[i][j-1] ])
                if (np.sum( cycle ) >= 255*2 and np.sum( cycle ) <= 255*6 
                and (cycle[7]+1)*(cycle[3]+1)*(cycle[5]+1)>1 and (cycle[1]+1)*(cycle[7]+1)*(cycle[5]+1)>1):
                    count = 0
                    f = 0
                    while f != 8:
                        if cycle[f] != cycle[ (f-1) % 8 ]:
                            count+=1
                        f+=1
                    if (count//2)==1:
                        img[i][j] = 255
if __name__ == '__main__':
    for i in range(10):
        thin2( img )
        thin1( img )
    cv.imshow('img',img)
    cv.waitKey(0)





