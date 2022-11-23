import pickle
import os


def connect(file):
    with open(file, "rb") as handle:
        f = FqlServer(file)
        try:
            f.table = pickle.loads(handle.read())
        except:
            pass
        return f

class FqlServer():
    def __init__(self, file):
        self.table = {}
        self.named_file = file

    def call(self, query):
        exec(query)
        self.save()


    def save(self):
        with open(self.named_file, "wb") as handle:
            handle.write(pickle.dumps(self.table))

    def setvalue(self, key, value):
        self.table[key] = value
        self.save()

    def getvalue(self, key):
        return self.table[key]