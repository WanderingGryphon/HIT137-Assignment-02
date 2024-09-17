import csv
import os
from collections import Counter
import spacy
from tqdm import tqdm


# Input file and output file path
input_file = 'csv_text.txt'
output_file = 'spacy_output.csv'

# Check if the input file exists
if not os.path.isfile(input_file):
    print(f"Error: The file '{input_file}' does not exist.")

# Check if the output file exists; create one if not
output_dir = os.path.dirname(output_file)
if output_dir and not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load the appropriate model and set the max length for process
model = spacy.load('en_ner_bc5cdr_md')
model.max_length = 1500000

# Set disease and drug counter
disease_counts = Counter()
drug_counts = Counter()

# Read the text from the input file
with open(input_file, 'r', encoding='utf-8') as f:
    text = f.read()

    # Split the text into chunks for processing
    chunk_size = 1500000    # Set chunk size equal to max length of the model
    text_chunks = [text[i: i + chunk_size] for i in range(0, len(text), chunk_size)]

    print(f"Total number of chunks: {len(text_chunks)}")

    for chunk in tqdm(text_chunks, desc='Processing Chunks', unit='chunk'):
        ner_output = model(chunk)

        # Extract tokens and their entity types from the NER output
        tokens_entities = [(token.text, token.ent_type_) for token in ner_output]

        # Separate diseases and drugs
        disease = [token[0] for token in tokens_entities if token[1] == 'DISEASE']
        drug = [token[0] for token in tokens_entities if token[1] == 'CHEMICAL']

        # Update counters
        disease_counts.update(disease)
        drug_counts.update(drug)

# Write output
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Entity Type', 'Word', 'Count'])

    # Write disease outputs
    for word, count in disease_counts.most_common():
        writer.writerow(['Disease', word, count])

    # Write drug outputs
    for word, count in drug_counts.most_common():
        writer.writerow(['Drug', word, count])

print(f"Spacy output saved to {output_file}")
