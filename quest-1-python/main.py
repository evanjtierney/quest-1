# Idea to use locale library came from: https://stackabuse.com/format-number-as-currency-string-in-python/
import csv
import locale


# Convert an int to a properly formatted dollar string
def to_dollar_string(amount):
    return locale.currency(amount, grouping=True)


# Setup locale with default settings
locale.setlocale(locale.LC_ALL, '')
dept_expenditures = {}

with open("city-of-seattle-2012-expenditures-dollars.csv") as file:
    csv_reader = csv.reader(file, delimiter=",")
    # Ignore first row (column headers)
    next(csv_reader)
    for row in csv_reader:
        # If this row has no expenditure value under 2012, ignore it
        if row[3] == '':
            continue
        dpt = row[0]
        expenditures = int(row[3])
        # Check if the dpt already exists as a key in the dict
        # If so, add on the current expenditure to the corresponding value
        # If not, create the entry with the initial value as the current expenditure
        if dpt in dept_expenditures:
            dept_expenditures[dpt] += expenditures
        else:
            dept_expenditures[dpt] = expenditures

for dpt, expenditures in dept_expenditures.items():
    print(dpt + ": " + to_dollar_string(expenditures))
