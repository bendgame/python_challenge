#Eric Kleppen

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

#file = r'C:\Users\bendgame\Desktop\Homework3\python_challenge\PyBank\PyBank_data.csv'

#fetch the file
file = os.path.join ('..', 'PyBank','PyBank_data.csv')

#create placeholder lists for the data
months = []
net_total = []

with open (file, newline = "") as csvfile:

    readcsv = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvfile)
    #print(f"header: {csv_header}")

    #put the data into lists
    for row in readcsv:
        months.append(row[0])
        net_total.append(int(row[1]))
        
   
    #count the number of months
    month_count = len(months)
    
    #set variables for loops
    x = 1
    y = 0
    
    #average change place holder
    average_change = (net_total[1]-net_total[0])
    
    #place holder list for changes 
    changes = []
    
    #for loop to calculate month to month change and dump the values into a list
    for month in range(month_count-1):
        average_change = (net_total[x] - net_total[y])
        changes.append(int(average_change))
        x+=1
        y+=1
        #print(x , y)
    
    #Calcuate the average monthly change and round it    
    av_mon_chng = round(sum(changes)/(month_count -1),2)

    #find the min and max change
    min_change = min(changes)
    max_change = max(changes)

    #return the index to find the positions in the list
    chng_i_min = changes.index(min_change)
    chng_i_max = changes.index(max_change)
    
    #find the months for the min and max changes
    min_chng_month = months[chng_i_min + 1]
    max_chng_month = months[chng_i_max + 1]
  

#Print the values in console

print("Financial Analysis")
print("----------------------------")
print(f"Months: {len(months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Monthly Change: {av_mon_chng}")
print(f"Greatest Increase in Profits: {max_chng_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_chng_month} (${min_change})")

#Write the output to a text file
fin_analysis = open("Financial_Analysis.txt","w")

fin_analysis.write("Financial Analysis\n")
fin_analysis.write("----------------------------\n")
fin_analysis.write(f"Months: {len(months)}\n")
fin_analysis.write(f"Total: ${sum(net_total)}\n")
fin_analysis.write(f"Average Monthly Change: {av_mon_chng}\n")
fin_analysis.write(f"Greatest Increase in Profits: {max_chng_month} (${max_change})\n")
fin_analysis.write(f"Greatest Decrease in Profits: {min_chng_month} (${min_change})\n")

 
fin_analysis.close() 
