import os

class cd():
    original_directory = ""

    def __init__(self, directory):
        self.directory = directory

    def __enter__(self):
        self.original_directory = os.getcwd()
        os.chdir(self.directory)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.original_directory)
