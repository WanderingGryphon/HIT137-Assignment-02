import pandas as pd
import os

# List of CSV file names and their text columns
csv_files = [('CSV1.csv', 'SHORT-TEXT'), ('CSV2.csv', 'TEXT'), ('CSV3.csv', 'TEXT'), ('CSV4.csv', 'TEXT')]

# Output text file to store extracted text
output_file = 'csv_text.txt'

with open(output_file, 'w', encoding='utf-8') as f:
    # Read each CSV file and extract text information
    for (file, text_column) in csv_files:
        # Check if file exists
        if os.path.exists(file):
            try:
                # Read CSV file into a DataFrame
                df = pd.read_csv(file, usecols=[text_column])

                # Check if the associated text column exists
                if text_column in df.columns:
                    # Iterate over each row and write the text to the output file
                    for text in df[text_column].dropna():  # Skip NaN values
                        f.write(str(text) + '\n')
                else:
                    print(f"Column {text_column} not found in {file}")
            except Exception as e:
                print(f"Error reading {file}: {e}")
        else:
            print(f"File not found: {file}")

# After processing all CSV files, this message confirms that the process is done
print(f"All text extracted to {output_file}")
