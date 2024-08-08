# Extract hun, english, english2 from resource.txt
# Example line: 佳=아름다울 가, good, auspicious; beautiful; delightful (8)
import json
import re

# Function to detect if a string contains Korean characters
def contains_korean(text):
    return bool(re.search(r'[\u3131-\uD79D]', text))

# Function to detect if a line should be ignored based on specific characters
def should_ignore_line(line):
    ignore_markers = ['俗字', '同字', '古字', '略字', '本字', '譌字']
    return any(marker in line for marker in ignore_markers)

# Function to parse a line from the resource.txt file
def parse_resource_line(line):
    if should_ignore_line(line):
        return None
    
    # Split by the '=' sign to separate the Hanja and the rest
    hanja_part, rest = line.split('=', 1)
    hanja = hanja_part.strip()

    # Split the rest by commas to separate hun and the rest
    parts = [part.strip() for part in rest.split(',')]

    # Initialize variables
    hun = None
    eum = None
    english = None
    english2 = None
    strokes = None

    # Extract hun and eum
    for part in parts:
        if contains_korean(part):
            hun_parts = part.split(' ')
            hun = ' '.join(hun_parts[:-1]).strip()  # "아름다울"
            eum = hun_parts[-1].strip()             # "가"
        else:
            break

    # Extract english and english2
    remaining_parts = []
    for part in parts:
        if not contains_korean(part):
            remaining_parts.append(part)
    
    if remaining_parts:
        english_part = remaining_parts[0]
        english_parts = re.split(r'[;,]', english_part, 1)
        english = english_parts[0].strip()
        if len(english_parts) > 1:
            english2 = english_parts[1].strip()

    # Handle case where english is 'surname'
    if english == 'surname' and english2:
        new_english1, *remaining_english2 = english2.split(';', 1)
        english = new_english1.strip()
        english2 = remaining_english2[0].strip() if remaining_english2 else None

    # Extract the number of strokes
    strokes_match = re.search(r'\((\d+)\)', line)
    strokes = int(strokes_match.group(1)) if strokes_match else None

    return hanja, hun, eum, english, english2, strokes


# Load the JSON data from the file
with open('hanja_copy.json', 'r', encoding='utf-8') as file:
    hanja_data = json.load(file)

# Create a mapping from Hanja to their data
hanja_dict = {entry['hanja']: entry for entry in hanja_data}

# Read and parse the resource.txt file
with open('resource.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # Skip empty lines or lines without '='
        if not line.strip() or '=' not in line:
            continue
        
        parsed_data = parse_resource_line(line)
        if parsed_data is None:
            continue

        hanja, hun, eum, english, english2, strokes = parsed_data

        if english:
            english = re.sub(r'\s*\(\d+\)$', '', english)
        if english2:
            english2 = re.sub(r'\s*\(\d+\)$', '', english2)

        # Update the corresponding entry in the hanja_data if the hanja exists
        if hanja in hanja_dict:
            if not hanja_dict[hanja]['훈']:
                hanja_dict[hanja]['훈'] = hun
            if hun and hanja_dict[hanja]['훈']:
                if (len(hanja_dict[hanja]['훈']) > len(hun)):
                    hanja_dict[hanja]['훈'] = hun
            if english:
                hanja_dict[hanja]['english'] = english
            if english2:
                hanja_dict[hanja]['english2'] = english2
            if strokes:
                hanja_dict[hanja]['strokes'] = strokes

# Convert the updated dictionary back to a list
updated_hanja_data = list(hanja_dict.values())

# Save the updated data back to the JSON file
with open('hanja.json', 'w', encoding='utf-8') as file:
    json.dump(updated_hanja_data, file, ensure_ascii=False, indent=4)

print("Updated '훈', '음', 'english', 'english2', and 'strokes' in hanja.json")


# Function to check if fields are non-null for all entries
def check_non_null_um(hanja_data):
    for entry in hanja_data:
        for field in ['훈', '음', 'english', 'strokes']:
            if not entry[field]:  # Checks if "음" is None or an empty string
                return False
    return True

# Check and print the result
all_non_null = check_non_null_um(hanja_data)
if all_non_null:
    print("All entries have a non-null field.")
else:
    print("Some entries (hun, english) have a null or empty field.")

# Function to check if fields are non-null for all entries
def check_non_null_um(hanja_data):
    for entry in hanja_data:
        for field in ['훈', '음']:
            if not entry[field]:  # Checks if "음" is None or an empty string
                return False
    return True

# Check and print the result
all_non_null = check_non_null_um(hanja_data)
if all_non_null:
    print("All entries have a non-null field.")
else:
    print("Some entries (hun) have a null or empty field.")
