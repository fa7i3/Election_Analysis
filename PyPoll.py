# Add our dependencies.
import csv
import os

# Assign a vriable for the file to load and the path.
file_to_load = (r"c:\Users\akemu\Election_Analysis\Election_Analysis\Resources\election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = (r"c:\Users\akemu\Election_Analysis\Election_Analysis\analysis\election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

# Read the file object with the reader fumction.
    file_reader = csv.reader(election_data)
    #Print the header row.
    headers = next(file_reader)
    print(headers)
