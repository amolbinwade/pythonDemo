import os
from pathlib import Path

file_dir_in_root = []
file_list_in_root = []
all_files = []
selected_files = []
selected_dirs = []
file_list_in_sel_dirs = []
envs = []
selected_envs = []
file_list_in_selected_envs = []
config_options = []
selected_config_options = []
rootpath = ""
fileName = ""


class UpdateItem:
    ADD = "ADD"
    configPath = None
    action = None
    possible_values = []

    def __init__(self, action, config_path, possible_values):
        self.action = action
        self.configPath = config_path
        self.possible_values = possible_values

    @staticmethod
    def fetch_possible_value_from_file(filepath):
        file = Path(filepath)
        if file.is_file():
            value = open(str(p), 'r').read()
        return value

    @staticmethod
    def fetch_possible_values_from_files(self, root_path, file_name_filter):
        possible_values = []
        loc = Path(root_path)
        for p in loc.iterdir():
            if p.is_file():
                if p.name.startswith(file_name_filter):
                    value = self.fetch_possible_value_from_file(self, p)
                    if value:
                        possible_values.append(value)
        return possible_values


def get_root_path():
    options = fetch_root_options()
    if options.__len__() > 0:
        print("Below frequently used root directory paths have been found. "
              "Please select if you want to use one of these:")
        count = 1
        for o in options:
            if o.__len__() > 0:
                print(str(count) + '. ' + o)
                count +=1
        selected = input("Enter number of the root path which you want to use. "
                     "Or if you want to specify some other path then type N: ")
        if selected != 'N' and selected != 'n':
            return options[int(selected)-1]
    path = input("Please enter root directory path:")
    check_input_exit(path)
    populate_root_dir_options(path)
    return path


def load_files_in_root_path(path):
    global fileName
    loc = Path(path)
    for p in loc.iterdir():
        if p.is_file():
            if p.name.startswith(fileName):
                file_list_in_root.append(p)


def load_dirs_in_root_path(path):
    global fileName
    loc = Path(path)
    for p in loc.iterdir():
        if p.is_dir():
            file_dir_in_root.append(p)


def load_all_files_in_path(path, load_into):
    global fileName
    loc = Path(path)
    for p in loc.iterdir():
        if p.is_file():
            if p.name.startswith(fileName):
                load_into.append(p)
        elif p.is_dir():
            load_all_files_in_path(p, load_into)


def check_input_exit(val):
    if val == 'x' or val == 'X':
        exit("User ended program.")


def check_choice(inp):
    vals = str(inp).split(',')
    vals1 = []
    for i in vals:
        if 0 < int(i) < 100:
            vals1.append(int(i))
    return vals1


def print_choice(choice1, list1, selected_list):
    print("You have selected:")
    for k in choice1:
        print(str(k)+". "+str(list1[k-1]))
    lineSep()


def populate_selected_list(choice1, list1, selected_list):
    for k in choice1:
        selected_list.append(list1[k-1])


def get_file_to_process():
    filename = input("Please enter the filename you want to process. "
                     "For example input test* for updating test-dev.txt, test-dit2.txt, etc.")
    lineSep()
    print("You entered {} as file to process.".format(filename))
    if confirm():
        return filename
    else:
        return get_file_to_process()


def confirm():
    confirm1 = input("Enter Y to confirm or N to enter the input again:")
    lineSep()
    if confirm1 == 'Y' or confirm1 == 'y':
        return True
    elif confirm1 == 'N' or confirm1 == 'n':
        return False
    else:
        print("Invalid input.")
        return confirm()


def select_files():
    global selected_files
    print("Please select files from below to process.")
    count = 1
    for i in file_list_in_root:
        print(" "+str(count)+". "+str(i))
        count += 1

    print("(file numbers in comma separated values e.g. 1,5,4)")
    selected = input("Select files:")
    lineSep()
    choice = check_choice(selected)
    print("You selected files: " + selected)
    if confirm():
        print_choice(choice, file_list_in_root, selected_files)
        populate_selected_list(choice, file_list_in_root, selected_dirs)
    else:
        select_files()


def select_directories():
    global selected_dirs
    print("Please select directories/regions from below options to process.")
    count = 1
    for i in file_dir_in_root:
        print(" "+str(count)+". "+str(i))
        count += 1
    print("(directory numbers in comma separated values e.g. 1,5,4)")
    selected = input("Select directories:")
    lineSep()
    choice = check_choice(selected)
    print("You selected directories: " + selected)
    if confirm():
        print_choice(choice, file_dir_in_root, selected_dirs)
        populate_selected_list(choice, file_dir_in_root, selected_dirs)
    else:
        select_directories()


