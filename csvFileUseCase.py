#Use case for CSV file into HTML list

#Define imports
import csv

#Variable definitions
html_output = ''
names = []

# # Open file and read it with 'Reader' method
# with open('patrons.csv', 'r') as data_file:
#     csv_data = csv.reader(data_file)

# Open file and read it with 'DictReader' method
with open('patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    # Skip over the first two lines as the first one is header and the next line which is information only
    # next(csv_data) #Not required for 'DictReader' method as the header does not exist in this method
    next(csv_data) 

    #Print file line by line
    for line in csv_data:
        # if line[0] == 'No Reward': # Exit out of the loop when the control reaches the line with 'No Reward' as the names after that are not required
        if line['FirstName'] == 'No Reward': #Modification for DictReader to ignore after this first name
            break
        # print(line)
        # names.append(f"{line[0]} {line[1]}") #For each line, append the names list variable with index 0, space and index 1
        names.append(f"{line['FirstName']} {line['LastName']}") #Modification for DictReader

# for name in names: #Print out each name in the names list
#     print(name)
#Getting the HTML Output ready
html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '\n<ul>' #Appending html coding

for name in names:
    html_output += f'\n\t<li>{name}</li>' # Append each name form the list into html output

html_output += '\n</ul>' #Closing out html output
print(html_output) #Print html output
