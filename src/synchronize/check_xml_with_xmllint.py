import subprocess

def check_xml_with_xmllint(file_path):
    try:
        # Run the xmllint command
        result = subprocess.run(['xmllint', '--noout', file_path], capture_output=True, text=True)

        # Check return status
        if result.returncode != 0:
            with open('fail.txt', 'a') as file:
                file.write("---------------------------------------\n")
                file.write("Failed synchronizing xml file '{}'\n".format(file_path))
                file.write("The format of XML file '{}' doesn't meet the specifications!\n".format(file_path))
                file.write("The following is the parsing error output:\n")
                file.write("{}".format(result.stderr))
            # print("---------------------------------------")
            # print(f"Failed synchronizing xml file '{file_path}'")
            # print(f"The format of XML file '{file_path}' doesn't meet the specifications!")
            # print("The following is the parsing error output:")
            # print(f"{result.stderr}")
            return 0
        return 1
    except FileNotFoundError:
        print("\033[31mxmllint command not found. Please make sure xmllint is installed and in your PATH.\033[0m")
        return 0
