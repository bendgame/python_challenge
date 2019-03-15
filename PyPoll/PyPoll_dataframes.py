import pandas as pd
# Make a reference to the books.csv file path
csvfile = r'C:\Users\bendgame\Desktop\Homework3\python_challenge\PyPoll\election_data.csv'


# Import the books.csv file as a DataFrame
elec_data = pd.read_csv(csvfile)

df_ed = pd.DataFrame(elec_data)

df_ed.head()

percc = []
candidates = list(df_ed["Candidate"].unique())
#print(candidates)

counts = list(df_ed['Candidate'].value_counts())
#print(counts)

perc = sum(counts)
#print(perc)

x = 0
for candidate in candidates:
    zz = round(counts[x]/perc,3)
    zz="{:.3%}".format(zz)
    percc.append(zz)
    x+=1

#percc ="{:.3%}".format(percc)
#print(percc)

data = list(zip(candidates, percc, counts))
#print(data[1])

max_count = df_ed['Candidate'].value_counts()

winner_count = max_count.max()

df_data = pd.DataFrame(data)

winner = list(df_data.loc[df_data[2]== winner_count,0])

sorted_ed =df_data.columns =["Canidate |", "Percent of Votes |", "Vote Count"]

sorted_ed = df_data.sort_values("Vote Count", ascending = False )


#sorted_ed.head()


#df_data.head()

#print(f"{df_data}")


    
#print(winner)
#print(winner.max())

#percc = perc/counts
#print(percc)
#for count in counts

print("Election Results")
print(" -------------------------")
print(f"Total Votes: {perc}")
print("--------------------------")
print(f"{sorted_ed}")
print(f" -------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")