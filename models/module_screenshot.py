import mss
from threading import Thread
from queue import Queue
import numpy as np
import time
class CaptureScreenshot(Thread):
    def __init__(self,coordinates: list[int], queue_img: Queue):
        super.__init__()
        self.queue_img = queue_img
        self.sct = mss.mss()
        self.limit_fps = 15

        self.area = {
            'top':coordinates[1],
            'left':coordinates[0],
            'width':coordinates[2],
            'height': coordinates[3]
        }

    def run(self):
        
        while True:
            while self.queue_img.full():
                self.queue_img.get()
            self.img = self.sct.grab(self.area)
            self.frame = np.array(self.img)
            self.frame = self.img[:,:,:3]
            self.queue_img.put(self.frame)
            time.sleep(1/self.limit_fps)