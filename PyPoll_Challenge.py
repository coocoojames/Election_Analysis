# Get voter turnout for each county
# Get percentage of votes from each county out of total votes
# Get county with the highest turnout
import os
import csv
file_to_open = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("Analysis","election_results.txt")
candidates = []
counties = []
candidate_votes = {}
county_turnouts_dict = {}
total_votes = 0
with open(file_to_open,'r') as election_data:
    election_results = csv.reader(election_data)
    next(election_results)
    for row in election_results:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        county_name = row[1]
        if county_name not in counties:
            counties.append(county_name)
            county_turnouts_dict[county_name] = 0
        county_turnouts_dict[county_name] += 1
# Ignore: personal testing
    # for i in range(len(counties)):
    #     county_turnouts_dict["Counties"[counties[i]]] = counties[i]

winning_candidate = ""
winning_vote_count = 0
winning_percentage = 0
largest_county_turnout = ""
largest_percentage = 0
with open(file_to_save,'w') as election_results:
    election_results.write(f'Election Results\n'
                                f'---------------------------------\n'
                                f'Total Votes: {total_votes:,}\n'
                                f'---------------------------------\n\n'
                                f'County Votes:\n')
    for county_name in county_turnouts_dict:
            turnout = county_turnouts_dict[county_name]
            turnout_percentage = turnout/total_votes*100
            print(f'{county_name} county has {turnout:,} votes which is {turnout_percentage:.1f}%')
            election_results.write(f'{county_name} county: {turnout_percentage:.1f}% ({turnout:,})\n')
            if turnout_percentage > largest_percentage:
                largest_percentage = turnout_percentage
                largest_county_turnout = county_name
    print("\nLargest County Turnout: "+largest_county_turnout)
    election_results.write(f'\n---------------------------------\n'
                            f'Largest County Turnout: {largest_county_turnout}\n'
                            f'---------------------------------\n')
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes)*100
        candidate_results = (f'Candidate: {candidate_name}: '
                                f'{vote_percentage:.1f}% '
                                f'({candidate_votes[candidate_name]:,})\n')
        print(candidate_results)
        election_results.write(candidate_results)
        if votes > winning_vote_count:
            winning_vote_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (f'---------------------------------\n'
                                f'Winner: {winning_candidate}\n'
                                f'Winning Vote Count: {winning_vote_count:,}\n'
                                f'Winning Percentage: {winning_percentage:.1f}%\n'
                                f'---------------------------------\n')
    print(winning_candidate_summary)
    election_results.write(winning_candidate_summary)