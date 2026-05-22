from controllers.controller_interface import ControllerApp
from rich.traceback import install
install()
if __name__ == "__main__":
    start = ControllerApp()

    start.start()