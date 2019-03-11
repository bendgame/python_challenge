# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------


# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.


import csv
import os

#file.os.path.join('..', 'election_data.csv')

file = r'C:\Users\bendgame\Desktop\Homework3\python_challenge\PyPoll\election_data.csv'


voterID = []
county = []
candidate = []


with open (file, newline ="") as csvfile:

    readcsv = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvfile)
    print(f"header: {csv_header}")
    
    for row in readcsv:
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        
    
    #print(voterID[:5])
    #print(county[:5])
    #print(candidate[:5])
    

print("Election Results")
print(" -------------------------")
print(f"Total Votes: ")
print("-------------------------")
print(f"Khan: ")
print(f"Correy: ")
print(f" Li: ")
print(f" O'Tooley: ")
print(f" -------------------------")
print(f"-------------------------")







