#import the os module
import os

#import module for reading CSV files
import csv

#create path to ensure we are using the correct file 
csvpath = os.path.join('Resources', 'budget_data.csv')

#create lists to store data 
total_months = []
total_profit = []
profit_change_monthy = []

#open the path with the reader 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip the header
    header=next(csvreader)
    
    #make it read through all the rows
    for row in csvreader:
        #add total months - we are linking "total_months" to the first coloumn as that is where months are
        total_months.append(row[0])
        #add total profit - need to make it an integer not a string
        total_profit.append(int(row[1]))


    #go through all the profits to get the monthly change 
    for i in range(len(total_profit)-1):
        profit_change_monthy.append(total_profit[i+1]-total_profit[i])

#ensure indent it out of the tab of the "with" statement 

# use max and min built in fucntions to find which is the greatest increase in profits and which is the greatest decrease in profits
increase_value_max = max(profit_change_monthy)
decrease_value_max = min(profit_change_monthy)

#apppend the values to correct month 
max_increase_month = profit_change_monthy.index(max(profit_change_monthy)) + 1
max_decrease_month = profit_change_monthy.index(min(profit_change_monthy)) + 1


#print analysis to the terminal
print("Financial Analysis")
print("---------------------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total Profits: ${sum(total_profit)}")
print(f"Average Change:${round(sum(profit_change_monthy)/len(profit_change_monthy),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(increase_value_max))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(decrease_value_max))})")

#Export a text file with the results 

#specify the file to write to - looking to make a txt file in the analysis folder in the PyBank folder
analysis_path = os.path.join("Analysis", "Financial Analysis.txt")

#open the file using "write mode"
#the code \n gives me a new line so my code is not all in one line on the txt file 
with open(analysis_path, 'w') as csvfile:
   csvfile.write("Financial Analysis")
   csvfile.write("\n")
   csvfile.write("--------------------------")
   csvfile.write("\n")
   csvfile.write(f"Total Months: {len(total_months)}")
   csvfile.write("\n")
   csvfile.write(f"Total Profits: ${sum(total_profit)}")
   csvfile.write("\n")
   csvfile.write(f"Average Change:${round(sum(profit_change_monthy)/len(profit_change_monthy),2)}")
   csvfile.write("\n")
   csvfile.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(increase_value_max))})")
   csvfile.write("\n")
   csvfile.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(decrease_value_max))})")

