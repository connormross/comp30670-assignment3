'''
Created on 1 Mar 2017

@author: connorross
'''

import argparse
import numpy
from et_xmlfile.tests.common_imports import read_file
import re 
from builtins import len 
from argcomplete.compat import str

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    
    filename = args.input
    
    buffer = read_file(filename)
    
    lines = buffer.split('\n')
    
    r = re.compile("([0-9]+)")
    
    lights = set()

    for line in (lines):
        x1, y1, x2, y2 = [int(x) for x in r.findall(line)]
        if line.startswith('toggle'):
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    if(x,y) in lights:
                        lights.remove((x,y))
                    else:
                        lights.add((x,y))
                        
        elif line.startswith('turn off'):
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if (x,y) in lights:
                        lights.remove((x,y))
                        
        elif line.startswith('turn on'):
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights.add((x,y))  
                        
        
        
        
    print (len(lights))


    
if __name__ == '__main__':
    main()
