# Use python to automate parsing and renaming of multiple files in a folder

# Imports
import os

os.chdir('/Users/vybhav/Desktop/Videos/') # Change directory to the directory where the files are

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f) # Separating file name and extension into two variables
    f_title, f_course, f_num = f_name.split('-') # Splitting the file name using the separater as -

    f_title = f_title.strip() # Strips leading and trailing spaces
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2) # Strips leading and trailing spaces and the first char of the string. ZFILL makes the string a minimum of defined character size, in this ex, it is 2 chars

    new_name = '{}-{}{}'.format(f_num, f_title, f_ext) # Formatting the print to name the file how I need

    os.rename(f, new_name)