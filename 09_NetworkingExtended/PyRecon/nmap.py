# Importing os
import os
# Function to get Nmap Port Scan
def get_nmap ( options, ip ):
	command = "nmap " + options + " " + ip
	process = os.popen( command )
	results = str( process.read() )
	# Returning the final result
	return results
print(get_nmap('-F','127.0.0.1'))
print("Nmap Scan done!")

