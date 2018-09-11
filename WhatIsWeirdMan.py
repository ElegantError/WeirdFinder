import matplotlib.image as mpimg
from os import listdir

#Please fetch files matching the matcher
def getFiles(directory, filterPattern):
    onlyFiles = [f for f in listdir(directory) if filterPattern in f]
    return onlyFiles

#Judges mask file (God mode)
def isWeird(imgPath):
    #assuming img is grayscale
    img = mpimg.imread(imgPath)
    xmax,ymax = img.shape
    xs,ys = [],[]
    for x in range(xmax):
        for y in range(ymax):
            if img[y,x] == 1.0:
                xs.append(x)
                ys.append(y)
    xs.sort()
    ys.sort()
    
    tot = len(xs)
    if tot == 0:        #0 is as regular as they come
        return ((0,0), False)
    
    dx, dy = xs[-1]-xs[0]+1, ys[-1]-ys[0]+1
    
    #rectangles are weird
    return ((dx,dy), dx*dy==tot)

#Exports weirdo fileids to file
def exportWeirdList(saveFileLoc, dirName, maskImgs):
    f = open(saveFileLoc,'w')
    for imgName in maskImgs:
        dims, thisIsWeird = isWeird(dirName + "\\" + imgName)
        #dims provides more info to judge on.  You wanna keep 1x1 masks?  You got the power.
        if thisIsWeird:
            f.write(imgName.replace(".png","") + "\n")
    f.close()
    

#Directory where salt masks are stored.  Don't put a trailing '\' or things will probably go badly.
maskDir = r'C:\Research\MachineLearning\Salt\train\masks'

maskImgs = getFiles(maskDir, ".png")

#DOIT
exportWeirdList(r'C:\Research\MachineLearning\Salt\Code\Python\ListOfWeirdOnes.txt', maskDir, maskImgs)



