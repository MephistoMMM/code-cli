
import os

VALID_SAMPLE_SUFFIX = ('c', 'cpp', 'pas')

class KidDir():
    """
    check the file in dir/src/, get it filename
    """

    def __init__(self,dirname):
        dirname = dirname[1:] if dirname.startswith('.') else dirname
        dirname = dirname[2:] if dirname.startswith('./') else dirname
        self.__dirname = dirname

    @property
    def dirabsname(self):
        return os.path.join(os.getcwd(),self.__dirname)

    @property
    def dirsrc(self):
        return os.path.join(self.dirabsname, 'src')

    @property
    def srcfilelist(self):
        return os.listdir(self.dirsrc)

    def getMakeFile(self):pass
        

    def getSample(self):
        samplelist = self.srcfilelist

        for sample in samplelist:
            sampleKidFile = KidFile(os.path.join(self.dirsrc,sample))

            if sampleKidFile.suffix in VALID_SAMPLE_SUFFIX:
                return sampleKidFile



class KidFile():
    """
    This Class deal the file name
    """

    def __init__(self,filename):
        self.__filename = filename


    @property
    def suffix(self):
        suffix = os.path.splitext(self.filename)[1]
        return suffix[1:]


    @property
    def filename(self):
        return os.path.basename(self.__filename)


    @property
    def name(self):
        return os.path.splitext(self.filename)[0]

    @property
    def path(self):
        return os.path.dirname(self.__filename)

