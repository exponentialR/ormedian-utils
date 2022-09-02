import time

import os
from pathlib import Path
import cv2
from colorama import Fore

from .logger_config import animated_exit
from .save_frames import logger


def image_resizer(new_size: tuple,
                  image_path: str,
                  n_f=True, new_folder='ResizedImages',
                  view=True, multiple_folders=False):
    """
    :param multiple_folders: Set True if the image path contains multiple folders containing images
    :param view: if True, there would display window showing resized images
    :param new_size: New Image size e.g (224, 224)
    :param image_path: '/path/to/where/images/are
    :param new_folder: '/Specify/new/folder
    :param args: at the moment you can specify either jpg or png
    :return: New image resized to new_size
    """
    Resized_folder = ""
    img_ext = ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.psd', '.eps', '.raw', '.svg', '.bmp', '.dib']

    path_dirname = os.path.dirname(image_path)
    if n_f and not multiple_folders:
        total_img_len = len([x for x in os.listdir(image_path) if Path(x).suffix in img_ext])
        logger.critical(f'{total_img_len} total Images found in \033[1;34;40m {image_path}\n')
        time.sleep(0.5)
        Resized_folder = os.path.join(path_dirname, new_folder)
        if not os.path.exists(Resized_folder):
            os.mkdir(Resized_folder)
        image_path = Path(image_path)

        Resized_folder = os.path.join(path_dirname, new_folder)
        if not os.path.exists(Resized_folder):
            os.mkdir(Resized_folder)
        else:
            print('WARNING!!! IMAGE FOLDER ALREADY EXISTS, OVERRIDING')
            pass
        tot_img = resizer(new_size, image_path, img_ext, Resized_folder, view)
        logger.info('IMAGES RESIZE DONE!!!')
        animated_exit('COMPUTING STATS')

        msg_print = f'\n==========================================================================\n' \
                    f'-------------------------IMAGE  RESIZE  STATISTICS---------------------- \n' \
                    f'--------------------------------------------------------------------------\n'
        folder_path_print = f'Resized Images Folder:\n'
        new_image_size = f'New Image Size:'

        space_u = f'\n==========================================================================\n'

        total_msg = f'Total Resized Images  : '
        total_number = f'               {tot_img} '
        space_b = f'\n=========================================================================='
        print(Fore.LIGHTBLUE_EX, msg_print, end='')
        print(Fore.LIGHTBLUE_EX, folder_path_print, end='')
        # for new_fol in Resized_folder:
        print(Fore.RED, f'      {Resized_folder}')
        # print(Fore.RED, f'{Resized_folder}', end='')
        print(Fore.LIGHTBLUE_EX, new_image_size, end='')
        print(Fore.RED, new_size, end='')
        # print(Fore.LIGHTBLUE_EX, msg_image_path, end='')
        # print(Fore.MAGENTA, image_folder_print, end='')
        print(Fore.LIGHTBLUE_EX, space_u, end='')
        print(Fore.LIGHTBLUE_EX, total_msg, end='')
        print(Fore.RED, total_number, end='')
        print(Fore.LIGHTBLUE_EX, space_b)
        cv2.destroyAllWindows()
        cv2.waitKey(1)

        # tot_img = resizer(new_size, image_path, Resized_folder, view, )

    elif not n_f and not multiple_folders:

        total_img_len = len([x for x in os.listdir(image_path) if Path(x).suffix in img_ext])
        logger.critical(f'{total_img_len} total Images found in \033[1;34;40m {image_path}\n')
        time.sleep(0.5)

        Resized_folder = image_path

        tot_img = resizer(new_size, image_path, img_ext, Resized_folder, view)
        logger.info('IMAGES RESIZE DONE!!!')
        animated_exit('COMPUTING STATS')

        msg_print = f'\n==========================================================================\n' \
                    f'-------------------------IMAGE  RESIZE  STATISTICS---------------------- \n' \
                    f'--------------------------------------------------------------------------\n'
        folder_path_print = f'Resized Images Folder:\n'
        new_image_size = f'New Image Size:'

        space_u = f'\n==========================================================================\n'

        total_msg = f'Total Resized Images  : '
        total_number = f'               {tot_img} '
        space_b = f'\n=========================================================================='
        print(Fore.LIGHTBLUE_EX, msg_print, end='')
        print(Fore.LIGHTBLUE_EX, folder_path_print, end='')

        print(Fore.RED, f'      {Resized_folder}')
        # print(Fore.RED, f'{Resized_folder}', end='')
        print(Fore.LIGHTBLUE_EX, new_image_size, end='')
        print(Fore.RED, new_size, end='')
        # print(Fore.LIGHTBLUE_EX, msg_image_path, end='')
        # print(Fore.MAGENTA, image_folder_print, end='')
        print(Fore.LIGHTBLUE_EX, space_u, end='')
        print(Fore.LIGHTBLUE_EX, total_msg, end='')
        print(Fore.RED, total_number, end='')
        print(Fore.LIGHTBLUE_EX, space_b)
        cv2.destroyAllWindows()
        cv2.waitKey(1)

    elif not n_f and multiple_folders:
        image_subfolders = [f.path for f in os.scandir(image_path) if f.is_dir()]  # prints out paths/subfolders
        total_img_len = len([x for y in image_subfolders for x in os.listdir(y) if Path(x).suffix in img_ext])
        logger.warning(f'THIS WILL OVERWRITE IMAGES IN THE CURRENT FOLDERS')
        logger.critical(f'{total_img_len} total Images found in {(Fore.BLUE, image_path)}\n')

        Resized_folder = image_subfolders
        image_subfolders = [f.path for f in os.scandir(image_path) if f.is_dir()]  # prints out paths/subfolders

        list_indx = 0
        tot_img = 0
        for img_fold in image_subfolders:
            logger.critical(f'RESIZING {img_fold} FOLDER')
            logger.critical(f'SAVING RESIZED IMAGES into EXISTING folder {img_fold}')
            tot_img_ = resizer(new_size, img_fold, img_ext, img_fold, view)

            # tot_img_ = resizer(new_size, img_fold, img_fold, view, )
            time.sleep(0.5)
            list_indx += 1
            tot_img += tot_img_
            if list_indx >= len(image_subfolders):
                break
        logger.info('IMAGES RESIZE DONE!!!')
        animated_exit('COMPUTING STATS')

        msg_print = f'\n==========================================================================\n' \
                    f'-------------------------IMAGE  RESIZE  STATISTICS---------------------- \n' \
                    f'--------------------------------------------------------------------------\n'
        folder_path_print = f'Resized Images Folder:\n'
        new_image_size = f'New Image Size:'

        space_u = f'\n==========================================================================\n'

        total_msg = f'Total Resized Images  : '
        total_number = f'               {tot_img} '
        space_b = f'\n=========================================================================='
        print(Fore.LIGHTBLUE_EX, msg_print, end='')
        print(Fore.LIGHTBLUE_EX, folder_path_print, end='')
        # for new_fol in Resized_folder:
        for fold in Resized_folder:
            print(Fore.RED, f'      {fold}')
        # print(Fore.RED, f'{Resized_folder}', end='')
        print(Fore.LIGHTBLUE_EX, new_image_size, end='')
        print(Fore.RED, new_size, end='')
        # print(Fore.LIGHTBLUE_EX, msg_image_path, end='')
        # print(Fore.MAGENTA, image_folder_print, end='')
        print(Fore.LIGHTBLUE_EX, space_u, end='')
        print(Fore.LIGHTBLUE_EX, total_msg, end='')
        print(Fore.RED, total_number, end='')
        print(Fore.LIGHTBLUE_EX, space_b)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
    else:
        Resized_folder = os.path.join(path_dirname, new_folder)
        if not os.path.exists(Resized_folder):
            os.mkdir(Resized_folder)
        else:
            print(f'WARNING! {Resized_folder} ALREADY EXISTS, USING EXISTING FOLDER PRESS ESC TO STOP');
            time.sleep(2.0)
            if cv2.waitKey(1) & 0xFF == 27: exit()

        image_subfolders = [f.path for f in os.scandir(image_path) if f.is_dir()]  # prints out paths/subfolders
        total_img_len = len([x for y in image_subfolders for x in os.listdir(y) if Path(x).suffix in img_ext])
        logger.critical(f'{total_img_len} total Images found in \033[1;34;40m {image_path}\n')
        subfolder_names = [f.name for f in os.scandir(image_path) if f.is_dir()]  # outputs only the subfolder names

        list_indx = 0
        tot_img = 0
        Res_folders = []
        for img_fold in image_subfolders:
            logger.critical(f'NOW RESIZING {img_fold}')
            Resized_folder_ = os.path.join(Resized_folder, subfolder_names[list_indx])

            Res_folders.append(Resized_folder_)
            if not os.path.exists(Resized_folder_):
                os.mkdir(Resized_folder_)
            else:
                animated_exit(
                    f'IMAGE FOLDER ALREADY EXISTS,\n OVERRIDING EXISTING FILES IN {Resized_folder_}\n PRESS Esc to Exit');
                time.sleep(2.0)
                if cv2.waitKey(1) & 0xFF == 27:
                    break
                else:
                    pass
            logger.info(f'SAVING INTO {Resized_folder_} FOLDER')
            tot_img_ = resizer(new_size, img_fold, img_ext, Resized_folder_, view)

            # tot_img_ = resizer(new_size, img_fold, Resized_folder_, view, )
            list_indx += 1
            tot_img += tot_img_
            if list_indx >= len(image_subfolders):
                cv2.destroyAllWindows()
                cv2.waitKey(1)
                break
        Resized_folder = Res_folders
        logger.info('IMAGES RESIZE DONE!!!')
        animated_exit('COMPUTING STATS')

        msg_print = f'\n==========================================================================\n' \
                    f'-------------------------IMAGE  RESIZE  STATISTICS---------------------- \n' \
                    f'--------------------------------------------------------------------------\n'
        folder_path_print = f'Resized Images Folder:\n'
        new_image_size = f'New Image Size:'

        space_u = f'\n==========================================================================\n'

        total_msg = f'Total Resized Images  : '
        total_number = f'               {tot_img} '
        space_b = f'\n=========================================================================='
        print(Fore.LIGHTBLUE_EX, msg_print, end='')
        print(Fore.LIGHTBLUE_EX, folder_path_print, end='')
        # for new_fol in Resized_folder:
        for fold in Resized_folder:
            print(Fore.RED, f'      {fold}')
        # print(Fore.RED, f'{Resized_folder}', end='')
        print(Fore.LIGHTBLUE_EX, new_image_size, end='')
        print(Fore.RED, new_size, end='')
        # print(Fore.LIGHTBLUE_EX, msg_image_path, end='')
        # print(Fore.MAGENTA, image_folder_print, end='')
        print(Fore.LIGHTBLUE_EX, space_u, end='')
        print(Fore.LIGHTBLUE_EX, total_msg, end='')
        print(Fore.RED, total_number, end='')
        print(Fore.LIGHTBLUE_EX, space_b)
        cv2.destroyAllWindows()
        cv2.waitKey(1)


