import datetime as dt
now = dt.datetime.now()
print("The date/time right now is",now)
import csv
import os
dir(csv)
# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who receieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Assign file to be opened
election_data = os.path.join("Resources","election_results.csv")
# Open the file
with open(election_data,'r') as election_data:
    # Perform analysis
    # Close the file
    print(election_data)
    file_reader = csv.reader(election_data)
    # for row in file_reader:
    #     print(row)
    headers = next(file_reader)
    print(headers)

file_to_save = os.path.join("Analysis","election_results.txt")
with open(file_to_save,'w') as analysis_file:
    analysis_file.write("Counties in the Election\n"
    f'----------------------\n')
    analysis_file.write("Arapahoe, Denver, Jefferson")
