from lxml import etree
import copy

def sync_add(src_elem, dst_elem):
    src_children = src_elem.iterdescendants()
    # 迭代普通的元素节点
    normal_elements = [elem for elem in src_children if not isinstance(elem, etree._Comment)]
    for src_child in normal_elements:
        flag_exit = False
        dst_children = dst_elem.xpath(f'//{src_child.tag}')
        if len(dst_children) != 0:
            for dst_child in dst_children:
                if dst_child.getroottree().getpath(dst_child) == src_child.getroottree().getpath(src_child):
                    flag_exit = True
        
        if flag_exit:
            continue

        src_elem_parent = src_child.getparent()
        dst_elem_parents = dst_elem.xpath(f'//{src_elem_parent.tag}')
        for dst_elem_parent in dst_elem_parents:
            if(dst_elem_parent.getroottree().getpath(dst_elem_parent) == src_elem_parent.getroottree().getpath(src_elem_parent)):
                print(f"添加标签{src_child.getroottree().getpath(src_child)}")
                index = src_elem_parent.index(src_child)
                dst_elem_parent.insert(index, copy.deepcopy(src_child))

if __name__ == '__main__':
    src_doc = etree.parse("../../resource/test1.xml")
    dst_doc = etree.parse("../../resource/test2.xml")
    src_root = src_doc.getroot()
    dst_root = dst_doc.getroot()
    sync_add(src_root, dst_root)
    dst_doc.write("../../resource/test2.xml", pretty_print=True)
