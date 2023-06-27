import csv

def calculate_average_from_csv(csv_file, column_name):
    total = 0
    count = 0

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if column_name in row:
                try:
                    value = float(row[column_name])
                    total += value
                    count += 1
                except ValueError:
                    pass

    if count > 0:
        average = total / count
        return average
    else:
        return None

def analyze_csv():
    print("Welcome to DataMetrics Data Analytics!")
    print("Please enter the path or name of the CSV file:")

    csv_file = input()

    print("Please enter the name of the column to calculate the average:")

    column_name = input()

    average = calculate_average_from_csv(csv_file, column_name)

    if average is not None:
        print(f"Thank you for providing the CSV file.")
        print(f"The average value of the '{column_name}' column is: ${average:.2f}")
    else:
        print(f"Unable to calculate the average. Please make sure the CSV file and column name are valid.")

analyze_csv()
