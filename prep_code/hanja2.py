# Use python hanja library to extract eum
import json
import hanja

# Load the JSON data from the file
with open('hanja.json', 'r', encoding='utf-8') as file:
    hanja_data = json.load(file)

# Function to get Korean pronunciation for a given Hanja character
def get_korean_pronunciation(hanja_char):
    # Use the hanja library to get the pronunciation
    return hanja.translate(hanja_char, 'substitution')

# Update the "음" for each Hanja entry in the data
for entry in hanja_data:
    hanja_char = entry['hanja']
    entry['음'] = get_korean_pronunciation(hanja_char)

# Save the updated data back to the JSON file
with open('hanja.json', 'w', encoding='utf-8') as file:
    json.dump(hanja_data, file, ensure_ascii=False, indent=4)

print("Updated '음' in hanja.json")

# Function to check if "음" is non-null for all entries
def check_non_null_um(hanja_data):
    for entry in hanja_data:
        if not entry['음']:  # Checks if "음" is None or an empty string
            return False
    return True

# Check and print the result
all_non_null = check_non_null_um(hanja_data)
if all_non_null:
    print("All entries have a non-null '음' field.")
else:
    print("Some entries have a null or empty '음' field.")