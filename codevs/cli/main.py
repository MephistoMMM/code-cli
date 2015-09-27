#!/usr/bin/env python3
from docopt import docopt
from functools import reduce

from log.logInit import setupLogger, checkOldLogger


CMDINVALIDCHAR = ('-','<')

cmd_router = {
    'build': 'build',
    'run': 'run',
    'token': 'token',
    'show': 'show',
    'push': 'push',
    'remove': 'remove'
}


def main():
    """CodeVS

    Usage:
      codevs [options]
      codevs build <file>               
      codevs run <file> 
      codevs token <token> <file>
      codevs show
      codevs push <token>
      codevs rm <token>                 

    Cmd:
      build     Build the file to executable file
      run       Build the file to executable file and exec it
      token     Set a Token to a file
      show      Show all token file
      push      Push a file with especial token 
      rm        Remove a token and the file if it exist.

    Options:
      -h --help     Show this screen.
      --version     Show version.

    """
    logInit()
    setupLogger()
    arguments = docopt(main.__doc__, version='CodeVS α')

    # get right cmd
    cmd = cliCommond(arguments)

    print(arguments)
    print(cmd_router[cmd])



def cliCommond(args):
    return reduce(
            lambda x, y: y[0] if y[1] and not y[0].startswith(CMDINVALIDCHAR) else x,
            args.items(), 'build')
