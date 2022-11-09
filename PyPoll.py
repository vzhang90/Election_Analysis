#The data we need to retrieve.
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')
# Open the election results and read the file
with open(file_to_load, 'r') as election_data:
    # To do: perform analysis. Print the file object
    print(election_data)
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read and print the header row
    headers = next(file_reader)
    print(headers)
    # Print each row in the CSV file
    for row in file_reader:
        print(row)

#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join('analysis', 'election_analysis.txt')
#Using the open() function with the "w" mode to write data to the file
open(file_to_save, "w")
# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
    #write three counties to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")


# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

