from lxml import etree
from . import get_index
from . import get_path
import copy

def sync_add(src_elem, dst_elem):
    # 获取所有子孙标签
    src_children = src_elem.iterdescendants()

    # 遍历所有子孙标签
    for src_child in src_children:

        if isinstance(src_child, etree._Comment):
            continue

        # 该标签是否已经存在
        flag_exist = False

        src_parent = src_child.getparent()
        src_parent_path = get_path.get_path(src_parent)
        dst_parents = dst_elem.getroottree().xpath(src_parent_path)
        dst_parent = dst_parents[0]
        dst_children = dst_parent.iterchildren()
        for dst_child in dst_children:
            if isinstance(src_child, etree._Element) and isinstance(dst_child, etree._Element):
                if src_child.tag == dst_child.tag:
                    flag_exist = True
                    break

        # 已经存在对应标签则跳过
        if flag_exist:
            continue
        else:
            print(f"添加标签{get_path.get_path(src_child)}")
            index = get_index.get_index(src_child)
            dst_parent.insert(index, copy.deepcopy(src_child))

if __name__ == '__main__':
    src_doc = etree.parse("../../resource/test1.xml")
    dst_doc = etree.parse("../../resource/test2.xml")
    src_root = src_doc.getroot()
    dst_root = dst_doc.getroot()
    sync_add(src_root, dst_root)
    dst_doc.write("../../resource/test2.xml", pretty_print=True)
