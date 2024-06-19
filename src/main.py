import sys
import os
from synchronize import sync_all
import find_files

def main():
    # 获取命令行参数
    args = sys.argv
    dst_xml_dirs = args[3:]

    files = find_files.find_files(args[2], dst_xml_dirs)

    sync_all.sync_all(args[1], args[2], files)

    print(f"同步了{len(files)}个xml文件:")
    for file in files:
        print("同步文件" + file)

if __name__ == '__main__':
    main()
