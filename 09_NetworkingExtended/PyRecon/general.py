# Importing os to make operating system calls using Python
import os

# Function to create a new directory
def create_dir(directory):

    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to write data to a file
def write_file(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()
