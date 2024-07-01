from lxml import etree

def get_element_index(elem):
    if isinstance(elem, etree._Comment):
        return -1
    children = elem.getparent().iterchildren()
    index = 0
    for child in children:
        if isinstance(child, etree._Element):
            if child.tag == elem.tag:
                return index
            index += 1

if __name__ == "__main__":
    # XML 内容作为字符串
    xml_string = '''
    <root>
        <!-- This is the first comment -->
        <child>Some content</child>
        <!-- This is the second comment -->
        <child1>Some content</child1>
        <child2>Some content</child2>
        <child3>Some content</child3>
    </root>
    '''

    # 解析 XML 字符串
    doc = etree.fromstring(xml_string)

    # 查找所有注释节点
    children = doc.iterdescendants()
    
    # 打印每个注释节点的索引
    for child in children:
        print(get_element_index(child))
