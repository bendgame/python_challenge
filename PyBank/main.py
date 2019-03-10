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
        
    #average = sum(net_total)/len(months)
    
    month_count = len(months)
    x = 1
    y = 0
    average_change = (net_total[1]-net_total[0])
    changes = []

    for month in range(month_count-1):
        average_change = (net_total[x] - net_total[y])
        changes.append(int(average_change))
        x+=1
        y+=1
        #print(x , y)
        
    av_mon_chng = round(sum(changes)/(month_count -1),2)

    min_change = min(changes)
    max_change = max(changes)

    chng_i_min = changes.index(min_change)
    chng_i_max = changes.index(max_change)
    
    min_chng_month = months[chng_i_min + 1]
    max_chng_month = months[chng_i_max + 1]
  

#    print(min(changes))
#    print(max(changes))
#print(chng_i_min)
#print(chng_i_max)
#print(min_month)
#print(max_month)

print("Financial Analysis")
print("----------------------------")
print(f"Months: {len(months)}")
print(f"Total: ${sum(net_total)}")
#print(f"Average Change for Profit/Loss: {average}")
print(f"Average Monthly Change: {av_mon_chng}")
print(f"Greatest Increase in Profits: {max_chng_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_chng_month} (${min_change})")
