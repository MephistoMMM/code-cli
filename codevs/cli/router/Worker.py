import os,sh,sys
from cli.log.loggers import writeUserLog
from cli.log.loggers import writeCodeVsLog
from cli.lib.KidDir import KidDir

class Worker():
    binSh = sh.Command('/bin/sh')

    def __init__(self, dirname):
        self.__kidDir = KidDir(dirname)

    def build(self):
        #TODO can suppose makefile

        try:
            sample = self.__kidDir.getSample()
            command = self.commandDict[sample.suffix]
            self.binSh('-c', command, _err=process_errlog)
            
            print('codevs info: Congratulation! Build successfully')

        except sh.ErrorReturnCode:
            print('codevs error: build err,\n'
                  '\tfailed to build your code,\n'
                  '\tyou should check your code carefully.')
            sys.exit(1)
        
        except Exception as err:
            print('codevs error: sorry,\n'
                  '\tthere is a error in our cli\n')
            writeCodeVsLog(err.value)
            sys.exit(1)


    def run(self, args):
        exec_filename = os.path.join(self.dirabsname, 'Main')
        exec_line = ' '.join([exec_filename,args.strip()])

        try:
            self.binSh(exec_line, _err=process_errlog, _out=process_errlog,_in=sys.stdin)

        except sh.ErrorReturnCode:
            print('codevs error: run err,\n'
                  '\tthere is a logic error in your code')
            sys.exit(1)

        except Exception as err:
            print('codevs error: sorry,\n'
                  '\tthere is a error in our cli\n')
            writeCodeVsLog(err.value)
            sys.exit(1)



    @property
    def dirsrc(self):
        return self.__kidDir.dirsrc

    @property
    def dirabsname(self):
        return self.__kidDir.dirabsname

    @property
    def commandDict(self):
        return {
                'c':' '.join([
                    'gcc',
                    os.path.join(self.dirsrc,'*'),
                    '-DONLINE_JUDGE',
                    '-o %s' % os.path.join(self.dirabsname, 'Main'),
                    '-static',
                    '-lm',
                    '-Wall',
                    '-O2']),
                'cpp':' '.join([
                       'g++',
                        os.path.join(self.dirsrc,'*'),
                       '-finput-charset=UTF-8',
                       '-o %s' % os.path.join(self.dirabsname, 'Main'),
                       '-static',
                       '-lm',
                       '-Wall',
                       '-O2']),
                'pas':' '.join([
                       'fpc',
                       os.path.join(self.dirsrc,'*'),
                       '-o %s' % os.path.join(self.dirabsname, 'Main')])
                }


def process_errlog(line, stdin, process):
    writeUserLog(line)
