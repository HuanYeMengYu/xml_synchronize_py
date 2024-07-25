from lxml import etree

def get_node_path(elem):
    return elem.getroottree().getpath(elem)

if __name__ == '__main__':
    # Creating a simple XML example
    xml_str = """
    <root>
        <!-- com1 -->
        <parent>
            <child1/>
            <!-- com2 -->
            <child2/>
        </parent>
        <!-- com3 -->
        <another_parent>
            <child3/>
            <!-- com4 -->
        </another_parent>
    </root>
    """
    # Parsing XML
    root = etree.XML(xml_str)
    
    # Get the path of each child element
    for elem in root.iterdescendants():
        path = get_node_path(elem)
        print(f"Path of {elem.tag}: {path}")
        print(f"index={elem.getparent().index(elem)}")
