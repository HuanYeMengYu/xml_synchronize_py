def get_sync_elems(sync_elems_path):
    with open(sync_elems_path, 'r') as file:
        words = [line.strip() for line in file]
    return words

if __name__ == '__main__':
    words = get_sync_elems("../../resource/sync_value.txt")
    print(words)
    for word in words:
        print(word)