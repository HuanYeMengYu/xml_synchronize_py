import os

def find_files(sample_file_path, directory_paths):
    # 获取样本文件名
    sample_file_name = os.path.basename(sample_file_path)
    
    # 存储结果的列表
    result_files = []

    # 遍历每个目录
    for directory_path in directory_paths:
        # 遍历目录及其子目录
        for root, dirs, files in os.walk(directory_path):
            # 检查当前目录中是否有与样本文件同名的文件
            for file in files:
                if file == sample_file_name:
                    # 将找到的文件路径添加到结果列表中
                    result_files.append(os.path.join(root, file))
    return result_files

if __name__ == '__main__':
    files = find_files("cell1.xml", "../../resource/benchmark/SmallCell", "../../resource/benchmark/MacroCell/MU1Peak2Avg")
    for file in files:
        print(file)
