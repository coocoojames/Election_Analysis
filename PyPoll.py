print('Running the Script')
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
# file_to_open = os.path.join("Resources","election_results.csv")
# file_to_save = os.path.join("Analysis","candidate_results.txt")
# Open the file
total_votes = 0
candidates = []
candidate_votes = {}

file_to_open = r'C:\\Users\\Johns\Documents\Data Science Bootcamp\\Election_Analysis\\Resources\\election_results.csv'

with open(file_to_open,'r') as election_data:
    # Perform analysis
    # Close the file
    print(election_data)
    file_reader = csv.reader(election_data)
    # for row in file_reader:
    #     print(row)
    next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    print(total_votes)
    print(candidates)
    print(candidate_votes)

print(candidate_votes.keys())

print(candidate_votes['Diana DeGette'])

candidate_xyz = {}
candidate_sample = {'Percentage': {'Candidate_Name': '', 'Candidate_Score':''}}
print(candidate_sample['Percentage'].keys())

# candidate_sample['Percentage'] = '87.6'

print(candidate_sample)

candidate_sample['Percentage']['Candidate_Name'] = 'Steve'
candidate_sample['Percentage']['Candidate_Score'] = '88.8'

print(candidate_sample)
# with open(file_to_save,'w') as candidate_results_file:
#     candidate_results_file.write(f'Election Results\n'
#                                 f'-------------------\n'
#                                 f'Total Votes: {total_votes}\n'
#                                 f'-------------------\n')
#     winning_candidate = ""
#     winning_vote_count = 0
#     winning_percentage = 0
#     for candidate_name in candidate_votes:
#         votes = candidate_votes[candidate_name]
#         vote_percentage = float(votes)/float(total_votes)*100
#         candidate_votes["Percentage"]["Candidate"] = str(round(vote_percentage,1))
#         candidate_results = (f'{candidate_name}'
#                             f' has {candidate_votes[candidate_name]}'
#                             f' votes, which is {vote_percentage:.1f}% of the total votes.\n')
#         print(candidate_results)
#         candidate_results_file.write(candidate_results)
#         if votes > winning_vote_count:
#             winning_vote_count = votes
#             winning_percentage = vote_percentage
#             winning_candidate = candidate_name
#     candidate_results_file.write("---------------------------------\n")
#     winning_candidate_summary = (f'---------------------\n'
#                                 f'Winner: {winning_candidate}\n'
#                                 f'Winning Vote Count: {winning_vote_count:,}\n'
#                                 f'Winning Percentage: {winning_percentage:.1f}%\n'
#                                 f'----------------------\n')
#     print(winning_candidate_summary)
#     candidate_results_file.write(winning_candidate_summary)

