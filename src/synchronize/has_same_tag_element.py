from lxml import etree

def has_same_tag_element(elem):
    """
    Check if an Element has duplicate child tags.
    
    Args:
    - elem (lxml.etree.Element): The Element to check.
    
    Returns:
    - bool: True if duplicate tags exist, False otherwise.
    """
    tags_seen = set()
    for child in elem.iterdescendants():
        if not isinstance(child, etree._Comment):
            # 获取标签名称
            tag = child.tag
            # 检查是否已经存在该标签名称
            if tag in tags_seen:
                return True
            # 将该标签名称添加到集合
            tags_seen.add(tag)
    return False

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
    if has_same_tag_element(root.find('parent')):
        print("The 'parent' element has duplicate tags.")
    else:
        print("The 'parent' element does not have duplicate tags.")
