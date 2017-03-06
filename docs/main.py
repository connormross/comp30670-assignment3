'''
Created on 1 Mar 2017

@author: connorross
'''

import argparse
import re 
from builtins import len 
import urllib.request


def main():
    #I use argparse to read in a URL from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--ur',action='store',dest='url',default=None,help='<Required> url link',required=True)
    args = parser.parse_args()
    print(args)
    
    argmts = args.url 
    print(argmts)
    
    #I use request from the urllib to open the content of the URL
    req = urllib.request.urlopen(argmts)

    buffer = req.read().decode('utf-8')
    
    lines = buffer.split('\n')
    
    #I use re.compile to only consider input that is a number
    r = re.compile("([0-9]+)")
    
    lights = set()
    
    for line in lines[1:-1]:
        print(line)
        #findall to assign x1, y1, x2, y2 to the values in lines()
        x1, y1, x2, y2 = [int(x) for x in r.findall(line)]
        if line.startswith('switch'):
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
