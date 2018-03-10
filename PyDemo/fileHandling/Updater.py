import os
from pathlib import Path

file_dir_in_root = []
file_list_in_root = []
rootpath = ""
fileName = ""

def get_root_path():
    path = input("Please enter root folder path:")
    check_input_exit(path)
    return path


def load_files_in_path(path):
    loc = Path(path)
    for p in loc.iterdir():
        if p.is_file():
            file_list_in_root.append(p)
        elif p.is_dir():
            file_dir_in_root.append(p)


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


def print_choice(choice1, list1):
    print("You have selected:")
    for k in choice1:
        print(str(k)+". "+str(list1[k-1]))


def get_file_to_process():
    filename = input("Which file you need to process?")
    print("You entered {} as file to process.".format(filename))
    if confirm():
        return filename
    else:
        get_file_to_process()


def confirm():
    confirm1 = input("Is this input correct? Enter Y to confirm N to enter input again:")
    if confirm1 == 'Y' or confirm1 == 'y':
        return True
    elif confirm1 == 'N' or confirm1 == 'n':
        return False
    else:
        print("Invalid input.")
        return confirm()


# get root directory path
rootpath = get_root_path()
print(rootpath)

# get fileName to process
fileName = get_file_to_process()


# load files/directory names from root path
load_files_in_path(rootpath)
print("Root directory {} has {} files and {} directories".format(rootpath,file_list_in_root.__len__(),
                                                                 file_list_in_root.__len__()))
feed = input("Please Enter any key to proceed:")

# select files
print("Please select files from below to process.")
print("Enter file numbers in comma separated values e.g. 1,5,4")
count = 1
for i in file_list_in_root:
    print(" "+str(count)+". "+str(i))
    count += 1

selectedFiles = input("Selected files:")
choice = check_choice(selectedFiles)
print("You selected files: " + selectedFiles)
confirm = input("Enter Y to confirm or N to select files again:")

if confirm == 'Y' or confirm == 'y':
    print_choice(choice, file_list_in_root)