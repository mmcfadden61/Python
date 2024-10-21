import shutil

# This file makes multiple copies of a XML file
def make_copies(src_file, dest_dir, num_copies):
    for i in range(1, num_copies + 1):
        dest_file = f"{dest_dir}/copy_{i}.xml"
        shutil.copy2(src_file, dest_file)
        print(f"Copy {i} created at {dest_file}")



# Example usage
source_file = r'C:\Test\TestWithVariable.xml'
destination_directory = 'C:\Test'
number_of_copies = 3

make_copies(source_file, destination_directory, number_of_copies)
