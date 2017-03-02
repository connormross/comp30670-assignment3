'''
Created on 1 Mar 2017

@author: connorross
'''

import argparse
import numpy
from et_xmlfile.tests.common_imports import read_file

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    
    filename = args.input
    
    buffer = read_file(filename=filename)
    
    lines = buffer.split('\n')

    size = int(lines[0])
    
    tester = LEDTester(size)
    
    for i, line in enumerate(lines[1:]):
        tester.execute_command(line)
        
    print("{} {}".format(filename, tester.count_lighting()))
    return

class LEDTester:
    
    
    
if __name__ == '__main__':
    main()
