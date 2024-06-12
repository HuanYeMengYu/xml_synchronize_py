from lxml import etree

# 解析 XML 文档
root = etree.parse("test_comment.xml")

# 使用 iter() 方法遍历所有元素和注释节点
for node in root.iter(etree.Element, etree.Comment):
    if isinstance(node, etree._Comment):
        print("注释节点:", node.text)
    else:
        print("元素节点:", node.tag, "-", node.text)
