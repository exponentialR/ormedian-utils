import time

from PIL import Image
import os
from pathlib import Path
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
from colorama import Fore

from .logger_config import animated_exit
from .save_frames import logger


def image_resizer(new_size: tuple,
                  image_path: str,
                  quality: int, n_f=True, new_folder='ResizedImages',
                  view=True, out_format='jpg', multiple_folders=False):
    """
    :param out_format: Specify the output image format
    :param view: if True, there would display window showing resized images
    :param new_size: New Image size e.g (224, 224)
    :param image_path: '/path/to/where/images/are
    :param new_folder: '/Specify/new/folder
    :param quality: The quality of the picture resized
    :param args: at the moment you can specify either jpg or png
    :return: New image resized to new_size
    """
    Resized_folder = ""
    img_ext = ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.psd', '.pdf', '.eps', '.raw', '.svg', '.bmp', '.dib']

    path_dirname = os.path.dirname(image_path)

    if n_f and not multiple_folders:
        total_img_len = len([x for x in os.listdir(image_path) if Path(x).suffix in img_ext])
        print(f' \033[3;31;40m {total_img_len} total Images found in \033[1;34;40m {image_path}\n')
        time.sleep(0.5)
        Resized_folder = os.path.join(path_dirname, new_folder)
        if not os.path.exists(Resized_folder):
            os.mkdir(Resized_folder)
        image_path = Path(image_path)  # /Users/solua1/Documents/Datasets

        Resized_folder = os.path.join(path_dirname, new_folder)  # /Users/solua1/Documents/ResizedImages
        if not os.path.exists(Resized_folder):
            os.mkdir(Resized_folder)
        else:
            print('WARNING!!! IMAGE FOLDER ALREADY EXISTS, OVERRIDING')
            pass

        tot_img = resizer(new_size, image_path, quality, img_ext, Resized_folder, view, out_format)

    elif not n_f and not multiple_folders:

        total_img_len = len([x for x in os.listdir(image_path) if Path(x).suffix in img_ext])
        print(f' \033[3;31;40m {total_img_len} total Images found in \033[1;34;40m {image_path}\n')
        time.sleep(0.5)

        Resized_folder = image_path
        tot_img = resizer(new_size, image_path, quality, img_ext, Resized_folder, view, out_format)

    elif not n_f and multiple_folders:
        image_subfolders = [f.path for f in os.scandir(image_path) if f.is_dir()]  # prints out paths/subfolders
        total_img_len = len([x for y in image_subfolders for x in os.listdir(y) if Path(x).suffix in img_ext])
        print(f' \033[3;31;40m {total_img_len} total Images found in \033[1;34;40m {image_path}\n')
        print(f'WARNING! THIS WILL OVERWRITE IMAGES IN THE CURRENT FOLDERS')
        Resized_folder = image_subfolders
        image_subfolders = [f.path for f in os.scandir(image_path) if f.is_dir()]  # prints out paths/subfolders

        list_indx = 0
        tot_img = 0
        for img_fold in image_subfolders:
            # Resized_folder_ = os.path.join(Resized_folder, subfolder_names[list_indx])
            print(f'\033[1;34;40mSTARTING RESIZING OF {img_fold} FOLDER')

            tot_img_ = resizer(new_size, img_fold, quality, img_ext, img_fold, view, out_format)
            time.sleep(0.5)
            list_indx += 1
            tot_img += tot_img_
            if list_indx >= len(image_subfolders):
                break
    else:
        Resized_folder = os.path.join(path_dirname, new_folder)
        if not os.path.exists(Resized_folder):
            os.mkdir(Resized_folder)
        else:
            print(f'WARNING! {Resized_folder} ALREADY EXISTS, USING EXISTING FOLDER PRESS ESC TO STOP')

        image_subfolders = [f.path for f in os.scandir(image_path) if f.is_dir()]  # prints out paths/subfolders
        total_img_len = len([x for y in image_subfolders for x in os.listdir(y) if Path(x).suffix in img_ext])
        print(f' \033[3;31;40m {total_img_len} total Images found in \033[1;34;40m {image_path}\n')
        subfolder_names = [f.name for f in os.scandir(image_path) if f.is_dir()]  # outputs only the subfolder names

        list_indx = 0
        tot_img = 0
        Res_folders = []
        for img_fold in image_subfolders:

            Resized_folder_ = os.path.join(Resized_folder, subfolder_names[list_indx])
            Res_folders.append(Resized_folder_)
            if not os.path.exists(Resized_folder_):
                os.mkdir(Resized_folder_)
            else:
                animated_exit(
                    f'IMAGE FOLDER ALREADY EXISTS,\n OVERRIDING EXISTING FILES IN {Resized_folder_}\n PRESS Esc to Exit')
                if cv2.waitKey(45) & 0xFF == 27: exit()
                time.sleep(2.0)
                pass
            tot_img_ = resizer(new_size, img_fold, quality, img_ext, Resized_folder_, view, out_format)
            list_indx += 1
            tot_img += tot_img_
            if list_indx >= len(image_subfolders):
                cv2.destroyAllWindows()
                cv2.waitKey(1)
                break
        Resized_folder = Res_folders
    logger.info('IMAGE RESIZING DONE!!!')
    animated_exit('COMPUTING STATS')

    msg_print = f'\n==========================================================================\n' \
                f'-------------------------IMAGE  RESIZING  STATISTICS---------------------- \n' \
                f'--------------------------------------------------------------------------\n'
    folder_path_print = f'\nResized Images Folder:'
    new_image_size = f'\nNew Image Size:'

    msg_image_path = f'\n Resized Images Format:'
    image_folder_print = f'{out_format}                           \n'
    space_u = f'==========================================================================\n'

    total_msg = f'Total Resized Images  : '
    total_number = f'               {tot_img} '
    space_b = f'\n========================================================================='
    print(Fore.LIGHTBLUE_EX, msg_print, end='')
    print(Fore.LIGHTBLUE_EX, folder_path_print, end='')
    print(Fore.RED, f'{Resized_folder}', end='')
    print(Fore.LIGHTBLUE_EX, new_image_size, end='')
    print(Fore.RED, new_size, end='')
    print(Fore.LIGHTBLUE_EX, msg_image_path, end='')
    print(Fore.MAGENTA, image_folder_print, end='')
    print(Fore.LIGHTBLUE_EX, space_u, end='')
    print(Fore.LIGHTBLUE_EX, total_msg, end='')
    print(Fore.RED, total_number, end='')
    print(Fore.LIGHTBLUE_EX, space_b)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    # print(f'\033[1;33;40m========================================================================\n')
    # print(f'\033[1;36;40m Resizing Image done!')
    # print(f' {tot_img} images have been resized to size: \033[2;32;40m {new_size} ')
    # print(f' with Image extension \033[3;31;40m{out_format}\n')
    # print(f'\033[1;36;40m RESIZED IMAGES can be found in \033[1;34;40m {Resized_folder}')
    #
    # print(f'\033[1;33;40m=========================================================================\n')


