from lxml import etree
from . import get_node_path

def sync_del(src_elem, dst_elem):
    # Get all descendant tags
    dst_children = list(dst_elem.iterdescendants())
    # Traverse all descendant tags
    for dst_child in dst_children:

        # Does the tag already exist?
        flag_exist = False

        dst_parent = dst_child.getparent()

        dst_parent_path = get_node_path.get_node_path(dst_parent)

        src_parents = src_elem.getroottree().xpath(dst_parent_path)
        # This node has been deleted in the target XML, so it will be skipped directly
        if len(src_parents)==0:
            continue
        src_parent = src_parents[0]
        src_children = src_parent.iterchildren()
        for src_child in src_children:
            if isinstance(src_child, etree._Element) and isinstance(dst_child, etree._Element):
                if src_child.tag == dst_child.tag:
                    flag_exist = True
                    break

        # If the corresponding tag already exists, skip it
        if flag_exist:
            continue
        else:
            with open('succeed.txt', 'a') as file:
                file.write("Deleted tag '{}'\n".format(get_node_path.get_node_path(dst_child)))
            # print(f"Deleted tag '{get_node_path.get_node_path(dst_child)}'")
            dst_parent.remove(dst_child)

if __name__ == '__main__':
    src_doc = etree.parse("../../resource/test1.xml")
    dst_doc = etree.parse("../../resource/test2.xml")
    src_root = src_doc.getroot()
    dst_root = dst_doc.getroot()
    sync_del(src_root, dst_root)
    dst_doc.write("../../resource/test2.xml", pretty_print=True)
    