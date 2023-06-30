import csv

def calculate_average(csv_file, column_name):
    """
    Calculates the average of a specific column in a CSV file.

    Args:
        csv_file (str): The path or name of the CSV file.
        column_name (str): The name of the column to calculate the average for.

    Returns:
        float: The average value of the specified column.
    """
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        column_values = [float(row[column_name]) for row in reader]

    # Calculate the average of the column values
    average = sum(column_values) / len(column_values)
    return average

def main():
    """
    Main function to run the DataMetrics data analytics program.
    """
    print("Welcome to DataMetrics Data Analytics!")
    csv_file = input("Please enter the path or name of the CSV file:\n")
    column_name = input("Please enter the name of the column to calculate the average for:\n")

    try:
        average = calculate_average(csv_file, column_name)
        print("\nThank you for providing the CSV file.")
        print(f"The average value of the '{column_name}' column is: ${average:.2f}")
    except FileNotFoundError:
        print("\nFile not found. Please check the path or name of the CSV file.")
    except KeyError:
        print(f"\n'{column_name}' column not found in the CSV file.")

# Run the program
if __name__ == '__main__':
    main()