import shutil
from functools import partial
import os


class Decode:
    def __init__(self, path=None):
        self.block_size = 1024 * 1024 * 8
        self.path = path if path is not None else os.getcwd()

    def read_from_file(self, filename, block_size=1024 * 1024 * 8):
        with open(filename, "rb") as fp:
            for chunk in iter(partial(fp.read, block_size), b''):
                yield chunk

    def normalize(self, filename, block_size=1024 * 1024 * 8):
        data = self.read_from_file(filename, block_size=block_size)
        fp = open(filename.split('.')[0] + "_decode.mp4", "wb")
        i = 0
        for d in data:
            if i == 0:
                fp.write(d[3:])
                i = 1
            else:
                fp.write(d)

        fp.close()

    def decode_all(self, block_size=1024 * 1024 * 8, inplace=False):
        l = os.listdir(self.path)
        os.chdir(self.path)
        for filename in l:
            if "mp4" in filename:
                print("decode:", filename)
                self.normalize(filename)
                if inplace:
                    os.remove(filename)
                    os.rename(filename.split('.')[0] + "_decode.mp4", filename)
