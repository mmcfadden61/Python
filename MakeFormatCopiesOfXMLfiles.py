import shutil
from xml.dom.minidom import parseString
from xml.parsers.expat import ExpatError


# This function formats the XML content to ensure proper indentation and new lines
def format_xml(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            xml_content = file.read()

        dom = parseString(xml_content)
        formatted_xml_content = dom.toprettyxml()

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(formatted_xml_content)
    except ExpatError as e:
        print(f"Error formatting XML file {file_path}: {e}")

# This file makes multiple copies of a XML file
def make_copies(src_file, dest_dir, num_copies):
    for i in range(1, num_copies + 1):
        dest_file = f"{dest_dir}/copy_{i}.xml"
        shutil.copy2(src_file, dest_file)
        format_xml(dest_file)
        print(f"Copy {i} created at {dest_file}")



# Example usage
source_file = r'C:\Test\Test.xml'
destination_directory = 'C:\Test'
number_of_copies = 3

make_copies(source_file, destination_directory, number_of_copies)
