import re

def sync_declaration(source_path, target_path, xml_encoding):
    # Define an internal function to find the location of the XML root node(open)
    def find_open_root_position(content):
        # Use regular expressions to match the root node starting with the beginning of the line
        match = re.search(r'^<(\w+)[^>]*>', content, re.MULTILINE)
        return match.start() if match else -1
    # Define an internal function to find the location of the XML root node(close)
    def find_close_root_position(content):
        # Use regular expressions to match the root node starting with the beginning of the line
        match = re.search(r'^</(\w+)>', content, re.MULTILINE)
        return match.end() if match else -1

    # Read the content of the source file
    with open(source_path, 'r', encoding=xml_encoding) as source_file:
        source_content = source_file.read()

    # Read the content of the target file
    with open(target_path, 'r', encoding=xml_encoding) as target_file:
        target_content = target_file.read()

    # Find the location of the root node in the source file and the target file
    source_root_pos = find_open_root_position(source_content)
    target_root_pos = find_open_root_position(target_content)
    source_end_root_pos = find_close_root_position(source_content)
    target_end_root_pos = find_close_root_position(target_content)

    # Ensure that both the source file and the target file contain the root node
    if source_root_pos == -1:
        raise ValueError("No root element found in the source file")
    if target_root_pos == -1:
        raise ValueError("No root element found in the target file")
    if source_end_root_pos == -1:
        raise ValueError("No root element(end) found in the source file")
    if target_end_root_pos == -1:
        raise ValueError("No root element(end) found in the target file")

    # Extract the content before the root node of the source file
    source_declaration = source_content[:source_root_pos]
    source_declaration_no_empty_lines = "\n".join([line for line in source_declaration.splitlines() if line.strip() != ""])
    # Extract the content after the root node of the target file
    target_after_root = target_content[target_root_pos:target_end_root_pos]

    # Extract the content after the root node(end) of the source file
    source_end_declaration = source_content[source_end_root_pos:]
    source_end_declaration_no_empty_lines = "\n".join([line for line in source_end_declaration.splitlines() if line.strip() != ""])

    # Replace the content before the root node of the source file into the target file
    target_new_content = source_declaration_no_empty_lines + "\n" + target_after_root + "\n" + source_end_declaration_no_empty_lines

    # Write the modified content back to the target file
    with open(target_path, 'w', encoding=xml_encoding) as target_file:
        target_file.write(target_new_content)

if __name__ == '__main__':
    sync_declaration("../../resource/maccfg.xml", "../../resource/project/build/nr5g/maccfg.xml", 'utf-8')
