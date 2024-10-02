import xml.etree.ElementTree as ET

# Define the path to the XML file
file_path = r'C:\Test\Test.xml'

# Number of copies to add
num_copies = 4

# Namespace dictionary
namespaces = {
    'mtccore': 'http://system.mp-objects.com/schemas/MTC/MTCCore/V1/MTCCore.xsd'
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

    # Find the CUSTOMER_ORDER_LINE section to copy
    #customer_order_line = root.find('.//mtccore:CUSTOMER_ORDER_LINE', namespaces)
    customer_order_line = root.find('mtccore:CUSTOMER_ORDER_LINE', namespaces)
    print (customer_order_line)
    if customer_order_line is None:
        print('No CUSTOMER_ORDER_LINE section found.')
        return

    # Get the PRODUCT_ID text from the existing CUSTOMER_ORDER_LINE
    product_id_elem = customer_order_line.find('.//mtccore:PRODUCT_ID', namespaces)
    if product_id_elem is None:
        print('No PRODUCT_ID found.')
        return

    base_product_id = product_id_elem.text

    # Find the parent element (assumed to be CUSTOMER_ORDER) to append the new lines
    customer_order = root.find('mtccore:CUSTOMER_ORDER_LINE', namespaces)
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
add_copies_to_xml(file_path, num_copies)
