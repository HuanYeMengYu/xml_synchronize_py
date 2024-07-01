from lxml import etree

def delete_all_comment(root):

    children = root.iterdescendants()

    for child in children:
        if isinstance(child, etree._Comment):
            child.getparent().remove(child)

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
        <add1>
            <!-- comm1 -->
            <son1>son1</son1>
            <son2>son2</son2>
            <son3>
                <!-- comm2 -->
                <grandson1>grandson1</grandson1>
                <!-- comm3 -->
                <grandson2>grandson2</grandson2>
                <grandson3>grandson3</grandson3>
            </son3>
        </add1>
    </root>
    '''

    # 解析 XML 字符串
    doc = etree.fromstring(xml_string)

    delete_all_comment(doc)

    print(etree.tostring(doc, pretty_print=True, encoding='unicode'))
