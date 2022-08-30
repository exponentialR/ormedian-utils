import os
import time
from glob import glob
import shutil
from pathlib import Path
from tqdm import tqdm


def filemover(folder_path: str, file_ext: str, new_folder: str):
    """

    :param new_folder: Name of new folder to move files to
    :param file_ext: extension of file to move e.g csv, json
    :param folder_path: Path to the parent folder containing files to move
    :return:
    """
    assert os.path.exists(Path(folder_path)), f'\033[1;36;40m Please provide a valid \033[1;34;40m folder path'
    file_list = [Path(x).suffix for x in os.listdir(folder_path)]
    if not file_ext in file_list:
        print(f'\033[1;36;40m{folder_path} \033[1;32;40mdoes not contain any \033[1;33;40m{file_ext} file\n')
        return

    parent_folder = os.path.dirname(Path(folder_path))  # parent directory of input folder
    n_folder = os.path.join(parent_folder, new_folder)  # path for files to move
    print(f'\033[1;36;40m Your files will be moved to \033[1;34;40m {n_folder}')
    time.sleep(1.0)

    if not os.path.exists(n_folder):
        os.mkdir(n_folder)  # make directory for folder if not already existing
    else:
        print(f'\033[1;39;41m {n_folder} is an existing path choose a different folder name')
        exit()
    files_to_move = glob(os.path.join(folder_path, f'*{file_ext}'))
    files_to_move = tqdm(files_to_move)

    i = 0
    for f in files_to_move:
        i += 1
        shutil.move(f, n_folder)
        time.sleep(.01)
        files_to_move.set_description(f'{i} {file_ext}s have been moved')

    print(f'\033[1;34;40m {i} {file_ext} FILES WERE MOVED')

# filemover('/Users/solua1/Documents/New_Image/New_Image', 'pdf', 'MovedFiles')