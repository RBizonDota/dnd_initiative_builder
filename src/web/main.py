import eel

from src.builders.base import BaseIniBuilder


def run_web(builder: BaseIniBuilder):
    """
    Function to run web app
    Parameters:
        builder (BaseIniBuilder): builder
    """
    eel.init("src/web")

    @eel.expose
    def get_chars():
        return builder.build()

    eel.start("./static/html/index.html", mode="browser")
