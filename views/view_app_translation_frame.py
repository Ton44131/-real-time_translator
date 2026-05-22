import customtkinter as ctk


class AppTranslationFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.start_translation = False

        self.from_lenguage_opition = ["Inglês"]
        self.to_lenguage_opition = ["Português"]

        self.config_frame()

    def config_frame(self) -> None:

        # Frame interno para centralizar os widgets
        self.container = ctk.CTkFrame(
            self,
            fg_color='transparent'
        )

        self.container.grid_rowconfigure((0,1), weight=1)
        self.container.grid_columnconfigure((0,1), weight=1)

        self.container.place(
            relx=0.5,
            rely=0.5,
            anchor='center'
        )

        self.wigets_frame_start_translation()

    def wigets_frame_start_translation(self) -> None:

        self.view_from_lenguage()
        self.view_arrow()
        self.view_to_lenguage()
        self.create_start_button()

    def view_from_lenguage(self) -> None:

        self.tittle_opition_from_lenguage = ctk.StringVar(
            value='Escolha o idioma'
        )

        self.from_lenguage_opition_menu = ctk.CTkOptionMenu(
            self.container,
            values=self.from_lenguage_opition,
            variable=self.tittle_opition_from_lenguage,
            width=140
        )

        self.from_lenguage_opition_menu.grid(
            row=0,
            column=0,
            padx=(0, 5)
        )

    def view_arrow(self) -> None:

        self.arrow = ctk.CTkLabel(
            self.container,
            text='→',
            font=('Arial', 28, 'bold')
        )

        self.arrow.grid(
            row=0,
            column=1
        )

    def view_to_lenguage(self) -> None:

        self.tittle_opition_to_lenguage = ctk.StringVar(
            value='Escolha o idioma'
        )

        self.to_lenguage_opition_menu = ctk.CTkOptionMenu(
            self.container,
            values=self.to_lenguage_opition,
            variable=self.tittle_opition_to_lenguage,
            width=140
        )

        self.to_lenguage_opition_menu.grid(
            row=0,
            column=2,
            padx=(5, 0)
        )
    
    def teste(self):
        self.start_translation = not self.start_translation
        self.text_stop_translation = 'Parar tradução'
        self.text_start_translation = 'Iniciar tradução'

        

        if self.start_translation:
            self.start_button.configure(text=self.text_stop_translation)
        else:
            self.start_button.configure(text=self.text_start_translation)
            
    def create_start_button(self) -> None:
        self.start_button = ctk.CTkButton(self.container,
                                          text='Iniciar tradução',
                                          command=self.teste)
        self.start_button.grid(row=1,
                               column=0,
                               columnspan=3)