from views.app_view import App
from views.view_capture_print import CaptureAreaWindow
from rich.traceback import install
install()
class ControllerApp:
    def __init__(self):
        self.app_interface = App(self)
        self.translate_frame = None
    def start(self):
        self.app_interface.run()

    def capture_coords(self):
        if self.translate_frame is None:
            self.translate_frame = CaptureAreaWindow(self.app_interface)
            self.app_interface.wait_window(
                self.translate_frame
            )
            self.translate_frame = None
