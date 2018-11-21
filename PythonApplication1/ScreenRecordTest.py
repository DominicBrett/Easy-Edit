import time
import cv2
import mss
import numpy
import subprocess

duration = int(self.duration.text)
framesPerSecond = int(self.framespersecond.text)
frameCount = 0
with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
    
    while frameCount != duration * framesPerSecond:
        
        # Start timer for screenshot
        timerStart = time.time()
        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))

        # Writes Image
        cv2.imwrite("Frames/Frame" + str(frameCount).zfill(7) + ".jpg", img)
        frameCount += 1

        # Finish Timer and work out the total delay to sleep for
        timerFinish = time.time()
        timeTaken = timerFinish - timerStart
        framePadDuration = (1 / framesPerSecond) - timeTaken

        # time.sleep() cannot be given value less than 0
        if (framePadDuration < 0):
            framePadDuration = 0

        time.sleep(framePadDuration)

 # ffmpeg command called via subprocess that creates a video file using images caputred previously, uses image2 demuxerm, pixel format is yuv420p, resoloution is 1920x1080
 # Also getss the file name from the associated text input and inserts it into the ffmpeg statment
makeVidFromFrames = subprocess.call("C:/ffmpeg-4.1-win64-static/bin/ffmpeg.exe -r " + str(
framesPerSecond) + " -f image2 -s  1920x1080 -i Frames/Frame%07d.jpg  -vcodec mpeg4 -crf 25 -pix_fmt yuv420p Video/" + self.output.text+ ".mp4",
shell=True)