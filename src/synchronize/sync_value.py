from lxml import etree
from . import get_sync_elems

def sync_value(src_elem, dst_elem, sync_elems):
    # 同步指定的元素的数据
    for elem_name in sync_elems:
        find_src_elems = src_elem.xpath(f'//{elem_name}')
        find_dst_elems = dst_elem.xpath(f'//{elem_name}')
        for find_src_elem in find_src_elems:
            for find_dst_elem in find_dst_elems:
                if src_elem.getroottree().getpath(find_src_elem) == dst_elem.getroottree().getpath(find_dst_elem):
                    print(f"同步标签数据{src_elem.getroottree().getpath(find_src_elem)}")
                    find_dst_elem.text = find_src_elem.text

    # 同步注释
    # 迭代普通的元素节点
    # normal_elements = [elem for elem in src_children if not isinstance(elem, etree._Comment)]

if __name__ == '__main__':
    src_doc = etree.parse("../../resource/test1.xml")
    dst_doc = etree.parse("../../resource/test2.xml")
    src_root = src_doc.getroot()
    dst_root = dst_doc.getroot()
    words = get_sync_elems.get_sync_elems("../../resource/sync_value.txt")
    sync_value(src_root, dst_root, words)
    dst_doc.write("../../resource/test2.xml", pretty_print=True)
    