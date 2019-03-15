import pandas as pd
import os

# Make a reference to the csv file path
#csvfile = r'C:\Users\bendgame\Desktop\Homework3\python_challenge\PyPoll\election_data.csv'
csvfile = os.path.join ('..', 'PyPoll','election_data.csv')


# read the csv file as a DataFrame
elec_data = pd.read_csv(csvfile)

df_ed = pd.DataFrame(elec_data)

#df_ed.head()

#create an empty list to store vote counts as percent
percent_count = []

#Create a list of unique(distinct) candidates
candidates = list(df_ed["Candidate"].unique())
#print(candidates)

#count the number of times the candidate appears and put into a list
counts = list(df_ed['Candidate'].value_counts())
#print(counts)

#get the total vote count
total_votes = sum(counts)
#print(perc)

#set variable for for loop
x = 0

#for loop to calculate percentages
for candidate in candidates:
    percentage = round(counts[x]/total_votes,3)
    percentage="{:.3%}".format(percentage)
    percent_count.append(percentage)
    x+=1

#percent_count ="{:.3%}".format(percent_count)
#print(percent_count)

#create a zipped list of data to rebuild data frame
data = list(zip(candidates, percent_count, counts))
#print(data[1])

#calculate counts to find winner
max_count = df_ed['Candidate'].value_counts()

#find the most counts
winner_count = max_count.max()

#put the zipped data into a data frame
df_data = pd.DataFrame(data)

#calculate the winner and put it into a list
winner = list(df_data.loc[df_data[2]== winner_count,0])

#rename the columns for df_data
sorted_data =df_data.columns =["Canidate |", "Percent of Votes |", "Vote Count"]

#sort the columns by vote count in descending order
sorted_data = df_data.sort_values("Vote Count", ascending = False )


print("Election Results")
print(" -------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
print(f"{sorted_data}")
print(f" -------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

#Write the outcome data to a txt file named election_winner

election_winner = open("election_winner.txt","w")

election_winner.write("Election Results\n")
election_winner.write("----------------------------\n")
election_winner.write(f"Total Votes: {total_votes}\n")
election_winner.write(f"--------------------------\n")
election_winner.write(f"{sorted_data}\n")
election_winner.write(f" -------------------------\n")
election_winner.write(f"Winner: {winner}\n")
election_winner.write(f"-------------------------")

election_winner.close()