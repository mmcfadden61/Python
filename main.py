import xml.etree.ElementTree as ET

def make_copies_of_section(file_path, section_tag, num_copies):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Find the section to copy
    section_to_copy = root.find(section_tag)

    if section_to_copy is None:
        print(f"Section <{section_tag}> not found in the XML file.")
        return

    # Make copies of the section
    for i in range(1, num_copies + 1):
        # Create a copy of the section
        section_copy = ET.fromstring(ET.tostring(section_to_copy))

        # Find the INVOICE_IDENTIFIER element and update its VALUE
        invoice_identifier = section_copy.find("INVOICE_IDENTIFIER")
        if invoice_identifier is not None:
            value_element = invoice_identifier.find("VALUE")
            if value_element is not None:
                value_element.text = f"RUN1305B_copy{i}"

        # Append the copy to the root
        root.append(section_copy)

    # Write the modified XML back to the file
    tree.write(file_path)
    print(f"Added {num_copies} copies of <{section_tag}> to {file_path}")

# Example usage
file_path = "C:\Test\INVOICE_UPS.xml"  # Replace with your XML file path
section_tag = "<INVOICE_LINE>"  # The tag of the section to copy
num_copies = 5  # Number of copies you want to make

make_copies_of_section(file_path, section_tag, num_copies)
