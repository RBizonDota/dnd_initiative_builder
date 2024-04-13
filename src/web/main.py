import eel

from src.builders.base import BaseIniBuilder


def run_web(file_name: str, builder: BaseIniBuilder):
    """
    Function to run web app
    Parameters:
        file_name (str): file name with config
        builder (BaseIniBuilder): builder
    """
    eel.init("src/web")

    @eel.expose
    def get_chars():
        return builder.build()

    eel.start("./static/html/index.html", mode="browser")
