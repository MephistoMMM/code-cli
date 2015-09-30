"""
there are functions for write logs
"""
import sys
import logging ,traceback
from .logInit import FILE_LOGGER_FILENAME

user_root_logger = logging.getLogger('user_root')
codevs_root_logger = logging.getLogger('codevs_root')

def writeUserLog(msg):
    user_root_logger.info(msg)



def writeCodeVsLog(msg):
    """
    write log then do something ,
    sys.exit()
    """
    codevs_root_logger.error(msg, 
            extra={'stack':traceback.format_exc()})

    # with open(FILE_LOGGER_FILENAME, mode='r', encoding='utf8') as f:
        # print(f.read())
        #TODO send this file to Codevs

    sys.exit(1)



