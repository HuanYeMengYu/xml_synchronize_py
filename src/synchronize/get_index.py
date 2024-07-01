from lxml import etree

def get_index(elem):
    return elem.getparent().index(elem)

if __name__ == '__main__':
    # 创建一个简单的 XML 示例
    xml_str = """
    <root>
        <child1/>
        <child2/>
        <child3/>
    </root>
    """
    # 解析 XML
    root = etree.XML(xml_str)
    
    # 获取每个子元素的 index
    for child in root:
        index = get_index(child)
        print(f"Index of {child.tag}: {index}")
