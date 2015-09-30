"""
test list 
"""
import sys
sys.path.append('..')

def loggers():
    """
    loggers
    """
    import logging
    import os
    from log.logInit import checkOldLogger
    from log.logInit import FILE_LOGGER_FILENAME

    user_root_logger = logging.getLogger('user_root')
    codevs_root_logger = logging.getLogger('codevs_root')

    user_root_logger.info('user_root_logger info run ok!')
    user_root_logger.debug('user_root_logger debug run ok!')
    user_root_logger.error('user_root_logger error run ok!')
    user_root_logger.warning('user_root_logger warning run ok!')
    user_root_logger.critical('user_root_logger critical run ok!')

    stack = {'stack': 'fuckkkkkkkkkkkkkkkkkkkkkkkkk'}
    codevs_root_logger.info('codevs_root_logger info run ok!',extra=stack)
    codevs_root_logger.debug('codevs_root_logger debug run ok!',extra=stack)
    codevs_root_logger.error('codevs_root_logger error run ok!',extra=stack)
    codevs_root_logger.warning('codevs_root_logger warning run ok!',extra=stack)
    codevs_root_logger.critical('codevs_root_logger critical run ok!',extra=stack)

    assert checkOldLogger() == True , 'error log file should be exist!'
    os.remove(FILE_LOGGER_FILENAME)


def kidDir():
    """
    KidDir
    """
    from os import path as osp
    from lib.KidDir import KidDir
    from lib.KidDir import VALID_SAMPLE_SUFFIX

    PATH = './test'
    kidDir = KidDir(PATH)
    sampleKidFile = kidDir.getSample()

    assert sampleKidFile.suffix in VALID_SAMPLE_SUFFIX, 'suffix wrang!'



def kidFile():
    """
    KidFile
    """
    from os import path as osp
    from lib.KidDir import  KidFile

    PATH = osp.dirname(osp.abspath(__file__))
    FIRST = 'kidFile'
    SECONDE = 'codeVs.py'
    THIRD = '.docker'
    FOUR = '.docker.png'

    path1 = osp.join(PATH,FIRST)
    path2 = osp.join(PATH,SECONDE)
    path3 = osp.join(PATH,THIRD)
    path4 = osp.join(PATH,FOUR)

    kidFile1 = KidFile(path1)
    kidFile2 = KidFile(path2)
    kidFile3 = KidFile(path3)
    kidFile4 = KidFile(path4)


    assert kidFile1.suffix =='', '1 suffix should be space'
    assert kidFile2.suffix =='py', '2 suffix should be py'
    assert kidFile3.suffix =='', '3 suffix should be space.' 
    assert kidFile4.suffix =='png', '4 suffix should be png' 

    assert kidFile1.filename =='kidFile', '1 filename should be kidFile'
    assert kidFile2.filename =='codeVs.py', '2 filename should be codeVs.py'
    assert kidFile3.filename =='.docker', '3 filename should be .docker'
    assert kidFile4.filename =='.docker.png', '4 filename should be .docker.png' 


    assert kidFile1.name =='kidFile', '1 name should be kidFile'
    assert kidFile2.name =='codeVs', '2 name should be kidFile2'
    assert kidFile3.name =='.docker', '3 name should be kidFile3'
    assert kidFile4.name =='.docker', '4 name should be .docker' 

    assert kidFile1.path ==PATH, '1 path should be {}'.format(PATH)
    assert kidFile2.path ==PATH, '2 path should be {}'.format(PATH)
    assert kidFile3.path ==PATH, '3 path should be {}'.format(PATH)
    assert kidFile4.path ==PATH, '4 path should be {}'.format(PATH) 


testList = []
testList.append(kidFile)
testList.append(loggers)
testList.append(kidDir)

result = {'all':0, 'success': 0, 'fail': 0}


for testaim in testList:
    result['all'] += 1
    try:
        testaim()
        result['success'] += 1

    except AssertionError as err:
        result['fail'] += 1
        print("{} testfalue!\n\t{}.\n".format(
                testaim.__name__, err))
else:
    print('\n{:-^20}\n'
          'all test {all}, success {success}, fail {fail}\n'.format('', **result))


    
    
        
