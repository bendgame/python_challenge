import pandas as pd
# Make a reference to the books.csv file path
csvfile = r'C:\Users\bendgame\Desktop\Homework3\python_challenge\PyPoll\election_data.csv'


# Import the books.csv file as a DataFrame
elec_data = pd.read_csv(csvfile)

df_ed = pd.DataFrame(elec_data)

df_ed.head()

percc = []
candidates = list(df_ed["Candidate"].unique())
print(candidates)

counts = list(df_ed['Candidate'].value_counts())
print(counts)

perc = sum(counts)
#print(perc)

x = 0
for candidate in candidates:
    zz = round(counts[x]/perc,3)
    percc.append(zz)
    x+=1
    
print(percc)

data = list(zip(candidates, percc, counts))
print(data[1])

#percc = perc/counts
#print(percc)
#for count in counts

print("Election Results")
print(" -------------------------")
print(f"Total Votes: {perc}")
print("-------------------------")
print(f"{data}")
#print(f"Correy: {correy_percent} ({len(correy)})")
#print(f"Li: {li_percent} ({len(li)}) ")
#print(f"O'Tooley: {otool_percent} ({len(otool)})")
#print(f" -------------------------")
#print(f"Winner: {winner}")
print(f"-------------------------")
    