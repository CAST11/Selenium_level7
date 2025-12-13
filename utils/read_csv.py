import csv


def get_csv_data(file_path):
    data = []
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header
        for row in reader:
            data.append(row)
    return data