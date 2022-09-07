import time

import cv2
import os
from pathlib import Path

from colorama import Fore

from .logger_config import animated_exit
from .save_frames import logger


def resizer(new_size,
            image_path,
            img_ext, new_folder, img_cnt):
    img_dirs = os.listdir(image_path)
    total_img_len = len([x for x in os.listdir(image_path) if Path(x).suffix in img_ext])
    i = img_cnt
    for img in img_dirs:
        img_e = Path(img).suffix
        exact_image_path = os.path.join(image_path, img)

        if img_e not in img_ext:
            # print(f'\033[1;31;40m {img} Skipped! not a supported image file ')
            logger.debug(f'\033[1;31;40m {img} Skipped! not a supported image file ')
            pass
        else:
            if not os.path.isfile(exact_image_path):
                print(f'\033[1;31;40m {exact_image_path} Skipped! not a supported image file')
                pass
            imgs = cv2.imread(exact_image_path, cv2.IMREAD_UNCHANGED)

            Resized_img = cv2.resize(imgs, new_size)
            if i % 20 == 0:
                logger.info(f'{i} Images resized; New Size: {Resized_img.shape[0]} x {Resized_img.shape[1]}')
                # print(f'\033[1;33;40m New size of {img}: {Resized_img.size[0]} x {Resized_img.size[1]}')1
            else:
                pass

            if not os.path.exists(new_folder):
                os.mkdir(new_folder)
            image_file = os.path.join(new_folder, f'{i}.jpg')
            # print(image_file)
            cv2.imwrite(f'{image_file}', Resized_img)
            i += 1
            cv2.waitKey(1)
            if i == total_img_len or (cv2.waitKey(1) & 0xFF == 27):
                cv2.destroyAllWindows()
                break
            else:
                pass

    return i


def resize_all(new_size:tuple, folder_path:str):
    """
    Takes folder_path: a directory containing folders with images, resize and save the images into a single folder.
    Images resized are in form 1.jpg, 2.jpg .....n.jpg
    :param new_size: expected size of the new images, accepts only tuple e.g (100, 100)
    :param folder_path: Directory containing folders with images
    :return:
    """
    img_ext = ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.psd', '.eps', '.raw', '.svg', '.bmp', '.dib']
    # Path cleaning section ==> 1. Check if sub folders are directories
    # 2. create a dictionary to house folders and number of images they contain
    folders = [f.path for f in os.scandir(folder_path) if f.is_dir() and Path(f)]
    fold_with_img = {}
    total_img_len = 0
    for f in folders:
        fold_with_img[f] = 0

        for f_ in os.listdir(f):
            if Path(f_).suffix in img_ext:
                fold_with_img[f] += 1
                total_img_len += 1
            else:
                pass

    logger.debug(f'TOTAL IMAGES to RESIZE: {total_img_len}')
    msg_print = f'\n==========================================================================\n' \
                f'-------------------------FOLDER STATISTICS-------------------------------- \n' \
                f'--------------------------------------------------------------------------\n'
    folder_path_print = f'FOLDERS with IMAGES:\n'
    space_u = f'\n==========================================================================\n'
    #
    total_msg = f'Total Images in Sub Folders  : '
    total_number = f'               {total_img_len} '
    space_b = f'\n=========================================================================='

    print(Fore.LIGHTBLUE_EX, msg_print, end='')
    print(Fore.LIGHTBLUE_EX, folder_path_print, end='')
    for fold, d in fold_with_img.items():
        print(Fore.RED, f'                {fold} ', end='')
        print(Fore.GREEN, f'{d} Images')
    print(Fore.LIGHTBLUE_EX, space_u, end='')
    print(Fore.LIGHTBLUE_EX, total_msg, end='')
    print(Fore.GREEN, total_number, end='')
    print(Fore.LIGHTBLUE_EX, space_b)
    time.sleep(2.0)
    animated_exit('STARTING RESIZE')
    print('')

    path_dirname = os.listdir(folder_path)
    parent_name = Path(folder_path).parent
    img_count = 0
    Resized_folder = os.path.join(parent_name, 'Resized')
    # print(f'RESIZED FOLDER: {Resized_folder}')
    for folder in path_dirname:
        folder_resizer = os.path.join(folder_path, folder)
        if not os.path.isdir(folder_resizer):
            animated_exit(f'{folder_resizer} NOT A DIRECTORY, IGNORING')
            print('')
            pass
        else:
            logger.info(f'RESIZING IMAGES in {folder}')
            img_count = resizer(new_size, folder_resizer, img_ext, Resized_folder, img_count)
            img_count += 0
            print(f'{img_count} IMAGES RESIZED')
    #
    msg_print = f'\n==========================================================================\n' \
                f'-------------------------IMAGE  RESIZE  STATISTICS---------------------- \n' \
                f'--------------------------------------------------------------------------\n'
    folder_path_print = f'Resized Images Folder:\n'
    new_image_size = f'New Image Size:'

    space_u = f'\n==========================================================================\n'

    total_msg = f'Total Resized Images  : '
    total_number = f'             {img_count} '
    space_b = f'\n=========================================================================='
    print(Fore.LIGHTBLUE_EX, msg_print, end='')
    print(Fore.LIGHTBLUE_EX, folder_path_print, end='')
    # for fold in Resized_folder:
    #     print(Fore.RED, f'      {fold}')
    print(Fore.GREEN, f'                {Resized_folder}')
    print(Fore.LIGHTBLUE_EX, f'{new_image_size}', end='')
    print(Fore.YELLOW, new_size, end='')
    print(Fore.LIGHTBLUE_EX, space_u, end='')
    print(Fore.LIGHTBLUE_EX, total_msg, end='')
    print(Fore.YELLOW, total_number, end='')
    print(Fore.LIGHTBLUE_EX, space_b)
    cv2.destroyAllWindows()
    cv2.waitKey(1)


