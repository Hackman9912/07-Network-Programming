'''
### Working With modules ( sys, os, subprocess, argparse, etc....) 

2. Write a script that runs a command and captures the number of bytes in a print statement.

'''

import sys
import os
from os import curdir

def main():
  
    word = os.getcwdb
    print(f'Here is your thing: {word()}')
    print(sys.getsizeof(word()))

if __name__ == '__main__':
    main()