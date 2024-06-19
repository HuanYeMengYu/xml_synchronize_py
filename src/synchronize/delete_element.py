from lxml import etree

def sync_del(src_elem, dst_elem):
    dst_children = dst_elem.iterdescendants()
    # 迭代普通的元素节点
    normal_elements = [elem for elem in dst_children if not isinstance(elem, etree._Comment)]
    for dst_child in normal_elements:
        if len(dst_elem.xpath(f'//{dst_child.tag}'))==0:
            continue
        flag_exit = False
        find_src_children = src_elem.xpath(f'//{dst_child.tag}')
        if len(find_src_children)!=0:
            for find_src_child in find_src_children:
                if find_src_child.getroottree().getpath(find_src_child) == dst_child.getroottree().getpath(dst_child):
                    flag_exit = True

        if flag_exit == False:
            print(f"删除标签{dst_child.getroottree().getpath(dst_child)}")
            parent = dst_child.getparent()
            parent.remove(dst_child)

if __name__ == '__main__':
    src_doc = etree.parse("../../resource/test1.xml")
    dst_doc = etree.parse("../../resource/test2.xml")
    src_root = src_doc.getroot()
    dst_root = dst_doc.getroot()
    sync_del(src_root, dst_root)
    dst_doc.write("../../resource/test2.xml", pretty_print=True)
    