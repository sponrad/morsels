import os
from tempfile import mkdtemp
from os.path import abspath
import shutil

class cd():
    original_directory = ""
    directory = ""
    temp_directory = False

    def __init__(self, directory=None):
        if directory:
            self.directory = directory
        else:
            temp_directory = mkdtemp()
            self.directory = abspath(temp_directory)
            self.temp_directory = True

    def __enter__(self):
        self.original_directory = os.getcwd()
        os.chdir(self.directory)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.original_directory)
        if self.temp_directory:
            shutil.rmtree(self.directory)
