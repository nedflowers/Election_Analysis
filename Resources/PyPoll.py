# 1.Find total number of votes cast  
# 2.A complete list of candidates who received votes
# 3.Total number of votes each candidate received
# 4.Percentage of votes each candidate won
# 5.The winner of the election based on popular vote


#Add Dependencies
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    for row in file_reader:
    # Read and print the header row.
        headers = next(file_reader)
        print(row)


# Create a filename variable to a direct or indirect path to the file.

with open(file_to_save, "w") as txt_file:

    txt_file.write("Counties in the Election\n")
    txt_file.write("--------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")


