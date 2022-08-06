import os
from glob import glob
import shutil
from pathlib import Path


def filemover(folder_path:str, file_ext:str, new_folder:str):
    """

    :param new_folder: Name of new folder to move files to
    :param file_ext: extension of file to move e.g csv, json
    :param folder_path: Path to the parent folder containing files to move
    :return:
    """
    assert os.path.exists(Path(folder_path)), f'\033[1;36;40m Please provide a valid \033[1;34;40m folder path'
    parent_folder = os.path.dirname(Path(folder_path))
    print(parent_folder)
    n_folder = os.path.join(parent_folder, new_folder)
    if not os.path.isdir(n_folder):
        os.mkdir(n_folder)
    else:
        print(f'{n_folder} is an existing path choose a different folder name')
    files_to_move = glob(os.path.join(folder_path, f'*{file_ext}'))
    # print(files_to_move)
    i = 0
    for f in files_to_move:
        shutil.move(f, n_folder)
        i += 1
        if not i % 5 ==0:
            pass
        else:
            print(f'\033[1;34;40m {i} json files have been moved')

    print(f'\033[1;34;40m {i} JSON FILES WERE MOVED')


if __name__ == "__main__":
    folder_path = '/home/iamshri/PycharmProjects/ormedian-utils/tests/testImages'
    f_e ='json'
    n_f = 'json_folder'
    filemover(folder_path, f_e, n_f)
