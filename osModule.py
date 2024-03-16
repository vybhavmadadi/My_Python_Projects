# OS Module tutorial notes
import os #Standard OS module
from datetime import datetime #Import datetime function from datetime module

# print(dir(os)) #Print all the attributes and methods in this module.
# print(os.getcwd()) #Print current working directory

os.chdir('/Users/vybhav/Desktop/') #Change working directory to new path

# CREATE NEW DIRECTORY OR DIRECTORIES
# os.mkdir('PythonTest') #Makes a new directory. Cannot be used to make sub directories under the directory that is being created.
# MOST COMMONLY USED.
# os.makedirs('PythonTest/SubDirOne') #Makes a new directory and can also make sub-directories underneath.

# REMOVE A DIRECTORY OR DIRECTORIES
# os.rmdir('PythonTest') #Removes a new directory. Cannot be used to remove sub directories.
# os.removedirs('PythonTest') #Removes directories and sub-directories.

# RENAME A FILE
# os.rename('Nissan-Xtrail.mov', 'Nissan.mov') #Rename a file, first comes the existing file name and then the second one.

# GET INFO ON A FILE
# print(os.stat('Nissan.mov')) # Get all info on a file
# print(os.stat('NIssan.mov').st_size) #Get file size in bytes
# print(os.stat('Nissan.mov').st_mtime) #Get last change date/time in base format
    #If you want to show the datetime in readable format, import datetime module and use it like this
# mod_time = os.stat('Nissan.mov').st_mtime #Pass the last modified date time to a variable
# print(datetime.fromtimestamp(mod_time)) #Using datetime module to print the last modified date in a readable format

# TRAVERSE DIRECTORY TREE AND ALL FILES WITHIN / DIRECTORY TREE GENERATOR
# the output yeilds a three value tuple. Directory Path, Directory name within path, file names within path
# for dirpath, dirnames, filenames in os.walk('/Users/vybhav/Desktop/'):
#     print('Current Path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)
#     print()

# GET ENVIORNMENT VARAIBLE(S)
# print(os.environ.get('HOME'))
    #create a new file using above environment
# file_path = os.environ.get('HOME') + 'test.txt' #THIS METHOD MAY PRODUCE INCORRECT ERRORS, like this one
                                                # where the path is missing a slash
# print(file_path)    # You can see here how the path is missing a slash differentiation home dir and the file name
# USE OS.PATH TO JOIN TWO PATHS
# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
# print(file_path)
# These commands will be useful to read a path that you might want to know and base your code on.
print(os.path.basename('/tmp/test.txt')) #Get the file name of a path. Does not matter if file exists or not
print(os.path.dirname('/tmp/test.txt')) #Get the directory name of a path. Does not matter if file exists or not
print(os.path.split('/tmp/test.txt')) #Split the directory name and path. Does not matter if file exists or not
print(os.path.exists('/tmp/test.txt')) #Check if a path exists
print(os.path.isdir('/tmp/fdgdfsfd')) #Check if path is a directory
print(os.path.isfile('/tmp/text.txt')) #Check if path is a file
print(os.path.splitext('/tmp/test.txt')) #Split path root and extension

print(os.listdir()) #You can pass a path in the brackets, but the basic function lists all the files in the current directory



