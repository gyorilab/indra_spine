import os
import xml.etree.ElementTree as ET
import csv

os.chdir('/Users/sangeethavempati/Documents/corpora/ApplicationEvaluation-Supplement')

tree = ET.parse("WhiteTextNegFixFull.xml")
root = tree.getroot()

sentences_with_true_interaction = []
data = []

interaction_true = False
for sentence in root.findall(".//sentence"):
    for pair in sentence.findall("pair"):
        if pair.get("interaction") == "True":
            #get sentence and add to set of sentences that contain at least one true interaction
            sentence_text = sentence.get("text")
            sentences_with_true_interaction.append([sentence_text])

            interaction_true = True
            current_data = {}
            e1 = pair.get("e1")
            e2 = pair.get("e2")
            for entity in sentence.findall("entity"):
                if entity.get("id") == e1:
                    #print(entity.get("text"))
                    #with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
                    #add e1 to e1 column
                    current_data["e1"] = entity.get("text")
                elif entity.get("id") == e2:
                    #print(entity.get("text"))
                    current_data["e2"] = entity.get("text")
                    current_data["text"] = sentence.get("text")
                    #with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
                    #add e2 to e2 column
                    #add sentence text to column
            data += [current_data]

print(data)

headers = ["e1","e2","text"]

csv_file_path = "true_manual_interactions2.csv"
'''
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(headers)

for dict in data:
    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
        csv_writer = csv.DictWriter(file, fieldnames=["e1", "e2", "sentence"])
        csv_writer.writerows(data)
'''

# Open the file once for writing
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    # Create a DictWriter with the correct fieldnames
    csv_writer = csv.DictWriter(file, fieldnames=headers)

    # Write the headers to the CSV file
    csv_writer.writeheader()

    # Write the data rows
    # Ensure the dictionary keys match the headers
    for row in data:
        csv_writer.writerow({
            "e1": row["e1"],
            "e2": row["e2"],
            "text": row.get("text", "")  # Using .get() to prevent KeyError
        })




'''
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    line_count = sum(1 for line in file)

print(line_count)
'''
#print(f"counter: {counter}")
'''
interaction_true = any(
    pair.get("interaction") == "True"
    for pair in sentence.findall("pair")
)
    
'''
'''
if interaction_true:
    # Get the text of the sentence
    sentence_text = sentence.get("text")
    # Add the sentence to the list
    sentences_with_true_interaction.append([sentence_text])

txt_path = "sentences4.txt"
with open(txt_path, 'w') as file:
    for string in sentences_with_true_interaction:
        file.write(str(string) + "\n")
'''
