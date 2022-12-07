def parse_output(path):
    """Given the input, we can actually ignore ls commands and directory names that result from
    those ls commands. All we need to know is what directory we are currently in and what files
    are contained in that directory.

    Ultimately, we want to parse the input into a dictionary where the key is the full path to a
    specific directory and the value is a dictionary that contains any files (with their sizes)
    within the directory and the full path to the parent directory.
    """
    directories = {}
    # we'll track the present working directory with a list -- moving down a level appends to 
    # the list, moving up a level removes the last entry in the list
    pwd = []
    with open(path, 'r') as f: 
        for line in f.readlines():
            line_parts = line.strip().split(' ')
            # commands -- the only commands we're interested in are the "cd" commands, just
            # ignore any "ls"
            if (line_parts[0] == '$'):
                if (line_parts[1] == 'cd'):
                    # if we move up one level, we just change the pwd
                    if (line_parts[2] == '..'):
                        pwd = pwd[:-1]
                    # otherwise we create a new directory if it doesn't already
                    # exist, then we change the pwd
                    else:
                        new_pwd = '/'.join([*pwd, line_parts[2]])
                        if new_pwd not in directories:
                            directories[new_pwd] = {
                                'files': [],
                                'parent': '/'.join(pwd)
                            }
                        pwd.append(line_parts[2])
            # dir contents -- ignore any directories listed as children and just append any
            # files, along with their size
            if (line_parts[0][0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
                directories['/'.join(pwd)]['files'].append((line_parts[1], int(line_parts[0]),))
    return directories

def directory_size(dir_name, directories):
    """Use recursion to get the size of a given directory."""
    # first sum the sizes of any files in the directory
    files = sum([f[1] for f in directories[dir_name]['files']])
    # then sum the size of any directory where the current directory is the direct parent
    directories = sum([directory_size(name, directories) for name, d in directories.items() if d['parent'] == dir_name])
    return files + directories

def p1():
    directories = parse_output('input.txt')
    all_sizes = [directory_size(name, directories) for name, _ in directories.items()]
    return sum([s for s in all_sizes if s <= 100000])

def p2():
    directories = parse_output('input.txt')
    all_sizes = [directory_size(name, directories) for name, _ in directories.items()]
    # calculate existing space on the drive (total size is 70,000,000 per prompt)
    free_space = 70000000 - max(all_sizes)
    # update requires 30,000,000 to install (per prompt) so calculate how much we need
    space_needed = 30000000 - free_space
    # find smallest directory that is at least large enough to allow the update
    return min([s for s in all_sizes if s >= space_needed])
                
# print('Part 1: ', p1())
print('Part 2: ', p2())