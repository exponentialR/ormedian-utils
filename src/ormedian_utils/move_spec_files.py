import os
import time
from glob import glob
import shutil
from pathlib import Path
from tqdm import tqdm
from colorama import Fore
from datetime import datetime

from .logger_config import animated_exit
from .save_frames import logger


def filemover(folder_path: str, file_ext: str, new_folder: str):
    """

    :param new_folder: Name of new folder to move files to
    :param file_ext: extension of file to move e.g csv, json
    :param folder_path: Path to the parent folder containing files to move
    :return:
    """
    if not os.path.exists(Path(folder_path)):
        logger.error(f'{folder_path} DOES NOT EXIST PLEASE PROVIDE A VALID FOLDER PATH ')
        exit()
    if file_ext[0] !=0:
        file_ext = f'.{file_ext}'
    else:
        pass
    file_list = [Path(x).suffix for x in os.listdir(folder_path)]
    if not file_ext in file_list:
        logger.exception(f'{folder_path} does not contain any {file_ext} file\n', exc_info=False)
        return

    parent_folder = os.path.dirname(Path(folder_path))  # parent directory of input folder
    n_folder = os.path.join(parent_folder, new_folder)  # path for files to move
    time.sleep(1.0)

    if not os.path.exists(n_folder):
        os.mkdir(n_folder)  # make directory for folder if not already existing
    else:
        logger.debug(f'{n_folder} IS AN EXISTING PATH')
        # animated_exit('CHANGING FOLDER NAME')
        new_folder_name = f'{new_folder}_{datetime.now().strftime("%H.%M.%S")}'
        n_folder = os.path.join(parent_folder, new_folder_name)
        os.mkdir(n_folder)
        animated_exit('CHANGING FOLDER NAME')
        logger.info(f'\nNEW_FOLDER NAME: {new_folder_name}')
    logger.info(f'YOUR FILES WILL BE MOVED to {n_folder}')
    files_to_move = glob(os.path.join(folder_path, f'*{file_ext}'))
    files_to_move = tqdm(files_to_move)

    i = 0
    for f in files_to_move:
        i += 1
        shutil.move(f, n_folder)
        time.sleep(.05)
        files_to_move.set_description(f'{i} {file_ext[1::]} files moved\n')

    msg_print = f'==========================================================================\n' \
                f'-------------------------MOVED FILE STATISTICS------------------------ \n' \
                f'--------------------------------------------------------------------------\n'
    f_moved = f'{file_ext[1::]}'
    msg_image_path = f'files were moved from:'
    fol_path = f'{folder_path}'
    image_folder_print = f'\n        to     {n_folder}                           \n'
    space_u = f'==========================================================================\n'
    total_msg = f'Total Number of Files moved:    '
    total_number = f'                                {i} '
    space_b = f'\n=========================================================================='

    print(Fore.CYAN, msg_print, end='')
    print(Fore.GREEN, f_moved, end='')
    print(Fore.LIGHTWHITE_EX, msg_image_path, end='')
    print(Fore.RED, fol_path)
    print(Fore.RED, image_folder_print, end='')
    print(Fore.CYAN, space_u, end='')
    print(Fore.GREEN, total_msg, end='')
    print(Fore.RED, total_number, end='')
    print(Fore.CYAN, space_b)


# filemover('/Users/solua1/Documents/D', 'pdf', 'MovedFiles')
