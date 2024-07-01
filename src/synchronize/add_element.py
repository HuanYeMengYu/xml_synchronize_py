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
            # 注释节点同路径同名如何处理？
            # if isinstance(src_child, etree._Comment) and isinstance(dst_child, etree._Comment):
            #     if src_child.text == dst_child.text:
            #         flag_exist = True
            #         break
            if isinstance(src_child, etree._Element) and isinstance(dst_child, etree._Element):
                if src_child.tag == dst_child.tag:
                    flag_exist = True
                    break

        # 查找目标xml中是否已经存在对应标签(名称相同、xpath相同)
        # if isinstance(src_child, etree._Comment):

        #     print(src_child)
        #     print(src_child.tag)
        #     print(src_child.text)

        #     dst_children = dst_elem.getroottree().xpath(f"//comment()[. = 'r{src_child.text}']")
        # else:
        #     dst_children = dst_elem.xpath(f'//{src_child.tag}')
        # if len(dst_children) != 0:
        #     for dst_child in dst_children:
        #         # 获取其父节点的路径，因为注释的路径带有下标，但是此处不需要用下标区分注释节点的位置
        #         src_path = get_path.get_path(src_child.getparent())
        #         dst_path = get_path.get_path(dst_child.getparent())
        #         if src_path == dst_path:
        #             flag_exist = True
        #             break

        # 已经存在对应标签则跳过
        if flag_exist:
            continue
        else:
            print(f"添加标签{get_path.get_path(src_child)}")
            index = get_index.get_index(src_child)
            dst_parent.insert(index, copy.deepcopy(src_child))

        # 不存在对应标签则添加标签
        # src_elem_parent = src_child.getparent()
        # dst_elem_parents = dst_elem.xpath(f'//{src_elem_parent.tag}')
        # for dst_elem_parent in dst_elem_parents:
        #     if get_path.get_path(dst_elem_parent) == get_path.get_path(src_elem_parent):
        #         print(f"添加标签{get_path.get_path(src_child)}")
        #         index = get_index.get_index(src_child)
        #         dst_elem_parent.insert(index, copy.deepcopy(src_child))
        #         break

if __name__ == '__main__':
    src_doc = etree.parse("../../resource/test1.xml")
    dst_doc = etree.parse("../../resource/test2.xml")
    src_root = src_doc.getroot()
    dst_root = dst_doc.getroot()
    sync_add(src_root, dst_root)
    dst_doc.write("../../resource/test2.xml", pretty_print=True)
