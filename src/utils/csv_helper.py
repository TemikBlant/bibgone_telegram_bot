import csv


def read_csv(file_name="ceva.csv"):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        list_csv = list(csv_reader)
    return list_csv
