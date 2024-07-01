from lxml import etree
import os
from . import sync_value
from . import add_element
from . import delete_element
from . import get_sync_elems
from . import recover_sequence
from . import has_same_tag_element
from . import delete_all_comment
from . import sync_comment

def sync_all(sync_value_file, sample_xml_path, dst_xmls_path):

    src_doc = etree.parse(sample_xml_path)
    src_root = src_doc.getroot()

    # 获取XML版本和编码
    xml_encoding = src_doc.docinfo.encoding

    # 判断该xml是否存在同名标签
    if has_same_tag_element.has_same_tag_element(src_root):
        print(f"{sample_xml_path}存在同名标签，跳过该文件")
        return

    sync_elems = get_sync_elems.get_sync_elems(sync_value_file)
    for dst_xml_path in dst_xmls_path:
        dst_doc = etree.parse(dst_xml_path)
        dst_root = dst_doc.getroot()

        # 判断该xml是否存在同名标签
        if has_same_tag_element.has_same_tag_element(dst_root):
            print(f"{dst_xml_path}存在同名标签，跳过该文件")
            continue

        delete_all_comment.delete_all_comment(dst_root)
        add_element.sync_add(src_root, dst_root)
        delete_element.sync_del(src_root, dst_root)
        sync_value.sync_value(src_root, dst_root, sync_elems)
        recover_sequence.recover_sequence(src_root, dst_root)
        sync_comment.sync_comment(src_root, dst_root)

        # 写入同步后的xml文件; 按阅览模式打印; 打印包括编码格式的声明节点
        dst_doc.write(dst_xml_path, pretty_print=True, encoding=xml_encoding, xml_declaration=True)
        # 调用系统命令
        os.system(f"xmllint --format {dst_xml_path} -o {dst_xml_path}")

    # 写入同步后的xml文件; 按阅览模式打印; 打印包括编码格式的声明节点
    src_doc.write(sample_xml_path, pretty_print=True, encoding=xml_encoding, xml_declaration=True)

    # 格式化样本xml文件
    os.system(f"xmllint --format {sample_xml_path} -o {sample_xml_path}")

if __name__ == '__main__':
    sync_all("../../resource/sync_value.txt", "../../resource/test1.xml", "../../resource/test2.xml")
