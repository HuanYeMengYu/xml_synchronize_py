from lxml import etree

def has_same_tag_element(elem):
    has_duplicated_tag = False
    tags_seen = set()
    tags_duplicated = set()
    for child in elem.iterdescendants():
        if not isinstance(child, etree._Comment):
            # Get the tag name
            tag = child.tag
            # Check if the tag name already exists
            if tag in tags_seen:
                has_duplicated_tag = True
                tags_duplicated.add(tag)
            # Add the tag name to the collection
            tags_seen.add(tag)
    return has_duplicated_tag, tags_duplicated

if __name__ == '__main__':
    # Example usage:

    # Example XML
    xml_str = """
    <root>
        <parent>
            <child1/>
            <child2/>
            <child1/> <!-- Duplicate tag -->
        </parent>
    </root>
    """

    root = etree.XML(xml_str)

    # Check if 'parent' element has duplicate tags
    has_duplicated_tag, tags_duplicated = has_same_tag_element(root.find('parent'))
    if has_duplicated_tag:
        print(f"The 'parent' element has duplicate tags:{tags_duplicated}")
    else:
        print("The 'parent' element does not have duplicate tags.")
