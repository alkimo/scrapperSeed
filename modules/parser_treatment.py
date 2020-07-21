import sys
sys.path.append("..")
import constant
import os
from random import randint

def treat_cli_name(name):
    folder_name = constant.SCRIPT_PATH + name + '/searchResult/' + name + '/'
    random_value=name

    if(os.path.isdir(folder_name) == True):
        existing_name = constant.SCRIPT_PATH + name + '/searchResult/' + name + '/'
        while(folder_name == existing_name):
            random_value=name + '-' + str(randint(100, 999))
            folder_name = constant.SCRIPT_PATH + name + '/searchResult/' + name + '-' + str(randint(100, 999)) + '/'
    return random_value