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
candidates = []
khan = []
correy = []
li = []
otool = []

unique_candidates = list(set(candidates))

x = 0
y = 0
z = 0

with open (file, newline ="") as csvfile:

    readcsv = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvfile)
    print(f"header: {csv_header}")
     
    for row in readcsv:
        voterID.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
   
    total_votes = len(voterID)        
    
    
    for candidate in candidates:
        if (candidates[x] == "Khan"):
            khan.append(1)
        x+=1
    
    x=0
   
    for candidate in candidates:
        if (candidates[x] == "Correy"):
            correy.append(1)
        x+=1
    x=0
   
    for candidate in candidates:
        if (candidates[x] == "Li"):
            li.append(1)
        x+=1
    x=0        
    
    for candidate in candidates:
        if (candidates[x] == "O'Tooley"):
            otool.append(1)
        x+=1
            
            
            
    unique_candidates = list(set(candidates))
   
    khan_votes = khan/
'''  
    print(unique_candidates)    
    
    print(len(khan))
print(len(correy))
print(len(li))
print(len(otool))
    
    #print(total_votes)
    
    #print(voterID[:5])
    #print(county[:5])
print(candidates[:5])
'''    

print("Election Results")
print(" -------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: ")
print(f"Correy: ")
print(f" Li: ")
print(f" O'Tooley: ")
print(f" -------------------------")
print(f"-------------------------")