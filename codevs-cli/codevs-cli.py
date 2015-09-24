#!/usr/bin/env python3
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
from docopt import docopt
from functools import reduce


CMDINVALIDCHAR = ('-','<')


cmd_router = {
    'build': 'build',
    'run': 'run',
    'token': 'token',
    'show': 'show',
    'push': 'push',
    'remove': 'remove'
    }


arguments = docopt(__doc__, version='CodeVS α')

# get right cmd
cmd = reduce(lambda x, y: y[0] if y[1] and not y[0].startswith(CMDINVALIDCHAR) else x, 
                arguments.items(), 'build')

print(arguments)
print(cmd_router[cmd])
