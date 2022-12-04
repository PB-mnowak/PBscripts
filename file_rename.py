from os import listdir, getcwd, system, path


def rename(mypath=None, old_pattern=None, new_pattern=None, count=0, /):

    if mypath is None:
        mypath = input('Directory: ')
        if not mypath:
            mypath = getcwd()
    if old_pattern is None:        
        old_pattern = input('Find: ')
    if new_pattern is None:
        new_pattern = input('Replace with: ')

    files = listdir(mypath)

    for name in files:
        if path.isfile(path.join(mypath, name)):
            if old_pattern in name:
                try:
                    new_name = name.replace(old_pattern, new_pattern)
                    command = f'ren "{path.join(mypath, name)}" "{new_name}"'
                    system(command)
                    count += 1
                except Exception as e:
                    print(f'File: {name}')
                    print(e)
        else:
            count += rename(path.join(mypath, name), old_pattern, new_pattern, count)

    return count

if __name__ == '__main__':
    total_count = rename()
    print(f'{total_count} changes made')