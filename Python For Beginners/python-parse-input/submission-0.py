from typing import List

def read_integers() -> List[int]:
    line = input()
    strings = line.split(",")
    int_list = []

    for s in strings:
        int_list.append(int(s))

    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
