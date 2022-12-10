import os


def execute(command):
    ret = os.system(command)
    if ret == 0:
        print('Command execution successfully')
    else:
        print('Command execution error')
        exit(1)


def change_work_path(path):
    os.chdir(path)


def get_work_path():
    os.getcwd()


def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
