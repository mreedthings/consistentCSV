import csv
import sys
from collections import Counter

def check_fields(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        field_counts = []
        row_number = 0

        for row in reader:
            row_number += 1
            field_counts.append(len(row))

            if row_number == 1:
                normal_number_of_fields = len(row)

            if row_number == 5:
                normal_number_of_fields = Counter(field_counts).most_common(1)[0][0]

            if row_number <= 5 and len(row) != normal_number_of_fields:
                print(f"Inconsistent number of fields at row {row_number}. Expected {normal_number_of_fields}, found {len(row)}.")

            if row_number > 5 and len(row) != normal_number_of_fields:
                print(f"Inconsistent number of fields at row {row_number}. Expected {normal_number_of_fields}, found {len(row)}.")
                return False

        return True

if len(sys.argv) != 2:
    print("Usage: python script.py <filename>")
else:
    filename = sys.argv[1]
    result = check_fields(filename)
    if result:
        print("All records contain the same number of fields.")
    else:
        print("Records have a varying number of fields.")
