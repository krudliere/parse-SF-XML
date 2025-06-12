import xml.etree.ElementTree as ET
import os
import csv

directory_path = "files"
output_file = "output.csv"

def parsePrint(filename):
    """
    Parses the XML file and prints the field items.
    
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    """

    tree = ET.parse(file_path)
    root = tree.getroot()

    print(f"Root tag: {root.tag}")  # Debug: Show root tag

    # Extract the namespace from the root element
    namespace = root.tag[root.tag.find("{")+1:root.tag.find("}")]
    print(f"Namespace: {namespace}")

    # Define the namespace
    ns = {'ns': namespace}
    
    filetype = "layout"

    if(filetype in filename):
        print(f"layout file: {filename}")
        # Find all field elements with namespace in layouts
        fieldItems = root.findall('.//ns:layoutSections/ns:layoutColumns/ns:layoutItems/ns:field', ns)
    else:
        # Find all fieldItem elements with namespace in flexipages
        fieldItems = root.findall('.//ns:flexiPageRegions/ns:itemInstances/ns:fieldInstance/ns:fieldItem', ns)

    data = []

    for fieldItem in fieldItems:
        print(fieldItem.text.replace("Record.", ""))  # Debug: Show each field item tag and attributes
        data.append([fieldItem.text.replace("Record.", "")])
    
    # Writing to CSV file
    # with open(output_file, "a", newline="") as file:
    #     writer = csv.writer(file)
    #     writer.writerows(data)


for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if filename != ".DS_Store":
        if os.path.isfile(file_path):
            # Process the file
            print(f"File: {filename}")
            parsePrint(filename)