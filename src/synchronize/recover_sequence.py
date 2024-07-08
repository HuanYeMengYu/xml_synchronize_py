from lxml import etree
from . import get_index
from . import get_path
from . import get_element_index
import copy

def recover_sequence(src_elem, dst_elem):
    # 获取所有子孙标签
    src_children = src_elem.iterdescendants()

    # 遍历所有子孙标签
    for src_child in src_children:
        if isinstance(src_child, etree._Element):

            src_parent = src_child.getparent()
            src_parent_path = get_path.get_path(src_parent)
            dst_parents = dst_elem.getroottree().xpath(src_parent_path)
            dst_parent = dst_parents[0]
            # 获取正确下标
            index = get_element_index.get_element_index(src_child)
            dst_children = dst_parent.iterchildren()
            for dst_child in dst_children:
                if isinstance(src_child, etree._Element) and isinstance(dst_child, etree._Element):
                    if src_child.tag == dst_child.tag:
                        dst_parent.insert(index, copy.deepcopy(dst_child))
                        dst_parent.remove(dst_child)
                        break

if __name__ == '__main__':
    # 测试用例
    src_xml_str = """
    <root>
        <!-- Comment1 -->
        <child1>
            <a>1</a>
            <b>2</b>
            <c>3</c>
        </child1>
        <!-- Comment2 -->
        <child2>
            <d>4</d>
            <e>5</e>
            <f>6</f>
        </child2>
    </root>
    """

    dst_xml_str = """
    <root>
        <!-- Comment2 -->
        <!-- Comment1 -->
        <child2>
            <e>5</e>
            <d>4</d>
            <f>6</f>
        </child2>
        <child1>
            <c>3</c>
            <b>2</b>
            <a>1</a>
        </child1>
    </root>
    """

    # 解析XML
    src_tree = etree.XML(src_xml_str)
    dst_tree = etree.XML(dst_xml_str)

    # 调用函数
    recover_sequence(src_tree, dst_tree)

    # 输出调整后的XML
    print(etree.tostring(dst_tree, pretty_print=True).decode())
