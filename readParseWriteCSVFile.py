# Read Parse and Write CSV Files
import csv # Imports for CSV modules

# with open('names.csv', 'r') as csv_file: # Open the CSV file as any file
#     csv_reader = csv.reader(csv_file) # Read through the CSV file

#     # next(csv_reader) #Next iteration skips over the first line or the line where the control is at.
#                      #This is used here to skip over the header line

#     with open('new_names.csv', 'w') as new_file: # Create new file and open to write to
#         # csv_writer = csv.writer(new_file, delimiter='-') #Copy the CSV file into a new file by changing delimiter from comma to dash
#         csv_writer = csv.writer(new_file, delimiter='\t') #Copy the CSV file into a new file by changing delimiter from comma to tab
        

#         for line in csv_reader: #Write each line to the new file
#             csv_writer.writerow(line)
#             # print(line) #Iterate through the CSV file and print each line
#             # print(line[2]) #If you only want to print one particular field [Index]

# # Similar to write with new delimiter, you can read with a new delimiter too, however if you try to
# # read the file without any delimiter, all the separate fields will show as one field as the command is 
# # expecting a comma instead of the tab like this example below
# with open('new_names.csv', 'r') as csv_file: # Open the CSV file as any file
#     csv_reader = csv.reader(csv_file) # Read through the CSV file

#     for line in csv_reader:
#         print(line)

# # Read the file like this with the new delimiter specified to read it correctly
# with open('new_names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t')

#     for line in csv_reader:
#         print(line)

# USING DICTIONARY READER instead of READER and DICTIONARY WRITER instead of WRITER
with open('names.csv', 'r') as csv_file: # Open the CSV file as any file
    csv_reader = csv.DictReader(csv_file) # Read through the CSV file using Dictionary Reader
# # Dictionary ready displays/writes the values in Key Value pair instead of header and rows model
#     with open('names_dictreader.csv', 'w') as new_file:
#         fieldNames = ['first_name', 'last_name', 'email'] # Dictionary writer will need the fields to be defined
#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldNames)
#         csv_writer.writeheader() #Explicitly specify if you want the header to be included

#         for line in csv_reader:
#             csv_writer.writerow(line)
# IF you want to REMOVE the email field from the copy to the new file, you can do this.
# Dictionary ready displays/writes the values in Key Value pair instead of header and rows model
    with open('names_dictreader.csv', 'w') as new_file:
        fieldNames = ['first_name', 'last_name'] # REMOVE the email from the field names list
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldNames)
        csv_writer.writeheader() #Explicitly specify if you want the header to be included

        for line in csv_reader:
            del line['email'] # DELETE the field name 'email' for each write before appending file
            csv_writer.writerow(line)
