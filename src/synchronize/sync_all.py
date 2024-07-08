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
from . import sync_declaration
from . import check_xml_with_xmllint

def sync_all(sync_value_file, sample_xml_path, dst_xmls_path):

    # 检查源xml文件是否符合规范
    check = check_xml_with_xmllint.check_xml_with_xmllint(sample_xml_path)
    if check==0:
        return

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

        # 检查目标xml文件是否符合规范
        check = check_xml_with_xmllint.check_xml_with_xmllint(dst_xml_path)
        if check==0:
            continue
        dst_doc = etree.parse(dst_xml_path)
        dst_root = dst_doc.getroot()

        # 判断该xml是否存在同名标签
        if has_same_tag_element.has_same_tag_element(dst_root):
            print(f"{dst_xml_path}存在同名标签，跳过该文件")
            continue

        # 先删除所有注释，防止影响增删节点的判断;(相同结构xml的注释应该也结构、内容相同)
        delete_all_comment.delete_all_comment(dst_root)
        # 增加节点
        add_element.sync_add(src_root, dst_root)
        # 增加新节点后注释节点被自动拷贝进去，再次删除所有注释防止影响后续删除节点
        delete_all_comment.delete_all_comment(dst_root)
        # 删除节点
        delete_element.sync_del(src_root, dst_root)
        # 同步指定节点的数据
        sync_value.sync_value(src_root, dst_root, sync_elems)
        # 同步节点顺序
        recover_sequence.recover_sequence(src_root, dst_root)
        # 同步注释节点
        sync_comment.sync_comment(src_root, dst_root)

        # 写入同步后的xml文件; 按阅览模式打印; 打印包括编码格式的声明节点
        dst_doc.write(dst_xml_path, pretty_print=True, encoding=xml_encoding, xml_declaration=True)
        # 同步xml声明
        sync_declaration.sync_declaration(sample_xml_path, dst_xml_path)
        # 调用系统命令，把xml格式化
        os.system(f"xmllint --format {dst_xml_path} -o {dst_xml_path}")

    # 格式化样本xml文件
    os.system(f"xmllint --format {sample_xml_path} -o {sample_xml_path}")

if __name__ == '__main__':
    sync_all("../../resource/sync_value.txt", "../../resource/test1.xml", "../../resource/test2.xml")
