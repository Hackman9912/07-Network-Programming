'''
### Working With modules ( sys, os, subprocess, argparse, etc....) 

1. Write a script that runs a command (like "ls -l", it can be any command you choose). 
'''

import os
import sys
import time
import subprocess
import argparse


def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('-t', '--title', help="Set the title for a cmd prompt")
	return parser.parse_args()

def change_title(title):
	print('Setting CMD title to ' + str(title))
	subprocess.Popen(['title', title], shell=True)
	


options = get_arguments()
change_title(options.title)


