"""
codevs build <dir>               
build files acrroding to filepath
build     Build the file to executable file
"""
from .Worker import Worker

def build(arguments):
    buildWorker = Worker(arguments['<dir>'])
    buildWorker.build()
    
    return buildWorker





