import os
from tempfile import mkdtemp
from os.path import abspath
import shutil

class cd():
    previous = ""
    current = ""
    temp_directory = False

    def __init__(self, directory=None):
        if directory:
            self.current = directory
        else:
            temp_directory = mkdtemp()
            self.current = abspath(temp_directory)
            self.temp_directory = True

    def __enter__(self):
        return self.enter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.exit()

    def enter(self):
        self.previous = os.getcwd()
        os.chdir(self.current)
        return self

    def exit(self):
        os.chdir(self.previous)
        if self.temp_directory:
            shutil.rmtree(self.current)
