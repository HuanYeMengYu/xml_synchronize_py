from lxml import etree

def get_node_index(elem):
    return elem.getparent().index(elem)

if __name__ == '__main__':
    # Creating a simple XML example
    xml_str = """
    <root>
        <child1/>
        <child2/>
        <child3/>
    </root>
    """
    # Parsing XML
    root = etree.XML(xml_str)
    
    # Get the index of each child element
    for child in root:
        index = get_node_index(child)
        print(f"Index of {child.tag}: {index}")
