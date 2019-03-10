#this is main.py in the pybank
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)


import csv
import os

file = r'C:\Users\bendgame\Desktop\Homework3\python_challenge\PyBank\PyBank_data.csv'

#file = os.path.join ('..', 'PyBank','PyBank_data.csv')

months = []
net_total = []

with open (file, newline = "") as csvfile:

    readcsv = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvfile)
    print(f"header: {csv_header}")

    for row in readcsv:
        months.append(row[0])
        net_total.append(int(row[1]))
        
average = sum(net_total)/len(months)

#print(months)
#print(net_total)

print("Financial Analysis")
print("----------------------------")
print(f"Months: {len(months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Change for Profit/Loss: {average}")
