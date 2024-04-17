import csv

# Specify the path to your CSV file
csv_file_path = "testbank.csv"

# Open the CSV file
with open(csv_file_path) as file:
    # Create a DictReader object, specifying the delimiter if needed
    csv_reader = csv.DictReader(file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Access data using column headers
        print(row['Question text'], row['Option A'], row['Option B'], row['Option C'], row['Correct Answer'] )  # Replace 'header1', 'header2', 'header3' with your actual column names
