import os.path


class FileReader:

    def __init__(self, filename):
            self.filename = filename

    def read(self):
        try:
            if not os.path.exists(self.filename):
                raise FileNotFoundError(f"file {self.filename} not found")
        except FileNotFoundError as err:
            print(err.args[0])
            return None
        else:
            with open(self.filename, 'r') as file:
                return file.read()

    def second_read(self):
        try:
            with open(self.filename, 'r') as file:
                file.read()
        except IOError:
            print("file not found")
            return None
