import time

from PIL import Image
import os
from pathlib import Path
import matplotlib.image as mpimg
import cv2


def image_resizer(new_size: tuple,
            image_path: str,
            quality: int, n_f=True, new_folder = 'ResizedImages',
            view=True, out_format='jpg'):
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
    n_folder = ""
    img_ext = ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.psd', '.pdf', '.eps', '.raw', '.svg', '.bmp', '.dib']
    i = 0
    img_dirs = os.listdir(image_path)
    total_img_len = len([x for x in os.listdir(image_path) if Path(x).suffix in img_ext])
    print(f' \033[3;31;40m {total_img_len} total Images found in \033[1;34;40m {image_path}\n')
    time.sleep(0.5)
    for img in img_dirs:
        img_e = Path(img).suffix
        new_path = os.path.join(image_path, img)

        if img_e not in img_ext:
            print(f'\033[1;31;40m {img} Skipped! not a supported image file '

                  )
            pass
        else:
            if not os.path.isfile(new_path):
                return
            imgs = Image.open(new_path)

            f, e = os.path.splitext(new_path)
            Resized_img = imgs.resize(new_size, Image.ANTIALIAS)
            print(f'\033[1;33;40m New size of {img}: {Resized_img.size[0]} x {Resized_img.size[1]}')

            # Check if user requested for new folder for resized images

            if not n_f:
                if out_format == 'jpg':
                    Resized_img.save(f + '.jpg', 'JPEG', quality=quality)
                else:
                    Resized_img.save(f + '.png', 'PNG', quality=quality)
                if not view:
                    pass
                Resized_img.show(new_folder)
                i += 1

            else:
                image_path = Path(image_path)
                n_folder = os.path.join(image_path.parent, new_folder)
                if not os.path.exists(n_folder):
                    os.mkdir(n_folder)

                if out_format == 'jpg':
                    Resized_img.save(f'{n_folder}/{img}', 'JPEG', quality=quality)
                else:
                    Resized_img.save(f'{n_folder}/{img}', 'PNG', quality=quality)

                i += 1
                if not view:
                    pass

                # Visualize the image output
                image = mpimg.imread(f'{n_folder}/{img}')
                cv2.namedWindow(f'{img}')
                cv2.imshow(f'{img}', cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                cv2.waitKey(200)
        if i == total_img_len:
            break

        cv2.destroyAllWindows()

    print(f'\033[1;33;40m========================================================\n')
    print(f'\033[1;36;40m Resizing Image done!')
    print(f' {i} images have been resized to size: \033[2;32;40m {new_size} ')
    print(f' with Image extension \033[3;31;40m{out_format}\n')
    print(f'\033[1;36;40m RESIZED IMAGES can be found in \033[1;34;40m {n_folder}')

    print(f'\033[1;33;40m========================================================\n')
image_resizer((50, 50), '/home/iamshri/Datasets/sub_resizedImages', 'Resizedsub', quality=100 )
