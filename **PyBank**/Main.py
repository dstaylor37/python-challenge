## PyBank

""" ![Revenue](Images/revenue-per-lead.jpg)

* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
The dataset is composed of two columns: `Date` and `Profit/Losses`. 
(Thankfully, your company has rather lax standards for accounting so the records are simple.)

* Your task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* As an example, your analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results. """

#Project starts here
# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("//Users//danieltaylor//Desktop//python-challenge//", "**PyBank**", "budget_data.csv")

date = []
revenue = []
change = []
count_months = 0
sum = 0
total_change = 0
avg_revenue_change = 0
increase = 0
decrease = 0

# Open the CSV
with open(csvpath, newline="",encoding="UTF8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
    for row in csvreader:
        date.append(row[0])
        revenue.append(row[1])
        count_months += 1
        sum += int(row[1])
