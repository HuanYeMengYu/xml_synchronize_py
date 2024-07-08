def sync_declaration(file1_path, file2_path):
    # 读取第一个文件的第一行内容
    with open(file1_path, 'r', encoding='utf-8') as file1:
        first_line_file1 = file1.readline().strip()  # 读取并去除首尾空白字符

    # 读取第二个文件的所有内容
    with open(file2_path, 'r', encoding='utf-8') as file2:
        lines_file2 = file2.readlines()

    # 如果第二个文件有内容，则替换第一行
    if lines_file2:
        lines_file2[0] = first_line_file1 + '\n'

        # 写入替换后的内容回第二个文件
        with open(file2_path, 'w', encoding='utf-8') as file2:
            file2.writelines(lines_file2)
