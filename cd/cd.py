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
        self.previous = os.getcwd()
        os.chdir(self.current)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.previous)
        if self.temp_directory:
            shutil.rmtree(self.current)
