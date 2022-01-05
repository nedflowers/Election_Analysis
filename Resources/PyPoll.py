# 1.Find total number of votes cast  
# 2.A complete list of candidates who received votes
# 3.Total number of votes each candidate received
# 4.Percentage of votes each candidate won
# 5.The winner of the election based on popular vote

#Add Dependencies
import csv
import os
#Assign variable to load file from program
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign variable to store save from program to path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1.Initialize accumulator to 0
total_votes = 0

#Declare new list
candidate_options = []

#Create dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open election results and load file. 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #Read and skip header
    headers = next(file_reader)

    #Print each row in CSV
    for row in file_reader:
        #Add 1 to total vote count
        total_votes += 1
        
        #Print Candidate name
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            #Add to list of candidates
            candidate_options.append(candidate_name)

            #Begin tracking votes per candidate
            candidate_votes[candidate_name] = 0

        #Add vote to candidate count
        candidate_votes[candidate_name] += 1

    #Determine the percentag eof votes per candidate
    for candidate_name in candidate_votes:
        #Retrieve vote count
        votes =  candidate_votes[candidate_name]
        #calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        #votes to terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #determine if votes are greater than winnning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #Set winning candidate to candiate name
            winning_candidate = candidate_name

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)    
