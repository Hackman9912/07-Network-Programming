'''
### Working With modules ( sys, os, subprocess, argparse, etc....) 

5. Create a script that will accept a single integer as a positional argument, and will print a hash symbol that amount of times.

'''

import os
import sys
import time
import subprocess
import argparse


def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--integer', help="Set the number of octothorps to print by hitting -i (your number). ")
	return parser.parse_args()

def print_octothorp(octo, numb):
	print('Getting this many octothorps: ' + numb + '\n' + str(octo))

options = get_arguments()
octo = '#' * int(options.integer)
print_octothorp(octo, options.integer)