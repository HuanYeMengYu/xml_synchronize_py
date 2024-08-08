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
from . import set_xml_indent
from . import sync_empty_lines

def sync_all(sync_value_file, sample_xml_path, dst_xmls_path):
    with open('succeed.txt', 'w') as file:
        file.write("This is the information of successful synchronization of XML files.\n")
        file.write("---------------------------------------\n")
    with open('fail.txt', 'w') as file:
        file.write("This is the information of unsuccessful synchronization of XML files.\n")
        file.write("---------------------------------------\n")

    dst_xml_stat = [1] * len(dst_xmls_path)
    dst_xml_index = 0

    # Check whether the source XML file complies with the specification
    check = check_xml_with_xmllint.check_xml_with_xmllint(sample_xml_path)
    if check==0:
        print("\033[31mSample xml file has something wrong, cancel this synchronization\033[0m")
        dst_xml_stat = [2 for _ in dst_xml_stat]
        return dst_xml_stat

    src_doc = etree.parse(sample_xml_path)
    src_root = src_doc.getroot()

    # Get XML version and encoding
    xml_encoding = src_doc.docinfo.encoding

    # Determine whether the source xml has a tag with the same name
    has_duplicated_tag, tags_duplicated = has_same_tag_element.has_same_tag_element(src_root)
    if has_duplicated_tag:
        with open('fail.txt', 'a') as file:
            file.write("The source xml file '{}' has tags with same name {} .\n".format(sample_xml_path, tags_duplicated))
        print("\033[31mSample xml file has something wrong, cancel this synchronization\033[0m")
        dst_xml_stat = [2 for _ in dst_xml_stat]
        return dst_xml_stat

    sync_elems = get_sync_elems.get_sync_elems(sync_value_file)

    for dst_xml_path in dst_xmls_path:
        # Check whether the target XML file complies with the specification
        check = check_xml_with_xmllint.check_xml_with_xmllint(dst_xml_path)
        if check==0:
            dst_xml_stat[dst_xml_index] = 0
            dst_xml_index += 1
            continue
        dst_doc = etree.parse(dst_xml_path)
        dst_root = dst_doc.getroot()

        # The root tag name does not match, skip this target file.
        if src_root.tag != dst_root.tag:
            with open('fail.txt', 'a') as file:
                file.write("---------------------------------------\n")
                file.write("Failed synchronizing xml file '{}'\n".format(dst_xml_path))
                file.write("The target xml file's root tag name '{}' is different from that of sample xml file '{}'.\n".format(dst_root.tag, src_root.tag))
                file.write("Skip synchronizing this target file.\n")
            # print("---------------------------------------")
            # print(f"Failed synchronizing xml file '{dst_xml_path}'")
            # print(f"The target xml file's root tag name '{dst_root.tag}' is different from that of sample xml file '{src_root.tag}'.")
            # print("Skip synchronizing this target file.")
            dst_xml_stat[dst_xml_index] = 0
            dst_xml_index += 1
            continue

        # Determine whether the target xml has a tag with the same name
        has_duplicated_tag, tags_duplicated = has_same_tag_element.has_same_tag_element(dst_root)
        if has_duplicated_tag:
            with open('fail.txt', 'a') as file:
                file.write("---------------------------------------\n")
                file.write("Failed synchronizing xml file '{}'\n".format(dst_xml_path))
                file.write("The target xml file '{}' has tags with same name {} .\n".format(dst_xml_path, tags_duplicated))
                file.write("Skip synchronizing this target file.\n")
            # print("---------------------------------------")
            # print(f"Failed synchronizing xml file '{dst_xml_path}'")
            # print(f"The target xml file '{dst_xml_path}' has tags with same name {tags_duplicated} .")
            # print("Skip synchronizing this target file.")
            dst_xml_stat[dst_xml_index] = 0
            dst_xml_index += 1
            continue

        dst_xml_index += 1

        with open('succeed.txt', 'a') as file:
            file.write("---------------------------------------\n")
            file.write("Successfully synchronized file:'{}'\n".format(dst_xml_path))
        # print("---------------------------------------")
        # print(f"Successfully synchronized file:{dst_xml_path}")

        # Delete all comments first to prevent affecting the judgment of adding and deleting nodes
        delete_all_comment.delete_all_comment(dst_root)
        # Adding Nodes
        add_element.sync_add(src_root, dst_root)
        # Delete all comments again to prevent affecting subsequent node deletion.
        delete_all_comment.delete_all_comment(dst_root)
        # Deleting Nodes
        delete_element.sync_del(src_root, dst_root)
        # Synchronize the text of the specified node according to the node's name
        sync_value.sync_value(src_root, dst_root, sync_elems)
        # Synchronize node order
        recover_sequence.recover_sequence(src_root, dst_root)
        # Synchronize Comment Node
        sync_comment.sync_comment(src_root, dst_root)

        # Write the synchronized XML file in reading mode
        dst_doc.write(dst_xml_path, pretty_print=True, encoding=xml_encoding, xml_declaration=True)
        # Call "xmllint" system commands to format XML
        os.system(f"xmllint --format {dst_xml_path} -o {dst_xml_path}")
        # Set the indent if destination xml file as 4 space
        set_xml_indent.set_xml_indent(dst_xml_path, xml_encoding)
        # Synchronize XML declaration
        sync_declaration.sync_declaration(sample_xml_path, dst_xml_path, xml_encoding)
        # Synchronize last blank lines(if exists)
        sync_empty_lines.sync_empty_lines(sample_xml_path, dst_xml_path, xml_encoding)

    print("---------------------------------------")
    return dst_xml_stat

if __name__ == '__main__':
    sync_all("../../resource/sync_value.txt", "../../resource/test1.xml", "../../resource/test2.xml")
