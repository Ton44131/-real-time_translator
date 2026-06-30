import mss
from threading import Thread
from queue import Queue
import numpy as np
import time
from PIL import Image
class CaptureScreenshot(Thread):
    def __init__(self,coordinates: list[int], queue_img: Queue, controller:object):
        super().__init__(daemon=True)
        self.controller = controller
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
        while self.controller.start_translate:
            while self.queue_img.full():
                self.queue_img.get()
            self.img = self.sct.grab(self.area)
            self.frame = np.array(self.img)
            self.frame = self.frame[:,:,:3]
            self.queue_img.put(self.frame)
            imagem = Image.fromarray(self.frame)
            imagem.save('./img/testes/imagem.png')
            time.sleep(1/self.limit_fps)

# cordenadas = [400,400,400,400]
# queue_img = Queue(maxsize=1)
# t = CaptureScreenshot(cordenadas, queue_img)
# t.start()
             
