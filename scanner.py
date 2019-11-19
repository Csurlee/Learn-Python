#!/usr/bin/python3.6

from pathlib import Path
import datetime
from prettytable import PrettyTable

path = Path('/Dev/python3/python3_the_hard_way/Python')
print(path)
path_list= Path('list.txt')

pt = PrettyTable()
pt.field_names = ["Files", "Size (byte)", "Created"]

pt.align["Files"] = "l"
pt.align["Size (byte)"] = "r"
pt.align["Created"] = "l"

for e in path.glob('**/*.*'):   # AZ UTOLSO * A FILE TIPUSA (pl .pdf .txt)
    directory = e.as_posix()
    created = datetime.datetime.fromtimestamp(e.stat().st_ctime)
    size = e.stat().st_size
    pt.add_row([directory, size, f"{created:%d-%m-%Y}"])


with open(path_list,'w') as file:
    file.write(str(pt))
print(pt)
