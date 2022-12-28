import sys

# Read input
filename = sys.argv[0].split('.')[0] + '.in'
lines = open(filename).readlines()

pwd = '/' 
folders = {}
files   = {}
full_path = '/'
for line in lines:
    if line[0] == '$':
        # command
        line_cmd = line.split()
        command = line_cmd[1]
        if command == "cd":
            arg = line_cmd[2]
            if arg == "..":
                full_path = '/'.join(full_path.split('/')[:-1])
            elif arg == "/":
                full_path = '/'
            else:
                full_path = full_path + '/' + arg
                try:
                    if full_path not in folders[pwd]:
                        folders[pwd].append(full_path)
                except:
                    folders[pwd] = [full_path]
#            old_pwd = pwd
            pwd = full_path
        elif command == "ls":
            # ignore it
            pass
        else:
            print("WTF!!!")
    else:
        if "dir" == line[0:3]:
            # ignore it
            pass
        else:
            try:
                size, filename = line.split()
                size = int(size)
                try:
                    # asegurar que no repetimos
                    files[pwd].append([filename, size])
                except:
                    files[pwd] = [[filename, size]]
            except:
                print("WTF!!! size")


limit_size = 100000
res = 0
folders_size = {}
for _folder in files:
    folder_size = 0
    for _file in files[_folder]:
        filename, size = _file
        folder_size += size
    folders_size[_folder] = folder_size


def getRecursiveSize(_folder, total_size):
    if _folder not in folders:
        # leaf folder
        return folders_size[_folder]

    recursive_size = 0
    for __folder in folders[_folder]:
        recursive_size += getRecursiveSize(__folder, 0)

    try:
        folder_size = folders_size[_folder]
    except:
        # folders with no files were not addwd in the folders_size list
        folder_size = 0

    return folder_size + recursive_size

folders_recursive_size = {}
for _folder in folders:
    folders_recursive_size[_folder] = getRecursiveSize(_folder, 0)

for _folder in folders_size:
    if _folder not in folders_recursive_size:
        folders_recursive_size[_folder] = folders_size[_folder]

res = 0
for _folder in folders_recursive_size:
    size = folders_recursive_size[_folder]
    if size <= limit_size:
        res += size

disk_total = 70000000
disk_used = 0
disk_used = folders_recursive_size['/']
disk_free = disk_total - disk_used
disk_update = 30000000
disk_to_remove = disk_update - disk_free
#print('Total disk    ', disk_total)
#print('Total used    ', disk_used)
#print('Total free    ', disk_free)
#print('Disk to remove', disk_to_remove)

min_size = folders_recursive_size['/']
for _folder in folders_recursive_size:
    size = folders_recursive_size[_folder]
    if size >= disk_to_remove:
        if size < min_size:
            min_size = size

print('Part1',res)
print('Part2',min_size)
