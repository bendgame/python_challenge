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


with open (file, newline ="") as csvfile:

    readcsv = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvfile)
    #print(f"header: {csv_header}")
     
    for row in readcsv:
        voterID.append(row[0])
        #county.append(row[1])
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
            
#unique_candidates = list(set(candidates))
   
    khan_percent = round((len(khan)/total_votes),3)
    correy_percent = round((len(correy)/total_votes),3)
    li_percent = round((len(li)/total_votes),3)
    otool_percent = round((len(otool)/total_votes),3)



#winner_list = {"Khan":"khan_percent", "Correy":"correy_percent", "Li":"li_percent", "O'Tooley":"otool_percent"}

    winner_list = [khan_percent,correy_percent,li_percent,otool_percent]
    
    if winner_list[0] > winner_list[1] and winner_list[0] > winner_list[2] and winner_list[0] > winner_list[3]:
        winner = "Khan"
    if winner_list[1] > winner_list[2] and winner_list[1] > winner_list[3] and winner_list[1] > winner_list[0]:
        winner = "Correy"
    if winner_list[2] > winner_list[1] and winner_list[2] > winner_list[3] and winner_list[2] > winner_list[0]:
        winner = "Li"
    if winner_list[3] > winner_list[0] and winner_list[3] > winner_list[1] and winner_list[3] > winner_list[2]:
        winner = "O'Tooley"

'''
#winner = winner_list.max()
print(winner_list)
print(winner)
'''
'''
print(khan_percent)
print(correy_percent)
print(li_percent)
print(otool_percent)
'''
khan_percent = "{:.3%}".format(khan_percent)
correy_percent = "{:.3%}".format(correy_percent)
li_percent = "{:.3%}".format(li_percent)
otool_percent = "{:.3%}".format(otool_percent)
 

print("Election Results")
print(" -------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {khan_percent} ({len(khan)})")
print(f"Correy: {correy_percent} ({len(correy)})")
print(f"Li: {li_percent} ({len(li)}) ")
print(f"O'Tooley: {otool_percent} ({len(otool)})")
print(f" -------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")
