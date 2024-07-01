from lxml import etree
import copy
from . import get_index
from . import get_path

def sync_comment(src_elem, dst_elem):
    
    # 获取所有子孙标签
    src_children = src_elem.iterdescendants()
    # 遍历所有子孙标签
    for src_child in src_children:
        if isinstance(src_child, etree._Comment):
            src_parent = src_child.getparent()
            src_parent_path = get_path.get_path(src_parent)
            index = get_index.get_index(src_child)
            dst_parents = dst_elem.getroottree().xpath(src_parent_path)
            dst_parent = dst_parents[0]
            dst_parent.insert(index, copy.deepcopy(src_child))

if __name__ == '__main__':
    # 示例 XML 字符串
    src_xml_string = '''
    <root>
        <child1>
            <!-- Source Comment 1 -->
            <subchild1>Subcontent 1</subchild1>
        </child1>
        <child2>
            <!-- Source Comment 2 -->
            <!-- Source Comment 3 -->
            <subchild2>Subcontent 2</subchild2>
            <add1>
                <!-- Source Comment 4 -->
                <add2>add2</add2>
                <!-- Source Comment 5 -->
                <add3>add3</add3>
                <!-- Source Comment 6 -->
                <add4>add4</add4>
                <!-- Source Comment 7 -->
            </add1>
        </child2>
    </root>'''

    dst_xml_string = '''
    <root>
        <child1>
            <subchild1>Subcontent A</subchild1>
        </child1>
        <child2>
            <subchild2>Subcontent B</subchild2>
            <add1>
                <add2>add2</add2>
                <add3>add3</add3>
                <add4>add4</add4>
            </add1>
        </child2>
    </root>'''

    # 解析 XML 字符串为 Element 对象
    src_root = etree.fromstring(src_xml_string)
    dst_root = etree.fromstring(dst_xml_string)

    # 同步注释节点
    sync_comment(src_root, dst_root)

    # 打印同步后的目标 XML
    print(etree.tostring(dst_root, pretty_print=True, encoding='unicode'))
