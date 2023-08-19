# CSV Field Consistency Checker, AKA ConsistentCSV

## Overview

ConsistentCSV is a Python script to validate that all records in a given CSV file contain the same number of fields. It uses the statistical mode of the first 5 records to determine the expected number of fields and checks the rest of the file for consistency.

## Installation

No special installation is required. Just clone this repository and run the script using Python.

## Usage

### Running the Script

You can run the script from the command line, passing the path to the CSV file you want to check as an argument:

```bash
python concsv.py yourfile.csv
```

The script will print messages to the console if it finds any records with a different number of fields from the expected, including the row numbers where the inconsistencies occur.

### Running Tests

The repository includes a set of unit tests to verify the functionality of the script. You can run the tests using:

```bash
python test_check_csv.py
```

## Requirements

- Python 3.x

## Contributing

If you would like to contribute to this project, please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License.
