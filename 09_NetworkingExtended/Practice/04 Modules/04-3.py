'''
### Working With modules ( sys, os, subprocess, argparse, etc....) 

3. Write a script that runs a command to display your current directory.

'''

import sys
import os
from os import curdir

def main():
  
    word = os.getcwdb
    print(f'Here is your thing: {word()}')


if __name__ == '__main__':
    main()