import csv
from datetime import datetime

# Input and output file paths
input_file = './tester.txt'
output_file1 = '../output_columns/date.csv'
output_file2 = '../output_columns/energy_production.csv'

# Read the input file
with open(input_file, 'r') as infile:
    lines = infile.readlines()

# Prepare data for output files
dates = []
values = []

for line in lines:
    date_str, value = line.strip().split(';')
    date_obj = datetime.strptime(date_str, '%d/%m/%Y')
    formatted_date = date_obj.strftime('%Y-%m-%d')
    dates.append([formatted_date])
    values.append([value])

# Write dates to the first output file
with open(output_file1, 'w', newline='') as outfile1:
    writer = csv.writer(outfile1)
    writer.writerow(['date'])
    writer.writerows(dates)

# Write values to the second output file
with open(output_file2, 'w', newline='') as outfile2:
    writer = csv.writer(outfile2)
    writer.writerow(['energy_production'])
    writer.writerows(values)



