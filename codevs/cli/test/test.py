import os
import sys

def main(filename):
    print(os.path.abspath(filename))
    print(os.path.join(os.getcwd(),filename))

main(sys.argv[1])

