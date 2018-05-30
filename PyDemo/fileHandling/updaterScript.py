import os
from pathlib import Path
import fileHandling.updater as up

#-------------- starting flow -------------
up.print_empty_lines()
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

up.lineSep()
up.print_empty_lines()
up.enter_to_proceed()

# fetch_config_update_option()
# Step:1 get root directory path
up.stepSep()
print("Step 1: Enter root directory.")
up.stepSep()
up.lineSep()
up.rootpath = up.get_root_path()
print("You entered root directory path as:" + up.rootpath)
up.lineSep()
up.print_empty_lines()
# get fileName to process
up.stepSep()
print("Step 2: Enter file to be updated.")
up.stepSep()
up.fileName = up.get_file_to_process()


# load files/directory names from root path
up.load_all_files_in_path(up.rootpath, up.all_files)
up.load_files_in_root_path(up.rootpath)
up.load_dirs_in_root_path(up.rootpath)
print("Searched the matching files for {} in all {} child directories. "
      "Found {} matching files.".format(up.fileName, up.file_dir_in_root.__len__(), up.all_files.__len__()))

up.enter_to_proceed()
up.print_empty_lines()

# Step 3
up.stepSep()
print("Step 3: Select child directories/regions in which files to be updated.")
up.stepSep()
# select directories
up.select_directories()
# load files in selected directories
up.populate_files_in_sel_dirs()
print("Searched the matching files for {} in {} selected child directories. "
      "Found {} matching files.".format(up.fileName, up.selected_dirs.__len__(), up.file_list_in_sel_dirs.__len__()))
up.enter_to_proceed()
up.print_empty_lines()

# Step 4
# select_envs_new()
up.stepSep()
print("Step 4: Select environments for which config files to be updated.")
up.fetch_envs_new()
up.select_envs()
up.populate_files_after_env_filter_new()
print("Searched the matching files for {} for {} envs in {} selected child directories. "
      "Found {} matching files.".format(up.fileName, up.selected_envs, up.selected_dirs.__len__()
                                        , up.file_list_in_selected_envs.__len__()))
up.stepSep()
up.print_empty_lines()
# Step 5
up.stepSep()
print("Step 5: Select config update option:")
up.fetch_config_update_option()


up.enter_to_proceed()
up.print_empty_lines()
# Step 6 : Iterate over final file list and give option to update file

up.stepSep()
print("Step 6: File Modification Begins:")
up.loop_for_files_update()

