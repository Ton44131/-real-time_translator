from views.app_view import App

class ControllerApp:
    def __init__(self):
        self.app_interface = App()
    def start(self):
        self.check_state()
        self.app_interface.run()

    def check_state(self):
        self.translate_running = self.app_interface.translent_view.start_translation
        if self.translate_running:
            print('Tradução iniciada')
            self.app_interface.after(100,self.check_state)
            return self.translate_running
        else:
            print('Parado')
        
