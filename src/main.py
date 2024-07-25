import sys
import os
from synchronize import sync_all
import find_files

def main():
    # Get command line arguments
    args = sys.argv
    dst_xml_dirs = args[3:]

    files = find_files.find_files(args[2], dst_xml_dirs)

    dst_xml_stat = sync_all.sync_all(args[1], args[2], files)

    count_succeed = dst_xml_stat.count(1)
    dst_xml_index = 0
    if count_succeed != 0:
        print(f"Successfully synchronized {count_succeed} xml files:")
        for file in files:
            if dst_xml_stat[dst_xml_index] == 1:
                print("Successfully synchronized file: " + file)
            dst_xml_index += 1

if __name__ == '__main__':
    main()
