#!/usr/bin/env python3
import sys, signal
sys.path.append('..')

from docopt import docopt
from functools import reduce

from .log import loggers
from .router.build import build
from .router.run import run
from .router.make import make

CMDINVALIDCHAR = ('-','<')

cmd_router = {
    'build': build,
    'run': run,
    'make': make,
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
      codevs run [options] <dir> 
      codevs make [options] [<target>] 
      codevs token <token> <file>
      codevs show
      codevs push <token>
      codevs rm <token>                 

    Cmd:
      build     Build the files in dir/src/ to executable file(dir/Main)
                ——you should put your source file into dir/src
      run       Build the files in dir/src/ to executable file(dir/Main) and exec it, you can use -a or --args to set arguments for your program
                ——you should put your source file into dir/src
      make      build your program accroding your makefile, also you can use target , e.g. make -f ./example.mk install
      token     Set a Token to a file
      show      Show all token file
      push      Push a file with especial token 
      rm        Remove a token and the file if it exist.

    Options:
      for run
      -a --args     set arguments for your program
      
      for make
      -f FILE       set makefile name as FILE not makefile
      -C DIR        set make dir as DIR not crrunt dir

      -h --help     Show this screen.
      --version     Show version.

    """
    try:
        setup_signal()
        arguments = docopt(main.__doc__, version='CodeVS α')

        # get right cmd
        cmd = cliCommond(arguments)
        cmd_router[cmd](arguments)

    except KeyError :
        message = '{:-^70}\n'.format('CodeVs')
        message += 'Welcome to use CodeVs-cli!\n\n'
        message += 'You should use "codevs build your_project_dir" to build source to exec\nutable file,\n'
        message += 'Also , you may want to "codevs run your_project_dir" to run project di\nrectly,\n'
        message += 'Linuxer like write makefile , just run command "codevs make".\n'
        message += '\n"codevs --help" give you more help information.\n'
        message += '{:-^70}\n'.format('To Code Fun!')
        message += '{: >70}\n'.format('lovely by wph95, mpsss and CodeVsers')
        loggers.writeUserLog(message)

    except Exception as err:
        print('codevs error: sorry,\n'
              '\tthere is a error in our cli\n')
        loggers.writeCodeVsLog(err.value)
        sys.exit(1)


def cliCommond(args):
    return reduce(
            lambda x, y: y[0] if y[1] and not y[0].startswith(CMDINVALIDCHAR) else x,
            args.items(), 'wrong_key')



def setup_signal():
    def signal_handler(signal, frame):
        print('Thanks for using codevs!')
        sys.exit(1)
    signal.signal(signal.SIGINT, signal_handler)
