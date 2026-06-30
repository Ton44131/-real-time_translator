from views.app_view import App
from views.view_capture_print import CaptureAreaWindow
from models.module_screenshot import CaptureScreenshot
import queue
from rich.traceback import install
import PIL
install()
class ControllerApp:
    def __init__(self):
        self.app_interface = App(self)
        self.translate_frame = None
        self.start_translate = False
        self.queue_img = queue.Queue(maxsize=3)
        self.cont = 0

    def start(self):
        self.app_interface.run()

    def toggle_translation(self):
        self.start_translate = not self.start_translate
        self.check_state()
        print(self.start_translate)

    def check_state(self):
        if self.start_translate:
            if self.cont ==0:
                self.capture_coords()
            self.cont=1
        else:
            self.cont = 0
    
    def capture_coords(self) -> None:
        if self.translate_frame is None:
            self.translate_frame = CaptureAreaWindow(self.app_interface).run()
            self.capture_screen()

    
    def capture_screen(self):
        self.cap_screen = CaptureScreenshot(self.translate_frame,self.queue_img,self)
        self.cap_screen.start()