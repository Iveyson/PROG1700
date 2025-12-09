import csv
def read_file(filename):
    with open(filename, "r") as f:
        write_file()   
def write_file():
    for line in f:
        records = []
        name, score = line.strip().split(",")
        records.append((name, float(score)))
        print(line.strip())
        print(records)