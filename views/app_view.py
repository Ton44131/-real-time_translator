import customtkinter as ctk
from .view_app_translation_frame import AppTranslationFrame


class App(ctk.CTk):
    """
    Main class of the application interface. To run the program, it is necessary to call the run method.
    """
    def __init__(self, controller) -> None:
        self.cont = 0
        super().__init__()
        self.controller = controller
        self._settings()
        self.nav_bar()
        self.container_main()
        self.translent_view = AppTranslationFrame(self.main, self.controller)
        # self.start_translation_frame()
        self.translent_view.grid(row=0,
                                    column=0,
                                    sticky='nswe',
                                    columnspan=2)

    
    # Initial window settings method
    def _settings(self) -> None:
        self.width_window = self.winfo_screenwidth()
        self.height_window = self.winfo_screenheight()
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((1), weight=1)
        self.after(0, lambda: self.state("zoomed"))
    
    # Navbar creation method
    def nav_bar(self) -> None:
        self.header = ctk.CTkFrame(self,
                                   fg_color='transparent',
                                   height=90)
        self.header.grid(row=0,
                         column=0,
                         columnspan=2,
                         sticky='we'
                         )

    def container_main(self) -> None:
        self.main = ctk.CTkFrame(self,
                                 fg_color='#000'
                                 )
        self.main.grid(row=1,
                       column=0,
                       columnspan=2,
                       sticky='nsew')
        self.main.grid_rowconfigure((0,1,2,3,4), weight=1)
        self.main.grid_columnconfigure((0,1), weight=1)
    
    # def check_state(self):
    #     if self.translent_view.start_translation:
    #         if self.cont ==0:
    #             self.controller.capture_coords()
    #             self.capture_started = True
    #         self.cont=1
    #     else:
    #         self.cont = 0
    #         self.capture_started = False
    #     self.after(100,self.check_state)


    def run(self):
        # self.check_state()
        self.mainloop()

