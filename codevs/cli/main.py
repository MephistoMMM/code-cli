#!/usr/bin/env python3
import sys
sys.path.append('..')

from docopt import docopt
from functools import reduce

from .log import loggers
from .router.build import build
from .router.run import run

CMDINVALIDCHAR = ('-','<')

cmd_router = {
    'build': build,
    'run': run,
    'token': 'token',
    'show': 'show',
    'push': 'push',
    'remove': 'remove'
}


def main():
    """CodeVS

    Usage:
      codevs [options]
      codevs build <dir>               
      codevs run [--args=ARGS] <dir> 
      codevs token <token> <file>
      codevs show
      codevs push <token>
      codevs rm <token>                 

    Cmd:
      build     Build the files in dir/src/ to executable file(dir/Main)
                ——you should put your source file into dir/src
      run       Build the files in dir/src/ to executable file(dir/Main) and exec it, you can use -a or --args to set arguments for your program
                ——you should put your source file into dir/src
      token     Set a Token to a file
      show      Show all token file
      push      Push a file with especial token 
      rm        Remove a token and the file if it exist.

    Options:
      -h --help     Show this screen.
      --version     Show version.

    """
    arguments = docopt(main.__doc__, version='CodeVS α')

    # get right cmd
    cmd = cliCommond(arguments)

    print(arguments)
    cmd_router[cmd](arguments)





def cliCommond(args):
    return reduce(
            lambda x, y: y[0] if y[1] and not y[0].startswith(CMDINVALIDCHAR) else x,
            args.items(), 'build')
