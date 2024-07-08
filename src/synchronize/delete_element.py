from lxml import etree
from . import get_path

def sync_del(src_elem, dst_elem):
    # 获取所有子孙标签
    dst_children = list(dst_elem.iterdescendants())
    # 遍历所有子孙标签
    for dst_child in dst_children:

        # 该标签是否已经存在
        flag_exist = False

        dst_parent = dst_child.getparent()

        dst_parent_path = get_path.get_path(dst_parent)

        src_parents = src_elem.getroottree().xpath(dst_parent_path)
        # 该节点已经在目标xml中删除，则直接跳过
        if len(src_parents)==0:
            continue
        src_parent = src_parents[0]
        src_children = src_parent.iterchildren()
        for src_child in src_children:
            if isinstance(src_child, etree._Element) and isinstance(dst_child, etree._Element):
                if src_child.tag == dst_child.tag:
                    flag_exist = True
                    break

        # 已经存在对应标签则跳过
        if flag_exist:
            continue
        else:
            print(f"删除标签{get_path.get_path(dst_child)}")
            dst_parent.remove(dst_child)

if __name__ == '__main__':
    src_doc = etree.parse("../../resource/test1.xml")
    dst_doc = etree.parse("../../resource/test2.xml")
    src_root = src_doc.getroot()
    dst_root = dst_doc.getroot()
    sync_del(src_root, dst_root)
    dst_doc.write("../../resource/test2.xml", pretty_print=True)
    