"""
This Class deal the file name
"""

import os

class KidFile:

    def __init__(self,filename):
        self.__filename = filename


    @property
    def suffix(self):
        suffix = os.path.splitext(self.__filename)[1]
        return suffix[1:]


    @property
    def filename(self):
        return os.path.basename(self.__filename)


    @property
    def name(self):
        return os.path.splitext(self.filename)[0]


