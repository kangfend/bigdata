import os
print(os.getcwd()) # Return the current working directory
os.chdir('/home/ayam/Code/bigdata') # Change current working directory
print(os.system('mkdir today')) # Run the command mkdir in the system shell

print(dir(os)) # <returns a list of all module functions>
print(help(os)) # <returns an extensive manual page created from the module's docstrings>

import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/today', 'also-today')
