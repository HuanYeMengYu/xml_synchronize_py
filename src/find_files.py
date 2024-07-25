import os

def find_files(sample_file_path, directory_paths):
    # Get sample file name
    sample_file_name = os.path.basename(sample_file_path)

    # Stores the result file list
    result_files = []

    # Traverse each directory
    for directory_path in directory_paths:
        # Traverse a directory and its subdirectories
        for root, dirs, files in os.walk(directory_path):
            # Check if there is a file with the same name as the sample file in the current directory
            for file in files:
                if file == sample_file_name:
                    # Add the found file path to the result list
                    result_files.append(os.path.join(root, file))
    return result_files

if __name__ == '__main__':
    paths = ["../resource/benchmark/HTOFF_todo/"]
    files = find_files("cell1.xml", paths)
    print("--------------------------------")
    for file in files:
        print(file)
