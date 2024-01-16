# Reading a file syntax:
with open("welcome.txt") as text_file:
    text_data = text_file.read()  # This reads the entire file and returns it as a string
print(text_data)
# 'with' creates a context manager, it creates a code block where the connection will be closed upon exiting the block

# To read line by line, iterating over them all:
with open("how_many_lines.txt") as lines_doc:
    for line in lines_doc.readlines():
        print(line)

# To read a single line:
with open("just_the_first.txt") as first_line_doc:
    first_line = first_line_doc.readline()
    print(first_line)
# You continue making calls to readline() to read subsequent lines
# When the file ends, subsequent calls will return ""

# To write a new file:
with open("bad_bands.txt", "w") as bad_bands_doc:
    bad_bands_doc.write("Imagine Dragons")
# Use "w" to go into write mode. The default assumed mode is "r" for read mode.
# If file "bad_bands.txt" already exists, it will be overwritten.

# To add a line to an existing file:
with open("cool_dogs.txt", "a") as cool_dogs_file:
    cool_dogs_file.write("Air Buddy\n")
# Use "a" for append mode. Use a \n to write on a new line. Every time you run the program while in
# append mode, the file will continue to write the line over and over again.

# Using "with" and indenting the block is an updated way of working with files.
# It is so that we don't have to manually .close() the file as we do in Java.
# Old way:
close_this_file = open('fun_file.txt')
setup = close_this_file.readline()
punchline = close_this_file.readline()
print(setup)
# New way
with open('fun_file.txt') as close_this_file:
    setup = close_this_file.readline()
    punchline = close_this_file.readline()
print(setup)

# CSV files:
with open("logger.csv") as log_csv_file:
    print(log_csv_file.read())

# Import the csv module to access tools for parsing csv files, like the DictReader tool.
import csv
list_of_email_addresses = []
with open('users.csv', newline='') as users_csv:
    user_reader = csv.DictReader(users_csv)
    for row in user_reader:
        list_of_email_addresses.append(row['Email'])

# A csv file might have a different delimiter instead of a comma. Use the delimiter parameter.
import csv
with open("books.csv", newline='') as books_csv:
  # ^You only need to add newline arg if using Reader as we are doing below
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = []
  for row in books_reader:
    isbn_list.append(row['ISBN'])  # <'ISBN' is the dictionary key
    # The dictionary key is the top row of the csv. The DictReader uses the top row to create dictionary keys that
    # match the rest of the data to them.

# Writing a csv file:
import csv
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

with open("logger.csv", "w") as logger_csv:
    log_writer = csv.DictWriter(logger_csv, fieldnames=fields)

    log_writer.writeheader()
    for item in access_log:
        log_writer.writerow(item)

# Reading a JSON file. It means JavaScript Object Notation. It is formatted similar to a Python dictionary.
# A JSON file
{
  'user': 'ellen_greg',
  'action': 'purchase',
  'item_id': '14781239',
}

import json
with open('purchase_14781239.json') as purchase_json:
  purchase_data = json.load(purchase_json)  # creates a dictionary from the file
print(purchase_data['user'])
# Prints 'ellen_greg'

# Writing a JSON file:
import json

data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]
with open("data.json", "w") as data_json:
  json.dump(data_payload, data_json)  # dump turns it into a json file

# Final file I/O project:
# Import necessary modules for working with CSV and JSON files
import csv
import json

# List to store the usernames of compromised users
compromised_users = []

# Open the file containing compromised data and read it
with open("passwords.csv") as password_file:
    # Use csv.DictReader to parse the CSV file
    password_csv = csv.DictReader(password_file)

    # Iterate over each row in the CSV file
    for password_row in password_csv:
        # Append the username from each row to the compromised_users list
        compromised_users.append(password_row["Username"])

# Open a new text file to write the usernames of compromised users
with open("compromised_users.txt", "w") as compromised_user_file:
    # Iterate over each username in the compromised_users list
    for compromised_user in compromised_users:
        # Write each username to the file, followed by a newline character
        compromised_user_file.write(compromised_user + "\n")

# Open a new JSON file to write a message for the boss
with open("boss_message.json", "w") as boss_message:
    # Dictionary to hold the message data
    boss_message_dict = {}
    # Setting recipient and message keys
    boss_message_dict["recipient"] = "The Boss"
    boss_message_dict["message"] = "Mission Success"
    # Write the dictionary to the JSON file
    json.dump(boss_message_dict, boss_message)

# Open a new CSV file to replace the old passwords file
with open("new_passwords.csv", "w") as new_passwords_obj:
    # Slash Null's signature as a multiline string
    slash_null_sig = """
    [MULTILINE STRING REMOVED FOR BREVITY]
    """
    # Split the signature into lines
    lines = slash_null_sig.split('\n')
    # Create a csv writer object
    writer = csv.writer(new_passwords_obj)
    # Iterate over each line in the signature
    for line in lines:
        # Write each line to the CSV file
        writer.writerow([line])
