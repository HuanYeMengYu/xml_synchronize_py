from xml.dom import minidom

def set_xml_indent(xml_path, xml_encoding):
    # Reading XML Files
    with open(xml_path, 'r', encoding=xml_encoding) as file:
        xml_string = file.read()

    # Parsing an XML string
    xml = minidom.parseString(xml_string)
    # set the indent of xml
    pretty_xml_as_string = xml.toprettyxml(indent="    ")  # Use four spaces for indentation
    # Remove extra blank lines
    lines = pretty_xml_as_string.split('\n')
    non_empty_lines = [line for line in lines if line.strip() != '']
    pretty_xml_as_string = '\n'.join(non_empty_lines)

    # Write formatted XML to a new file
    with open(xml_path, 'w', encoding=xml_encoding) as file:
        file.write(pretty_xml_as_string)

if __name__ == '__main__':
    set_xml_indent("../../resource/cell1.xml")
