# project starts here
#modules

#creates file paths along operating systems
import os
#module for reading csv files
import csv

# # Set path for file
election_data = os.path.join('//Users//danieltaylor//Desktop//python-challenge//**PyPoll**//election_data.csv')
output_path = ('//Users//danieltaylor//Desktop//python-challenge//**PyPoll**//output_2.txt')

#read file
#open the CSV

#lists to store data


#creates the dictionary for storing name and vote count
poll = {}

#creates the total votes variable and sets it to zero (0)
totalvotes = 0

#gets the election data file
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skips the header
    next(csvreader, None)

    #creates a dictionary using the candidate's last name as a key
    #counts each candidates' votes separately
    #creates a tally by looping


 #   next(csvreader,none)
    for row in csvreader:
        totalvotes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1



candidates = []
num_votes = []

for key, value in poll.items():
        candidates.append(key)
        num_votes.append(value)

vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/totalvotes*100,2))

new_totalvotes=float(totalvotes)

clean_data = list(zip(candidates, num_votes, vote_percent))

winner_list= []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

winner = winner_list[0]

if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + " , " + winner_list[w]

output_file = os.path.join('//Users//danieltaylor//Desktop//python-challenge//**PyPoll**//output_2.txt')

with open(output_file, 'w') as txtfile:
#    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(num_votes)  + 
#    '\n-------------------------\n')
    txtfile.writelines('Election Results  \n-------------------------\nTotal Votes: ' + str(new_totalvotes) +
    '\n-------------------------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints file to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())

