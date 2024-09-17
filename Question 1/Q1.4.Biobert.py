import csv
import os
from collections import Counter
from tqdm import tqdm
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline


def combine_entities(ner_output):
    entities = []
    current_entity = ''
    current_label = None

    for output in ner_output:
        word = output['word']
        label = output['entity']

        # Handle incomplete tokens
        if word.startswith('##'):
            current_entity += word[2:]
        else:
            if current_entity and current_label:  # Prevent appending empty entities
                entities.append((current_entity, current_label))
            current_entity = word
            current_label = label

    # Append the last entity if any
    if current_entity and current_label:
        entities.append((current_entity, current_label))

    return entities or None  # Return None if no entities found


# Input file and output file path
input_file = 'csv_text.txt'
output_file = 'biobert_output.csv'

# Check if the input file exists
if not os.path.isfile(input_file):
    print(f"Error: The file '{input_file}' does not exist.")

# Check if the output file exists; create one if not
output_dir = os.path.dirname(output_file)
if output_dir and not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load the tokenizer, model and pipeline
tokenizer = AutoTokenizer.from_pretrained('judithrosell/BioBERT_BC5CDR_NER_new')
model = AutoModelForTokenClassification.from_pretrained('judithrosell/BioBERT_BC5CDR_NER_new')
ner_pipeline = pipeline('ner', model=model, tokenizer=tokenizer, batch_size=8)

# Set disease and drug counter
disease_counts = Counter()
drug_counts = Counter()

# Read the text from the input file
with open(input_file, 'r', encoding='utf-8') as f:
    text = f.read()

    # Split the text into chunks of size 512 (max size for biobert) for processing
    chunk_size = 512
    text_chunk = [text[i: i + chunk_size] for i in range(0, len(text), chunk_size)]

    # Initiating
    for chunk in tqdm(text_chunk, desc='Processing Chunks', unit='chunk'):
        # Process the chunk with ner pipeline
        ner_output = ner_pipeline(chunk)

        # Combine incomplete tokens into full entities
        combined_entities = combine_entities(ner_output)

        if combined_entities is None:
            continue  # Skip if there are no entities

        # Filter entities based on labels
        disease = [entity[0] for entity in combined_entities if 'Disease' in entity[1]]
        drug = [entity[0] for entity in combined_entities if 'Chemical' in entity[1]]

        # Update counters
        disease_counts.update(disease)
        drug_counts.update(drug)

# Write output
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Entity', 'Word', 'Count'])

    # Write disease outputs
    for word, count in disease_counts.most_common():
        writer.writerow(['Disease', word, count])

    # Write drug outputs
    for word, count in drug_counts.most_common():
        writer.writerow(['Drug', word, count])

print(f"Biobert output saved to {output_file}")
