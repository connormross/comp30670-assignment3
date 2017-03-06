'''
Created on 1 Mar 2017

@author: connorross
'''
import sys 
import argparse
import numpy
from et_xmlfile.tests.common_imports import read_file
import re 
from builtins import len 
from argcomplete.compat import str
import urllib.request


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--ur',action='store',dest='url',default=None,help='<Required> url link',required=True)
    args = parser.parse_args()
    print(args)
    
    argmts = args.url 
    print(argmts)
    
    req = urllib.request.urlopen(argmts)

    buffer = req.read().decode('utf-8')
    print(buffer)

    
    


    
if __name__ == '__main__':
    main()
