import sys
import os
from synchronize import sync_all
import find_files

def main():
    # Get command line arguments
    args = sys.argv
    dst_xml_dirs = args[3:]

    files = find_files.find_files(args[2], dst_xml_dirs)
    
    dst_xmls_stat = sync_all.sync_all(args[1], args[2], files)

    count_succeed = dst_xmls_stat.count(1)
    count_fail = dst_xmls_stat.count(0)
    count_sample_fail = dst_xmls_stat.count(2)
    dst_xml_index = 0
    if count_sample_fail == 0:
        for file in files:
            if dst_xmls_stat[dst_xml_index] == 0:
                print("\033[31mFailed to synchronize file: " + file + "\033[0m")
            dst_xml_index += 1

    print("---------------------------------------")
    print(f"\033[32mTotally synchronized {count_succeed + count_fail} xml files, {count_succeed} succeeded,\033[0m \033[31m{count_fail} failed.\033[0m")

if __name__ == '__main__':
    main()
