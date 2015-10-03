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
            fileType = self.__kidDir.fileType
            command = self.commandDict[fileType]()
            self.binSh('-c', command, _err=process_errlog)
            
            writeUserLog('codevs info: Congratulation! Build successfully')

        except sh.ErrorReturnCode:
            writeUserLog('codevs error: build err,\n'
                  '\tfailed to build your code,\n'
                  '\tyou should check your code carefully.')
            sys.exit(1)

        except KeyError as err:
            writeUserLog('codevs error: no valid file in src,\n'
                  '\tplease checkout your files suffix.')
            sys.exit(1)
        
        except Exception as err:
            writeUserLog('codevs error: sorry,\n'
                  '\tthere is a error in our cli\n')
            writeCodeVsLog(err)
            sys.exit(1)


    def run(self, args):
        exec_filename = os.path.join(self.dirabsname, 'Main')
        print(args)
        exec_line = ' '.join([exec_filename,args.strip()])

        try:
            self.binSh('-c',exec_line, _err=process_errlog, _out=process_errlog,_in=sys.stdin)

        except sh.ErrorReturnCode:
            writeUserLog('codevs error: run err,\n'
                  '\tthere is a logic error in your code')
            sys.exit(1)

        except Exception as err:
            writeUserLog('codevs error: sorry,\n'
                  '\tthere is a error in our cli\n')
            writeCodeVsLog(err)
            sys.exit(1)



    @property
    def dirsrc(self):
        return self.__kidDir.dirsrc

    @property
    def dirabsname(self):
        return self.__kidDir.dirabsname

    @property
    def commandDict(self):
        def c():
            return ' '.join([
                   'gcc',
                   ' '.join([x.absname for x in self.__kidDir.srcfilelist]),
                   '-DONLINE_JUDGE',
                   '-o %s' % os.path.join(self.dirabsname, 'Main'),
                   # '-static',
                   '-lm',
                   '-Wall',
                   '-O2'])
        def cpp():
            return ' '.join([
                   'g++',
                   ' '.join([x.absname for x in self.__kidDir.srcfilelist]),
                   '-finput-charset=UTF-8',
                   '-o %s' % os.path.join(self.dirabsname, 'Main'),
                   '-static',
                   '-lm',
                   '-Wall',
                   '-O2'])
        def pas():
            return ' '.join([
                   'fpc',
                   ' '.join([x.absname for x in self.__kidDir.srcfilelist]),
                   '-o %s' % os.path.join(self.dirabsname, 'Main')])

        return { 'c':c, 'cpp':cpp, 'pas':pas}


def process_errlog(line, stdin, process):
    writeUserLog(line[:-1])
