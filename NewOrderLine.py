import xml.etree.ElementTree as ET

# Define the path to the XML file
xml_file = r'C:\Test\Test.xml'
@file_path = r'C:\Test\Test.xml'
# Number of additional copies to create
num_copies = 3
print (xml_file)
# Namespace dictionary
namespaces = {
    'mtccore': 'http://system.mp-objects.com/schemas/MTC/MTCCore/V1/MTCCore.xsd',
    'mtc': 'http://system.mp-objects.com/schemas/MTC/CustomerOrder/CustomerOrder.xsd'
}

def increment_product_id(product_id_text, increment):
    """Increment the PRODUCT_ID value."""
    base, current_number = product_id_text.rsplit('-', 1)
    new_number = str(int(current_number) + increment)
    return f"{base}-{new_number}"

def add_copies_to_xml(file_path, num_copies):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Print root tag and attributes for debugging
    print(f"Root tag: {root.tag}")
    print(f"Root attributes: {root.attrib}")

    # Find the CUSTOMER_ORDER_LINE section to copy
    customer_order_lines = root.findall('.//mtcore:CUSTOMER_ORDER_LINE', namespaces)
    if not customer_order_lines:
        print('No CUSTOMER_ORDER_LINE sections found.')
        return

    # Print found CUSTOMER_ORDER_LINE sections for debugging
    for idx, line in enumerate(customer_order_lines):
        print(f"Found CUSTOMER_ORDER_LINE #{idx}:")
        ET.dump(line)

    # Use the first CUSTOMER_ORDER_LINE as a template
    customer_order_line = customer_order_lines[0]

    # Get the PRODUCT_ID text from the existing CUSTOMER_ORDER_LINE
    product_id_elem = customer_order_line.find('.//mtccore:PRODUCT_ID', namespaces)
    if product_id_elem is None:
        print('No PRODUCT_ID found.')
        return

    base_product_id = product_id_elem.text

    # Find the CUSTOMER_ORDER element to append the new lines
    customer_order = root.find('.//mtc:CUSTOMER_ORDER', namespaces)
    if customer_order is None:
        print('No CUSTOMER_ORDER section found.')
        return

    # Create new CUSTOMER_ORDER_LINE sections
    for i in range(1, num_copies + 1):
        # Create a new CUSTOMER_ORDER_LINE element
        new_order_line = ET.Element('mtccore:CUSTOMER_ORDER_LINE', nsmap=namespaces)
        for elem in customer_order_line:
            new_elem = ET.SubElement(new_order_line, elem.tag, nsmap=namespaces)
            new_elem.text = elem.text

        # Increment PRODUCT_ID
        product_id_elem = new_order_line.find('.//mtccore:PRODUCT_ID', namespaces)
        if product_id_elem is not None:
            product_id_elem.text = increment_product_id(base_product_id, i)

        # Append the new CUSTOMER_ORDER_LINE to the CUSTOMER_ORDER
        customer_order.append(new_order_line)

    # Write the modified XML back to the file
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

# Run the function
add_copies_to_xml(xml_file, num_copies)
