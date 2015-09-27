"""
KidFile
"""

from os import path as osp
from KidFile import KidFile

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


