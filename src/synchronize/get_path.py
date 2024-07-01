from lxml import etree

def get_path(elem):
    return elem.getroottree().getpath(elem)

if __name__ == '__main__':
    # 创建一个简单的 XML 示例
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
    # 解析 XML
    root = etree.XML(xml_str)
    
    # 获取每个子元素的路径
    for elem in root.iterdescendants():
        path = get_path(elem)
        print(f"Path of {elem.tag}: {path}")
        print(f"index={elem.getparent().index(elem)}")
