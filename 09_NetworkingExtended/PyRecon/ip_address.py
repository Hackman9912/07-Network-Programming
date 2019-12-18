import os
def get_ip_address(urL):

    command = "host " + urL
    process = os.popen(command)
    results = str(process.read())

    marker = results.find('has address') + 12

    return results[marker:].splitlines()[0]
print(get_ip_address('google.com'))
