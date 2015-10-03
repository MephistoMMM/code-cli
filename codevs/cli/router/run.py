"""
codevs run <dir> <args>
build files and run the Main
"""
from cli.lib.KidDir import KidDir
from cli.router.build import build
from cli.router.Worker import Worker

def run(arguments):
    buildWorker = build(arguments)
    programArgs = ' ' if arguments['--args'] is None else arguments['--args']
    buildWorker.run(programArgs)

    return buildWorker

    
