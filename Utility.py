import sys
import os


def resource_path(relative_path):
    """
    Utility function for loading data (i.e. images) with a specific path in mind. Haven't fully understood
    how to use it yet, as it will try and store data within the temp folder when running the game
    as an executable after building with Pyinstaller. However, this data is then somehow not actually
    read and causes the game to crash.
    :param relative_path: relative path to data from the current file
    :return: properly formatted path
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
