import csv
import re
from collections import Counter


def extract_top_words(input_path, output_path, top_n):
    try:
        # Compile regex pattern once to avoid re-compiling it for every line
        # This matches any character that is not a letter (a-z, A-Z) or space
        pattern = re.compile(r'[^a-zA-Z\s]')

        # Initialize a Counter object to store word counts efficiently
        word_counts = Counter()

        # Process the text file line by line
        with open(input_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Preprocess the text (remove non-alphanumeric characters and convert to lowercase)
                line = pattern.sub('', line).lower()
                words = line.split()
                word_counts.update(words)  # Increment word counts

        # Get the top n words
        top_words = word_counts.most_common(top_n)

        # Write the top words to a CSV file
        with open(output_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Word', 'Count'])  # Header row
            csv_writer.writerows(top_words)  # Write all rows at once

        print(f'Top {top_n} words written to {output_path}')

    # Handle case where the input file is not found
    except FileNotFoundError:
        print(f'Error: The file {input_path} was not found.')

    # Handle any other IO-related errors (e.g., issues reading/writing files)
    except IOError as e:
        print(f'Error reading or writing to file: {e}')


# Using the function to extract the top 30 words
extract_top_words('csv_text.txt', 'top_30_words.csv', 30)