def resizer(new_size,
            image_path,
            img_ext, new_folder,
            view):
    img_dirs = os.listdir(image_path)
    # img_extend = [x for x in os.listdir(image_path) if Path(x).suffix in img_ext]
    total_img_len = len([x for x in os.listdir(image_path) if Path(x).suffix in img_ext])
    i = 0
    for img in img_dirs:
        img_e = Path(img).suffix
        exact_image_path = os.path.join(image_path, img)

        if img_e not in img_ext:
            print(f'\033[1;31;40m {img} Skipped! not a supported image file ')
            pass
        else:
            if not os.path.isfile(exact_image_path):
                print(f'\033[1;31;40m {exact_image_path} Skipped! not a supported image file')
                pass
            # imgs = Image.open(exact_image_path)
            imgs = cv2.imread(exact_image_path, cv2.IMREAD_UNCHANGED)
            # Resized_img = imgs.resize(new_size, Image.ANTIALIAS)
            # print(f'Exact Image Path {exact_image_path}')
            Resized_img = cv2.resize(imgs, new_size)
            if i % 20 == 0:
                logger.info(f'{i} Images resized; New Size: {Resized_img.shape[0]} x {Resized_img.shape[1]}')
                # print(f'\033[1;33;40m New size of {img}: {Resized_img.size[0]} x {Resized_img.size[1]}')1
            else:
                pass
            image_path = Path(image_path)
            n_folder = os.path.join(image_path.parent, new_folder)

            if not os.path.exists(n_folder):
                os.mkdir(n_folder)
            cv2.imwrite(f'{os.path.join(n_folder, img)}', Resized_img)
            if view == False:
                pass
            else:
                cv2.imshow('Resizing Image', Resized_img)  # cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                i += 1
                cv2.waitKey(1)
                if i == total_img_len or (cv2.waitKey(1) & 0xFF == 27):
                    cv2.destroyAllWindows()
                    break
                else:
                    pass
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    return i


# images_folder = '/Users/solua1/Documents/Friday'
# # images_folder = '/Users/solua1/Documents/Datasets/files'
# # images_folder = '/Users/solua1/Documents/Datasets/3'
# image_resizer((200, 200), images_folder, n_f=True, new_folder='TesteFr', view=True, multiple_folders=True)
# print(images_folder[0:-4])
