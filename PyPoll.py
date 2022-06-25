#The data we need to retrieve
#1. Total # of votes cast
#2. Complete list of candidates who recieved votes
#3. % of votes each candidate won
#4. Total # of votes each candidate won
#5. Winner of the election

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
     # Print the header row.
    headers = next(file_reader)
    print(headers)

