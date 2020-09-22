from typing import List, Optional


def get_data() -> List[Optional[List]]:
    data = []

    with open('data.txt', 'r') as f:
        while line := f.readline():
            number, interval = line.split()
            data.append([number, interval])

    return data