def resizer(new_size,
            image_path,
            quality, img_ext, new_folder,
            view, out_format):
    img_dirs = os.listdir(image_path)
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
            imgs = Image.open(exact_image_path)

            Resized_img = imgs.resize(new_size, Image.ANTIALIAS)
            print(f'\033[1;33;40m New size of {img}: {Resized_img.size[0]} x {Resized_img.size[1]}')
            image_path = Path(image_path)
            n_folder = os.path.join(image_path.parent, new_folder)

            if not os.path.exists(n_folder):
                os.mkdir(n_folder)

            if out_format == 'jpg':
                Resized_img.save(os.path.join(n_folder, img), 'JPEG', quality=quality)
            else:
                Resized_img.save(os.path.join(n_folder, img), 'PNG', quality=quality)
            if view == False:
                pass
            else:
                # image = mpimg.imread(os.path.join(n_folder, img))
                image = cv2.imread(os.path.join(n_folder, img))

                # image = Image.open(os.path.join(n_folder, img))
                # plt.figure(1)
                # plt.imshow(image)
                # plt.title(f'Resized Image: {img}')
                # plt.pause(0.00000001)
                # if 0xFF == 27:
                #     plt.close('all')
                #     break
                cv2.namedWindow(f'{img}')
                # plt.imshow(image)
                # plt.show()
                cv2.imshow(f'{img}', image)  # cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                i += 1
                cv2.waitKey(2)

                if cv2.waitKey(1) & 0xFF == 27:
                    return i
                cv2.destroyAllWindows()
                cv2.waitKey(1)

            if i == total_img_len:

                cv2.destroyAllWindows()
                cv2.waitKey(1)
                return i
            else:
                pass
            cv2.destroyAllWindows()
            cv2.waitKey(1)
    #         break
    cv2.destroyAllWindows()


#
# images_folder = '/Users/solua1/Documents/Datasets'
# images_folder = '/Users/solua1/Documents/Datasets/3'
# image_resizer((200, 200),
#               images_folder,
#               100, multiple_folders=False, n_f=True, view=True, new_folder='Thursday')
