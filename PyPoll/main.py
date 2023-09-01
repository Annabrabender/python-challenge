#import the os module
import os

#import module for reading CSV files
import csv

#create path to ensure we are using the correct file 
csvpath = os.path.join('Resources', 'election_data.csv')

#create our variables for the number of votes for each candidate and the total (will need for percentage calculations later on) 
votes_total = 0
votes_stockham = 0
votes_degette = 0
votes_doane = 0

#think about what we are looking for 
    #the total number of votes cast
    #the list of candiates and their votes and percenatge 
    #the winner my popular vote (who has the most votes)

#open the path with the reader 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip the header
    header=next(csvreader)

    #start with the votes 
    #go through each row 
    for row in csvreader:
        votes_total +=1

        #we also want to store the candidates name alongside their vote 
        if row[2] == "Charles Casper Stockham":
            votes_stockham += 1
        elif row[2] == "Diana DeGette":
            votes_degette +=1
        elif row [2] == "Raymon Anthony Doane":
            votes_doane += 1

# to find the winner we are going to use both the names and the votes - we can make a dictionary 
candidates_votes = {'Charles Casper Stockham': votes_stockham,
                    'Diana DeGette': votes_degette,
                    'Raymon Anthony Doane': votes_doane}



#need to see who has the most votes 
winner = max(candidates_votes, key=candidates_votes.get)

#now need to calculate the percentage
stockham_percent = round((votes_stockham/votes_total)*100 ,3)
degette_percent = round((votes_degette/votes_total)*100 ,3)
doane_percent = round((votes_doane/votes_total)*100, 3)

#now we need to print our analysis 

print("Election Analysis")
print("---------------------------------------")
print(f"Total votes: {votes_total}")
print("---------------------------------------")
print(f"Charles Casper Stockham: {stockham_percent}% ({votes_stockham})")
print(f"Diana DeGette: {degette_percent}% ({votes_degette})")
print(f"Raymon Anthony Doane: {doane_percent}% ({votes_doane})")
print("---------------------------------------")
print(f"Winner: {winner}")
print("---------------------------------------")


#Export a text file with the results 

#specify the file to write to - looking to make a txt file in the analysis folder in the PyBank folder
analysis_path = os.path.join("Analysis", "Election Analysis.txt")

#open the file using "write mode"
#the code \n gives me a new line so my code is not all in one line on the txt file 
with open(analysis_path, 'w') as csvfile:
   csvfile.write("Election Analysis")
   csvfile.write("\n")
   csvfile.write("---------------------------------------")
   csvfile.write("\n")
   csvfile.write(f"Total votes: {votes_total}")
   csvfile.write("\n")
   csvfile.write("---------------------------------------")
   csvfile.write("\n")
   csvfile.write(f"Charles Casper Stockham: {stockham_percent}% ({votes_stockham})")
   csvfile.write("\n")
   csvfile.write(f"Diana DeGette: {degette_percent}% ({votes_degette})")
   csvfile.write("\n")
   csvfile.write(f"Raymon Anthony Doane: {doane_percent}% ({votes_doane})")
   csvfile.write("\n")
   csvfile.write("---------------------------------------")
   csvfile.write("\n")
   csvfile.write(f"Winner: {winner}")
   csvfile.write("\n")
   csvfile.write("---------------------------------------")
   csvfile.write("\n")