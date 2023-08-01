import csv

def read_csv_file(filename, num_rows):
    try:
        with open(filename, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            header = next(csvreader)  # Read the header row

            # Display the data
            print("Header:", header)
            row_count = 0
            for row in csvreader:
                print(row)
                row_count += 1
                if row_count >= num_rows:
                    break
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    filename = "D:/dataset/Friday-02-03-2018_TrafficForML_CICFlowMeter.csv"
    read_csv_file(filename, num_rows=10)
