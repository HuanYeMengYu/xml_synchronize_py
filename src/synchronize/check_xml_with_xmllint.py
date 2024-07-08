import subprocess

def check_xml_with_xmllint(file_path):
    try:
        # 运行 xmllint 命令
        result = subprocess.run(['xmllint', '--noout', file_path], capture_output=True, text=True)

        # 检查返回状态
        if result.returncode != 0:
            print(f"{file_path} 的格式不符合规范!")
            print(f"错误输出: {result.stderr}")
            return 0
        return 1
    except FileNotFoundError:
        print("xmllint command not found. Please make sure xmllint is installed and in your PATH.")
        return 0
