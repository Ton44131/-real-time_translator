import tkinter as tk

class CaptureAreaWindow(tk.Toplevel):

    """
    Class to select the coordinates that will be used to create the translation window.
    
    Use the run method to start.
    """
    def __init__(self,master) -> None:
        super().__init__(master)
        self._settings()

        # coordinate attributes
        self.x0 = 0
        self.y0 = 0
        self.coordinates = []

        self.area_capture = None
        self._setup_capture_canvas()

    def _settings(self) -> None:
        """Configure window settings"""

        self.attributes('-fullscreen', True,
                        '-alpha',0.3,
                        '-topmost',True
                        )
    
    def _setup_capture_canvas(self) -> None:
        """Create the widgets used in the capture window."""

        self.capture_canvas = tk.Canvas(self,
                                        bg='#000')
        self.capture_canvas.pack(fill='both',
                                 expand=True)
        self._bind_canvas_events()
    
    def _bind_canvas_events(self) -> None:
        """Configure mouse events for capture selection."""

        self.capture_canvas.bind('<Button-1>', self.on_event_mouse_click)
        self.capture_canvas.bind('<B1-Motion>', self.on_event_mouse_movement)
        self.capture_canvas.bind('<ButtonRelease-1>', self.on_capture_complete)


    def on_event_mouse_click(self, event) -> None:
        """Creates the starting point of the capture area."""

        self.x0, self.y0  = event.x, event.y
        self.area_capture = self.capture_canvas.create_rectangle(self.x0,
                                                                 self.y0,
                                                                 event.x,
                                                                 event.y,
                                                                 width=5,
                                                                 outline='lime'
                                                                 )

    def on_event_mouse_movement(self,event) -> None:
        """Define the final coordinates of the selected area."""
        self.capture_canvas.coords(self.area_capture,
                                       self.x0,
                                       self.y0,
                                       event.x,
                                       event.y)
        
    def on_capture_complete(self,_) -> None:
        """ Set the coordinates for future return."""
        self.coordinates = list(map(int,self.capture_canvas.coords(self.area_capture)))
        self.destroy()

    def run(self) -> list[int,int,int,int]:
        """A method that initializes and returns the final value of the coordinates of the selected area."""
        self.wait_window()
        return self.coordinates   
