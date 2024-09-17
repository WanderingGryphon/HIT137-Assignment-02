import os
import re
import csv
from transformers import AutoTokenizer
from collections import Counter
from tqdm import tqdm


def count_unique_tokens(input_file, output_file, model_name, top_n):
    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return

    # Ensure that the output directory exists
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load the tokenizer using fast implementation
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

    # Initialize a Counter to keep count of unique tokens
    token_count = Counter()

    # Regular expression for refining tokens
    token_pattern = re.compile(r"\b[a-z]+(?:-[a-z]+)?\b")

    # Process the text file in chunks to avoid excess memory usage
    chunk_size = 10 * 1024 * 1024  # 10 MB chunks

    # Open the input_file and set up the progress bar
    with open(input_file, 'r', encoding='utf-8') as f, tqdm(
            total=os.path.getsize(input_file), unit='B', unit_scale=True,
            desc='Processing') as pbar:
        # Read the file in chunks
        while True:
            text_chunk = f.read(chunk_size)
            if not text_chunk:
                break

            # Tokenize the current text chunk
            tokens = tokenizer.tokenize(text_chunk)

            # Refine tokens using the regular expression
            refined_tokens = []
            for token in tokens:
                refined_tokens.extend(re.findall(token_pattern, token.lower()))

            # Update the counter with the refined tokens
            token_count.update(refined_tokens)

            # Update the progress bar
            pbar.update(len(text_chunk.encode('utf-8')))

    # Get top_n most common tokens
    top_tokens = token_count.most_common(top_n)

    # Write the results in a csv file
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Token', 'Count'])
        writer.writerows(top_tokens)

    print(f"Top {top_n} tokens and their counts saved to {output_file}")


# Usage
count_unique_tokens('csv_text.txt', 'token_count.csv', 'bert-base-uncased', 30)
