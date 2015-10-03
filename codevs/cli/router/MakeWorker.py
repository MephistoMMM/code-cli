import os,sh,sys
from cli.log.loggers import writeUserLog
from cli.log.loggers import writeCodeVsLog

class MakeWorker():
    binSh = sh.Command('/bin/sh')

    def make(self, argstrnig):
        try:
            self.binSh('-c', ' '.join(['make', argstrnig]), _err=process_errlog)

        except sh.ErrorReturnCode:
            print('codevs error: make err,\n'
                  '\tfailed to make your code,\n'
                  '\tyou should check your code or makefile carefully.')
            sys.exit(1)
        
        except Exception as err:
            print('codevs error: sorry,\n'
                  '\tthere is a error in our cli\n')
            writeCodeVsLog(err)
            sys.exit(1)


def process_errlog(line, stdin, process):
    writeUserLog(line)
