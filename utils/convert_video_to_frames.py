import cv2

framesPath = "/frames/monkey-island-I/"
videoPath = "/videos/monkey-island-I/TheSecretOfMonkeyIslandFull.mp4"

def extractImages():
    vidcap = cv2.VideoCapture(videoPath)
    success,image = vidcap.read()
    count = 2
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*5000))
        cv2.imwrite(framesPath + "frame%d.jpg" % count, image)
        success,image = vidcap.read()
        print("Read a new frame: ", success)
        count += 1

if __name__=="__main__":
    extractImages()

