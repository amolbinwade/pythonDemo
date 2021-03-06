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
file_type = ''
update_items = []


class UpdateItem:
    ADD = "ADD"
    UPDATE = "UPDATE"
    # configPath = None
    # action = None
    # possible_values = []

    def __init__(self, action, config_path, possible_values):
        self.action = action
        self.configPath = config_path
        self.possible_values = possible_values

    @staticmethod
    def fetch_possible_value_from_file(filepath):
        file = Path(filepath)
        value = None
        if file.is_file():
            value = open(str(file), 'r').read()
        return value

    @staticmethod
    def fetch_possible_values_from_files(root_path, file_name_filter):
        possible_values = []
        loc = Path(root_path)
        for p in loc.iterdir():
            if p.is_file():
                if p.name.startswith(file_name_filter):
                    value = UpdateItem.fetch_possible_value_from_file(p)
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
                     "Or if you want to specify some other path then type N: "+"\n" + ">>")
        if selected != 'N' and selected != 'n':
            return options[int(selected)-1]
    path = input("Please enter root directory path:"+ "\n" +">>")
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


def check_choice(inp, max1):
    vals = str(inp).split(',')
    vals1 = []
    for i in vals:
        if 0 < int(i) < max1+1:
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
                     "For example input test for updating test-dev.txt, test-dit2.txt, etc." + "\n" +">>")
    lineSep()
    print("You entered {} as file to process.".format(filename))
    if confirm():
        return filename
    else:
        return get_file_to_process()


def get_file_type():
    file_type_a = input("Please enter the file type you want to process. "
                     "For example input xml or properties" + "\n" +">>")
    lineSep()
    print("You entered {} as file type to process.".format(file_type_a))
    if confirm():
        return file_type_a
    else:
        return get_file_type()

def confirm():
    confirm1 = input("Enter Y to confirm or N to enter the input again:"+"\n"+">>")
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
    selected = input("Select files:"+ "\n" +">>")
    lineSep()
    choice = check_choice(selected, count)
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
    selected = input("Select directories:"+ "\n" +">>")
    lineSep()
    choice = check_choice(selected, count)
    print("You selected directories: " + selected)
    if confirm():
        print_choice(choice, file_dir_in_root, selected_dirs)
        populate_selected_list(choice, file_dir_in_root, selected_dirs)
    else:
        select_directories()


def select_envs():
    print("Please select for which environments the file {} to be updated.".format(fileName))
    count = 0

    while count < len(envs):
        env = ''
        for i in range(1, 5):
            if count < len(envs):
                env += "{}. {}{}".format(count+1, envs[count], '\t'*5)
                count += 1
        print(env)
    print("(environment numbers in comma separated values e.g. 1,5,4)")
    selected = input("Select environments:"+ "\n" +">>")
    lineSep()
    choice = check_choice(selected, count)
    print("You selected environments: " + selected)
    if confirm():
        print_choice(choice, envs, selected_envs)
        populate_selected_list(choice, envs, selected_envs)
    else:
        select_envs()


def select_config_value(values):
    print("Please select correct config value for current file.")
    count = 1
    for i in values:
        print(" "+str(count)+". "+str(i))
        count += 1
    print("(enter number of correct value.)")
    selected = input("Select Value:"+ "\n" +">>")
    lineSep()
    choice = check_choice(selected, count)
    print("You selected value: " + selected)
    if confirm():
        print_choice(choice, values, None)
        return values[choice[0]-1]
    else:
        select_config_value(values)


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
                            if k+'_' in p.name:
                                file_list_in_selected_envs.append(p)
                elif p.is_dir():
                        load_all_files_in_path(p, file_list_in_selected_envs)


def populate_files_after_env_filter_new():
    if selected_dirs.__len__() > 0:
        for dir1 in selected_dirs:
            populate_files_after_env_filter_from_dir(dir1)


def populate_files_after_env_filter_from_dir(dir1):
    loc = Path(dir1)
    for p in loc.iterdir():
        if p.is_file():
            if p.name.startswith(fileName):
                for k in selected_envs:
                    if k+'.' in p.name:
                        file_list_in_selected_envs.append(p)
        elif p.is_dir():
            populate_files_after_env_filter_from_dir(p)


def enter_to_proceed():
    feed = input("Please Enter any key to proceed:"+ "\n" +">>")
    print("...............................................")


def lineSep():
    print("...............................................")


def stepSep():
    print("===============================================")


def print_empty_lines():
    print('\n')
    print('\n')


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


