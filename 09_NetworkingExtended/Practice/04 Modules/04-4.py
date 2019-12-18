'''
### Working With modules ( sys, os, subprocess, argparse, etc....) 

4. write a ping script where we get user input,and then run a ping request to that host.

'''

import os
 
def get_ping(ip):
  
    command = "ping " + ip
    process = os.popen(command)

    results = str(process.read())
    return results


ip = input('Enter an IP to ping: ')
print(get_ping(ip))