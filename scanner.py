# this pyton file scans a folder and creates a txt file with the list of files path, date when created was and size



from pathlib import Path
import datetime
import utils.prettytable


from prettytable import PrettyTable

path = Path('/home/csurlee/Desktop')
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
