from lxml import etree
from . import get_node_path
from . import get_sync_elems

def sync_value(src_elem, dst_elem, sync_elems):
    # Synchronize the content of the specified element
    for elem_name in sync_elems:
        find_src_elems = src_elem.xpath(f'//{elem_name}')
        find_dst_elems = dst_elem.xpath(f'//{elem_name}')
        for find_src_elem in find_src_elems:
            for find_dst_elem in find_dst_elems:
                if get_node_path.get_node_path(find_src_elem) == get_node_path.get_node_path(find_dst_elem):
                    with open('succeed.txt', 'a') as file:
                        file.write("Synchronized tag data '{}' = {}\n".format(get_node_path.get_node_path(find_src_elem), find_src_elem.text))
                    # print(f"Synchronized tag data '{get_node_path.get_node_path(find_src_elem)}' = {find_src_elem.text}")
                    find_dst_elem.text = find_src_elem.text

if __name__ == '__main__':
    src_doc = etree.parse("../../resource/test1.xml")
    dst_doc = etree.parse("../../resource/test2.xml")
    src_root = src_doc.getroot()
    dst_root = dst_doc.getroot()
    words = get_sync_elems.get_sync_elems("../../resource/sync_value.txt")
    sync_value(src_root, dst_root, words)
    dst_doc.write("../../resource/test2.xml", pretty_print=True)
