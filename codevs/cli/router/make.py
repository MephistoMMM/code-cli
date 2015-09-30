"""
codevs make [<target>] [options]
make files acrroding to makefile
"""
from .MakeWorker import MakeWorker

def make(arguments):
    args = []
    makeWorker = MakeWorker()
    
    if arguments['<target>'] is not None: 
        args.append(arguments['<target>'])
    if arguments['-C'] is not None: 
        args.append('-C')
        args.append(arguments['-C'])
    if arguments['-f'] is not None: 
        args.append('-f')
        args.append(arguments['-f'])

    makeWorker.make(' '.join(args))

    
