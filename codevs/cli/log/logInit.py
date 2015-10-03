"""
we need two loggers,
    the first is used to say the result of running to user,
    the second is used to save the result of sys error in log file.
"""
import logging, sys, os
import os.path as path

FILE_LOGGER_NAME = 'codevs_error.log'
FILE_LOGGER_FILENAME = path.join(path.dirname(path.abspath(__file__)), FILE_LOGGER_NAME)
CODEVS_ERROR_FORMAT = '------------------------------------------------\n'\
                      '%(asctime)-15s  %(message)s: \n'\
                      'At  %(filename)s -> %(funcName)s -> %(lineno)d\n'\
                      '%(stack)s\n\n'\
                      'Over'

def setupLogger():

    # root logger
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter())
    console_handler.setLevel(logging.INFO)
    user_root_logger = logging.getLogger('user_root')
    user_root_logger.addHandler(console_handler)
    user_root_logger.setLevel(logging.INFO)

    # codevs error logger
    file_handler = logging.FileHandler(FILE_LOGGER_FILENAME, mode='w',encoding='utf8')
    file_handler.setFormatter(logging.Formatter(CODEVS_ERROR_FORMAT))
    file_handler.setLevel(logging.ERROR)
    codevs_root_logger = logging.getLogger('codevs_root')
    codevs_root_logger.addHandler(file_handler)
    codevs_root_logger.setLevel(logging.ERROR)


def checkOldLogger():
    """
    this check the log file whether is exited,
    if it is exited , it means there is a error in latest running,
    so we should send it to CodeVs .
    """
    try:
        with open(FILE_LOGGER_FILENAME, mode='r') as f:
            #TODO this need send err imformation to CodeVS
            if '-' in f.readline():
                print('this is an error in your latest running codevs')
                return True

    except FileNotFoundError as err: pass



