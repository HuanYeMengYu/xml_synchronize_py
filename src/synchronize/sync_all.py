from lxml import etree
import os
from . import sync_value
from . import add_element
from . import delete_element
from . import get_sync_elems

def sync_all(sync_value_file, sample_xml_path, dst_xmls_path):
    # 格式化样本xml文件
    os.system(f"xmllint --format {sample_xml_path} -o {sample_xml_path}")

    src_doc = etree.parse(sample_xml_path)
    src_root = src_doc.getroot()
    sync_elems = get_sync_elems.get_sync_elems(sync_value_file)
    for dst_xml_path in dst_xmls_path:
        dst_doc = etree.parse(dst_xml_path)
        dst_root = dst_doc.getroot()

        delete_element.sync_del(src_root, dst_root)
        add_element.sync_add(src_root, dst_root)
        sync_value.sync_value(src_root, dst_root, sync_elems)

        dst_doc.write(dst_xml_path, pretty_print=True)
        # 调用系统命令
        os.system(f"xmllint --format {dst_xml_path} -o {dst_xml_path}")

if __name__ == '__main__':
    sync_all("../../resource/sync_value.txt", "../../resource/test1.xml", "../../resource/test2.xml")
