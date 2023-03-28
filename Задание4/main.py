def read_files():
    list_of_files = ['1.txt', '2.txt', '3.txt']
    strings_from_files = []
    for file in list_of_files:
        with open(file, 'r', encoding='utf-8') as f:
            info_and_strings = []
            for line in f:
                info_and_strings.append(line.strip())
            info_and_strings.insert(0, str(len(info_and_strings)))
            info_and_strings.insert(0, file)
            strings_from_files.append(info_and_strings)
    strings_from_files.sort(key=len)
    sum_file = 'total.txt'
    with open(sum_file, 'w', encoding='utf-8') as file:
        for string in strings_from_files:
            for _ in string:
                file.writelines(_ + '\n')
    return


print(read_files())