def fetch_envs_new():
    global envs
    for i in file_list_in_sel_dirs:
        if i.name.startswith(fileName):
            start_index = i.name.find(fileName)
            str1 = i.name[start_index+len(fileName)+1:]
            end_index = str1.find(".")
            str2 = str1[:end_index]
            if not str2 in envs:
                envs.append(str2)


def fetch_config_update_option():
    print("Enter full path of configuration that need to be added/updated.")
    print("(E.g. config.xyz.abc)")
    config = input("Enter configuration name:"+ "\n" +">>")
    action = fetch_update_action(config)
    values = fetch_possible_values(config)
    update_item = UpdateItem(action, config, values)
    update_items.append(update_item)


def fetch_update_action(config):
    print("What needs to be done on {}".format(config))
    print("1. Add")
    print("2. Update")
    action = input("Enter option:"+ "\n" +">>")
    if action == '1':
        return UpdateItem.ADD
    elif action == '2':
        return UpdateItem.UPDATE
    else:
        print("Invalid selection")
        return fetch_update_action(config)


def fetch_possible_values(config):
    lineSep()
    print("How you want to enter possible values for {}".format(config))
    print("1. From pre-populated input files.")
    print("2. Enter comma separated value. ")
    action = input("Enter option:"+ "\n" +">>")
    lineSep()
    if action == '1':
        file_path = input("Enter root folder path for pre-populated input files"+ "\n" +">>")
        file_name = input("Enter file name filter (Starting characters of file name):"+ "\n" +">>")
        return UpdateItem.fetch_possible_values_from_files(file_path, file_name)
    elif action == '2':
        values = input("Enter comma separated possible values:"+ "\n" +">>")
        vals = values.split(',')
        return vals
    else:
        print("Invalid selection")
        return fetch_possible_values(config)


def filesep():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


def loop_for_files_update():
    count = 1
    for f in file_list_in_selected_envs:
        filesep()
        print("Currently Editing File: {}. [{}/{}]".format(f, count, len(file_list_in_selected_envs)))
        count += 1
        filesep()
        for c in update_items:
            print("Configuration Parameter: {}".format(c.configPath))
            selected_value = select_config_value(c.possible_values)
            update_file(f, c.configPath, c.action, selected_value)


def update_file(file, config_path, action, selected_value):
    if action == 'ADD':
        add_config(file, config_path, selected_value)
    else:
        act = 'Updated'


def add_config(file, config_path, selected_value):
    if file_type == 'xml':
        add_to_xml_file(file, config_path, selected_value)


def add_to_xml_file(file, config_path, selected_value):
    elements = str(config_path).split('.')
    current = 0
    update_open = False
    update_end = False
    update_done = False
    val = ''
    count = len(elements)
    f = open(file, 'r')
    new_file = open(file+'n', 'w')
    for line in f.readlines():
        if not update_open:
            if line.__contains__('<' + elements[current]):
                current += 1
                if current == (count):
                    update_open = True
                    start_index = line.find('<'+elements[current-1]+'>')
                    val = line[0:start_index] + '<'+elements[current-1]+'>' + '\n'+'\t'*count + selected_value + '\n'
                    # start_index = line.find('<'+elements[current-1]+'>')
                    # start_index = start_index + len('<'+elements[current-1]+'>')
                    if line.__contains__('</'+elements[current-1]+'>'):
                        start_index = line.find('</'+elements[current-1]+'>')
                        start_index1 = start_index + len('</'+elements[current-1]+'>')
                        val = val + '\n'+ '</'+elements[current-1]+'>'
                        val = val + line[start_index1:len(line)]
                        update_end = True
        if update_open and not update_end:
            if line.__contains__('</'+elements[current-1]+'>'):
                val = val +line[0:start_index]+ '</'+elements[current-1]+'>'
                start_index = line.find('</'+elements[current-1]+'>')
                start_index = start_index + len('</'+elements[current-1]+'>')
                val = val + line[start_index:len(line)]
                update_end = True
        if not update_open:
            new_file.write(line)
        elif update_open and update_end and not update_done:
            new_file.write(val)
            update_done = True
        elif update_done:
            new_file.write(line)
    f.close()
    new_file.close()

    print('Added config {} with value {} to file {}'.format(config_path, selected_value, file))

# +++++++functions end here ++++++++++++++


add_to_xml_file('/home/amol/temp/configs/APAC/fragments/config-file_dev1.txt', 'config.test.rest', 'wow')