# import CSV file
import os
import csv
pybank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Read in the CSV file
with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader, None)
    first_row = next(csvreader, None)
    prev_dollars = int(first_row[1])
    total_net = int(first_row[1])
    total_months = 1
    total_monthly_change = 0
    monthly_change_list = []
    monthly_change_dates = []

    for row in csvreader: 
        current_dollars = int(row[1])
        total_net += current_dollars
        total_months += 1
        monthly_change = current_dollars - prev_dollars
        monthly_change_list.append(monthly_change) 
        monthly_change_dates.append(row[0]) 
        total_monthly_change += monthly_change
        prev_dollars = int(row[1])

print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${total_monthly_change / total_months}")
print(f"Greatest Increase in Profits: {monthly_change_dates} (${max(monthly_change_list)})")
print(f"Greatest Decrease in Profits: {monthly_change_dates} (${min(monthly_change_list)})")
