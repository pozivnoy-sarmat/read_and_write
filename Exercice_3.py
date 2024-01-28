import os
from pprint import pprint

current = os.getcwd()
folder = 'texts'
file_1 = '1.txt'
file_2 = '2.txt'
file_3 = '3.txt'
file_4 = 'layout.txt'

with open(os.path.join(current, file_1), encoding="utf-8") as file1, open(
        os.path.join(current, file_2), encoding="utf-8") as file2, open(
    os.path.join(current, file_3), encoding="utf-8") as file3, open(os.path.join(current, file_4),
                                                                    'w', encoding="utf-8") as new_file:
    files_info = {
        file1: [len(file1.readlines()), file_1],
        file2: [len(file2.readlines()), file_2],
        file3: [len(file3.readlines()), file_3]
    }

    sort_file = dict(sorted(files_info.items(), key=lambda item: item[1][0]))
    pprint(sort_file, sort_dicts=False)
    file1.seek(0)
    file2.seek(0)
    file3.seek(0)

    for keys, values in sort_file.items():
        new_file.writelines(f'{values[1]}\n')
        new_file.writelines(f'{values[0]}\n')
        for line in keys.readlines():
            new_file.writelines(f'{line}')
        new_file.writelines('\n')
