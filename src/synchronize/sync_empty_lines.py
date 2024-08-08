def sync_empty_lines(source_path, target_path, xml_encoding):
    # Reading the source XML file
    with open(source_path, 'r', encoding=xml_encoding) as source_file:
        source_content = source_file.readlines()
    # Read the target XML file
    with open(target_path, 'r', encoding=xml_encoding) as target_file:
        target_content = target_file.readlines()
    # Find the blank line numbers in the source XML file
    empty_lines = [i for i, line in enumerate(source_content) if not line.strip()]

    # The contents of the target XML file are converted to a list
    target_lines = target_content

    # Update the content of the target XML file
    updated_target_lines = []
    empty_line_index = 0

    for i, line in enumerate(target_lines):
        updated_target_lines.append(line)
        # Add blank lines from the source XML file to the target XML file
        while empty_line_index < len(empty_lines) and i+empty_line_index+1 == empty_lines[empty_line_index]:
            updated_target_lines.append(source_content[empty_lines[empty_line_index]])
            empty_line_index += 1

    # The last line of the synchronization file (may be blank)
    updated_target_lines[-1] = source_content[-1]

    # Write the updated content to the target XML file
    with open(target_path, 'w', encoding=xml_encoding) as target_file:
        target_file.writelines(updated_target_lines)

if __name__ == '__main__':
    source_xml_path = '../../resource/maccfg.xml'
    target_xml_path = '../../resource/project/build/nr5g/maccfg.xml'
    sync_empty_lines(source_xml_path, target_xml_path, 'utf-8')