def select_envs():
    print("Please select for which environments the file {} to be updated.".format(fileName))
    count = 1
    for i in envs:
        print(" "+str(count)+". "+str(i))
        count += 1
    print("(environment numbers in comma separated values e.g. 1,5,4)")
    selected = input("Select environments:")
    lineSep()
    choice = check_choice(selected)
    print("You selected environments: " + selected)
    if confirm():
        print_choice(choice, envs, selected_envs)
        populate_selected_list(choice, envs, selected_envs)
    else:
        select_envs()


def populate_files_in_sel_dirs():
    global fileName
    if selected_dirs.__len__() > 0:
        for dir in selected_dirs:
            loc = Path(dir)
            for p in loc.iterdir():
                if p.is_file():
                    if p.name.startswith(fileName):
                        file_list_in_sel_dirs.append(p)
                    elif p.is_dir():
                        load_all_files_in_path(p, file_list_in_sel_dirs)


def populate_files_after_env_filter():
    if selected_dirs.__len__() > 0:
        for dir in selected_dirs:
            loc = Path(dir)
            for p in loc.iterdir():
                if p.is_file():
                    if p.name.startswith(fileName):
                        for k in selected_envs:
                            if k in p.name:
                                file_list_in_selected_envs.append(p)
                    elif p.is_dir():
                        load_all_files_in_path(p, file_list_in_selected_envs)


def enter_to_proceed():
    feed = input("Please Enter any key to proceed:")
    print("...............................................")


def lineSep():
    print("...............................................")


def stepSep():
    print("===============================================")


def populate_root_dir_options(rootdir):
    f = open("roots.txt", "a+")
    f.write(rootdir+',')
    f.close()


def fetch_root_options():
    f = open("roots.txt", "r+")
    contents = f.read()
    vals = []
    if contents.__len__() > 0:
        vals = contents.split(',')
    f.close()
    return vals

def fetch_envs():
    global envs
    f = open("envs.txt","r")
    contents = f.read()
    if contents.__len__() > 0:
        envs = contents.split(',')
    f.close()


def fetch_config_update_option():

    config_options.append("Add new config element.")
    count = 1
    for i in config_options:
        print(" "+str(count)+". "+str(i))
        count += 1
    print("(Option numbers in comma separated values e.g. 1,2)")
    selected = input("Select options:")
    lineSep()
    choice = check_choice(selected)
    print("You selected config options: " + selected)
    if confirm():
        print_choice(choice, config_options, selected_config_options)
        populate_selected_list(choice, config_options, selected_config_options)
    else:
        select_envs()



# +++++++functions end here ++++++++++++++

#-------------- starting flow -------------
print("""+++++++++++Welcome to Config Updater+++++++++++
This script has below steps:
1. Enter root directory.
2. Enter file to be updated.
3. Select child directories/regions in which files to be updated.
4. Select environments for which config files to be updated. 
5. Select config update options:
    A. Add new config element
    
    A.1. Enter config element full path (CONFIG.XYZ.ABC)
    A.1. Select option to choose value:
        a. Select from pre-configured files
        b. Enter comma separated value options
6. Auto generate Report file.""")
lineSep()
enter_to_proceed()


# Step:1 get root directory path
stepSep()
print("Step 1: Enter root directory.")
stepSep()
lineSep()
rootpath = get_root_path()
print("You entered root directory path as:" + rootpath)
lineSep()

# get fileName to process
stepSep()
print("Step 2: Enter file to be updated.")
stepSep()
fileName = get_file_to_process()


# load files/directory names from root path
load_all_files_in_path(rootpath, all_files)
load_files_in_root_path(rootpath)
load_dirs_in_root_path(rootpath)
print("Searched the matching files for {} in all {} child directories. "
      "Found {} matching files.".format(fileName,file_dir_in_root.__len__(), all_files.__len__()))

enter_to_proceed()

# Step 3
stepSep()
print("Step 3: Select child directories/regions in which files to be updated.")
stepSep()
# select directories
select_directories()
# load files in selected directories
populate_files_in_sel_dirs()
print("Searched the matching files for {} in {} selected child directories. "
      "Found {} matching files.".format(fileName,selected_dirs.__len__(), file_list_in_sel_dirs.__len__()))
enter_to_proceed()

# Step 4
stepSep()
print("Step 4: Select environments for which config files to be updated.")
fetch_envs()
select_envs()
populate_files_after_env_filter()
print("Searched the matching files for {} for {} envs in {} selected child directories. "
      "Found {} matching files.".format(fileName, selected_envs, selected_dirs.__len__(), file_list_in_selected_envs.__len__()))
stepSep()

# Step 5
stepSep()
print("Step 5: Select config update option:")
fetch_config_update_option()
populate_config_options()


enter_to_proceed()



