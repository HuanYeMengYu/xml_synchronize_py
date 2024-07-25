import subprocess

def check_xml_with_xmllint(file_path):
    try:
        # Run the xmllint command
        result = subprocess.run(['xmllint', '--noout', file_path], capture_output=True, text=True)

        # Check return status
        if result.returncode != 0:
            print("----------------------------------------")
            print(f"{file_path} format doesn't meet the specifications!")
            print("The following is the error output:")
            print(f"{result.stderr}")
            print("----------------------------------------")
            return 0
        return 1
    except FileNotFoundError:
        print("xmllint command not found. Please make sure xmllint is installed and in your PATH.")
        return 0
