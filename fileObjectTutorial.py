# File Objects Tutorial

# # Not usually the way to open a file as you have explicitly close it.
# f = open('test.txt', 'r') # If file is in the same directory, if not specify entire path.
# # second argument, r is for reading, w is writing, a is for appending, r+ is for read and write.

# print(f.name) # Print the name of the file
# print(f.mode) # Mode in which the file was opened, for this example, it is r

# f.close() # When you have a file open, you HAVE to explicitly CLOSE it.

# Most if not for all cases, the above method is not used, the following context method is suggested to be used.
# CONTEXT METHOD TO OPEN A FILE

# with open('test.txt', 'r') as f: # The file is opened within this with block and when the control exits this
                                 # exits this with block, the file is closed.
    # f_contents = f.read() # Read all the contents of the file.
    # f_contents = f.readlines() # Read all the contents of the file as a list with every index item ending in a line break.
    # f_contents = f.readline() #Reads one line at a time when the readline is used the next time in the same code.
# # Instead of reading each line one by one, we can use a for loop to get all of them, like this.
#     for line in f:
#         print(line, end='') # The last end='' is to remove spaces between prints in the output.
                            # Also this method occupies less memory as one line is fetched at one time and only one line occupies memory at any given point of time.
    # f_contents = f.read(100) # Number of characters to print. Can be used concurrently to print all of the file.
    # Same as above, but with loop
    # size_to_read = 10
    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')
    
    # f.seek(0) # Set the control back to the beginning. Position can be changed within the parenthesis

    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')

    # print(f.tell()) # f.tell shows the character number that the control is at.

    # while len(f_contents) > 0:
    #     print(f_contents, end='')
    #     f_contents = f.read(size_to_read)

    # print(f_contents)

    # f.write('Test') # Write within with open read control will not work as the file is open.

# WRITING TO A FILE
# with open('test2.txt', 'w') as f: # If the file does not exist, this write will create one. If not, it will overwrite an existing one.
    # pass #you can use this to not do anything with the opened file.
    # f.write('Test') #Write to the file that is open.
    # f.seek(0) # Will put control back to the beginning so that the next write command overwrites the one above, but if the next write is lower in character than the above, only the new characters will change and the other characters from the above one will remain.
    # f.write('R') #Similar to read, this will continue to write at the position where the control was left on the last write.

# Use read and write to do copy test.txt to a new file test_copy.txt
# with open('test.txt', 'r') as rf: # Open the test.txt in read mode.
#     with open('test_copy.txt', 'w') as wf: # Open/Create a new test_copy.txt in write mode
#         for line in rf: # For each line in the read file
#             wf.write(line) # write that line into the write file

# Use read and write to copy test_pic.jpg to a new file
# same thing as above will not work as the picture file is not in binary.
with open('test_pic.jpg', 'rb') as rf: # Use the read binary mode
    with open('test_pic_copy.jpg', 'wb') as wf: # Use the write binary mode
        # for line in rf:
        #     wf.write(line)
# Do the same as above but with chunks
        chunk_size = 4096 # Define chunk size in bytes
        rf_chunk = rf.read(chunk_size) # Assign the read file chunk to the current chunk size
        while len(rf_chunk) > 0: # Create a while loop read the read file until the chunk length becomes 0
            wf.write(rf_chunk) # Write the current chunk to the write file
            rf_chunk = rf.read(chunk_size) #Assign the current chunk control to the rf_chunk variable to stop an infinite loop
        
