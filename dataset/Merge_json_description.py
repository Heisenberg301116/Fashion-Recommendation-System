import json

# List of JSON file names to merge
json_files = ['hat.json', 'outwear.json', 'pants.json', 'shirt.json', 'shoes.json', 'shorts.json', 'skirt.json', 't-shirt.json']

# Create an empty list to store the data from each file
merged_data = []

# Iterate through each JSON file and append its data to the merged_data list
for file_name in json_files:
    with open('Description/' + file_name, 'r') as file:
        data = json.load(file)
        merged_data.extend(data)

# Write the merged data to a new JSON file
with open('merged_data.json', 'w') as merged_file:
    json.dump(merged_data, merged_file, indent=4)

print("JSON files merged successfully.")