import xml.etree.ElementTree as ET

def make_copies_of_invoice_lines(file_path, num_copies):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Find the body/INVOICE element
    invoice_element = root.find(".//body/INVOICE")

    if invoice_element is None:
        print("INVOICE element not found in the XML file.")
        return

    # Find all INVOICE_LINE elements
    invoice_lines = invoice_element.findall("INVOICE_LINE")

    if not invoice_lines:
        print("No INVOICE_LINE elements found in the XML file.")
        return

    # Make copies of each INVOICE_LINE element
    for i in range(1, num_copies + 1):
        for invoice_line in invoice_lines:
            # Create a copy of the INVOICE_LINE element
            invoice_line_copy = ET.fromstring(ET.tostring(invoice_line))

            # Find the INVOICE_IDENTIFIER element and update its VALUE
            invoice_identifier = invoice_line_copy.find("INVOICE_IDENTIFIER")
            if invoice_identifier is not None:
                value_element = invoice_identifier.find("VALUE")
                if value_element is not None:
                    # Increment the VALUE text to ensure uniqueness
                    value_element.text = f"{value_element.text}_copy{i}"

            # Append the copy to the INVOICE element
            invoice_element.append(invoice_line_copy)

    # Write the modified XML back to the file with proper formatting
    tree.write(file_path, encoding="utf-8", xml_declaration=True)

    # Reformat the XML file to ensure proper indentation and new lines
    with open(file_path, 'r', encoding='utf-8') as file:
        xml_content = file.read()

    formatted_xml_content = format_xml(xml_content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_xml_content)

    print(f"Added {num_copies} copies of each INVOICE_LINE to {file_path}")

def format_xml(xml_string):
    """Function to format XML string with proper indentation and new lines."""
    from xml.dom.minidom import parseString
    dom = parseString(xml_string)
    return dom.toprettyxml()

# Example usage
file_path = r"C:\Test\INVOICE_UPS.xml"  # Replace with your XML file path
num_copies = 2  # Number of copies you want to make

make_copies_of_invoice_lines(file_path, num_copies)
