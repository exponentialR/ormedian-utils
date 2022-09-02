import json
import os.path
import re
from pathlib import Path
import cv2
from datetime import datetime
import logging
from tqdm import tqdm
from colorama import Fore

import time
from .logger_config import CustomFormatter, animated_exit

import datetime as dt

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Define format for logs
fmt = '%(asctime)s | %(levelname)8s | %(message)s'

# Create stdout handler for logging to the console (logs all five levels)
stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(CustomFormatter(fmt))

# Create file handler for logging to a file (logs all five levels)
today = dt.date.today()
file_handler = logging.FileHandler('my_app_{}.log'.format(today.strftime('%Y_%m_%d')))
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(fmt))

# Add both handlers to the logger
logger.addHandler(stdout_handler)
logger.addHandler(file_handler)


def frame_capture(file, image_format, new_folder, videos, view):
    frames_folder = os.path.join(new_folder, videos[0:-len(Path(videos).suffix)])
    if os.path.exists(frames_folder):
        pass
    else:
        os.mkdir(frames_folder)

    cap = cv2.VideoCapture(file)
    i = 0
    while True:
        ret, frame = cap.read()
        if ret:
            if view:
                cv2.imshow('Output Video', frame)
            else:
                pass
            cv2.imwrite(f'{frames_folder}/image_{i}.{image_format}', frame)
            i += 1
            if not i % 20 == 0:
                pass
            else:
                logger.info(f'Frames collected into {frames_folder} : {i}')
            if cv2.waitKey(1) & 0xFF == 27:
                logger.critical('EXITING FRAME COLLECTION.....');
                time.sleep(0.5)
                logger.critical(f'SUBTOTAL IMAGES SAVED: {i}')
                return i

        else:
            cap.release()
            cv2.destroyAllWindows()
            logger.critical(f'SUBTOTAL IMAGES SAVED for {file}: {i}')
            return i
        cv2.waitKey(1)
    cap.release
    cv2.destroyAllWindows()
    cv2.waitKey(1)


def save_video_frames(cap_input, folder, image_name, video_format, view):
    video_name = os.path.join(folder, image_name)
    if not os.path.exists(video_name):
        pass
    else:
        logger.error('Video name already exist, please choose a different name')
    # camera = cv2.VideoCapture(cv2.CAP_V4L2)
    camera = cv2.VideoCapture(cap_input)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    width, height = camera.get(cv2.CAP_PROP_FRAME_WIDTH), camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
    video_ = cv2.VideoWriter(f'{video_name}.{video_format}', fourcc, 20.0, (int(width), int(height)))

    i = 0
    while camera.isOpened():
        ret, frame = camera.read()
        if ret == True:
            frame = cv2.flip(frame, 1)
            video_.write(frame)
            cv2.imwrite(f'{video_name}_{i}.jpg', frame)

            if view:

                cv2.imshow(f'{video_name}', frame)
            else:
                pass
            if i % 20 == 0:
                logger.info(f'NUMBER OF IMAGES SAVED: {i}')
            else:
                pass
            i += 1

            # if cv2.waitKey(1) & 0xFF == ord('q'):
            if cv2.waitKey(1) & 0xFF == 27:
                camera.release()
                video_.release()
                cv2.destroyAllWindows()
                cv2.waitKey(1)
                animated_exit('EXITING FRAME COLLECTION')
                break
    msg_print = f'\n==========================================================================\n' \
                f'-------------------------SAVED FRAME STATISTICS------------------------ \n' \
                f'--------------------------------------------------------------------------\n'
    folder_path_print = f'Saved Video'' Path:'

    msg_image_path = f'\n Saved Images Folder:'
    image_folder_print = f'{folder}                           \n'
    space_u = f'==========================================================================\n'

    total_msg = f'Total Number of Images saved:    '
    total_number = f'                {i} '
    space_b = f'\n=========================================================================='
    print(Fore.LIGHTBLUE_EX, msg_print, end='')
    print(Fore.LIGHTBLUE_EX, folder_path_print, end='')
    print(Fore.RED, f'{video_name}{video_format}', end='')
    print(Fore.LIGHTBLUE_EX, msg_image_path, end='')
    print(Fore.MAGENTA, image_folder_print, end='')
    print(Fore.LIGHTBLUE_EX, space_u, end='')
    print(Fore.LIGHTBLUE_EX, total_msg, end='')
    print(Fore.RED, total_number, end='')
    print(Fore.LIGHTBLUE_EX, space_b)
    camera.release()
    video_.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)


def save_frames_only(cap_input, folder, image_name, image_format, view):
    video_name = os.path.join(folder, image_name)
    camera = cv2.VideoCapture(cap_input)
    i = 0
    while camera.isOpened():
        ret, frame = camera.read()
        if ret == True:
            frame = cv2.flip(frame, 1)
            cv2.imwrite(f'{video_name}_{i}.{image_format}', frame)
            if view:

                cv2.imshow(f'Output {image_name} Video', frame)
            else:
                pass
            if i % 20 == 0:
                logger.info(f'NUMBER OF IMAGES SAVED: {i}')
            else:
                pass
            i += 1

            if cv2.waitKey(1) & 0xFF == ord('q'):
                camera.release()
                cv2.destroyAllWindows()
                cv2.waitKey(1)
                animated_exit(f'EXITING FRAME COLLECTION')
                break

    msg_print = f'\n==========================================================================\n' \
                f'-------------------------SAVED FRAME STATISTICS------------------------ \n' \
                f'--------------------------------------------------------------------------\n'
    # folder_path_print = f'Saved Video'' Path:'

    msg_image_path = f'\n Saved Images Folder:'
    image_folder_print = f'{folder}                           \n'
    space_u = f'==========================================================================\n'

    total_msg = f'Total Number of Images saved:    '
    total_number = f'                {i} '
    space_b = f'\n=========================================================================='
    print(Fore.LIGHTBLUE_EX, msg_print, end='')
    print(Fore.LIGHTBLUE_EX, msg_image_path, end='')
    print(Fore.MAGENTA, image_folder_print, end='')
    print(Fore.LIGHTBLUE_EX, space_u, end='')
    print(Fore.LIGHTBLUE_EX, total_msg, end='')
    print(Fore.RED, total_number, end='')
    print(Fore.LIGHTBLUE_EX, space_b)
    camera.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)


class collect_frames:
    def __init__(self, num, video_format='mp4', image_name='frame', image_format='jpg', view=True):
        super(collect_frames, self).__init__()
        self.img_ext = ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.psd', '.pdf', '.eps', '.raw', '.svg', '.bmp',
                        '.dib']
        self.vid_ext = ['.avi', '.flv', '.mpg', '.mpeg', '.mpe', '.mpv', '.mp2', '.mp4', '.3gp', '.m4p', '.m4v', '.ogg',
                        '.webm', '.mov', '.wmv']
        # self.videos_path = videos_path
        self.cap_input = num
        if image_format[0] != '.':
            image_format = f'.{image_format}'
        self.image_format = image_format
        self.image_name = image_name
        if video_format[0] != '.':
            video_format = f'.{video_format}'
        self.video_format = video_format
        self.view = view

    def camera(self, folder_path, save_video=True):
        """
        Press q to stop collecting frames
        :param folder_path: Path to save images and video into
        :param save_video:
        :param num: integer values between 0 - as many cameras you have
        :return:
        """
        # folder_name = datetime.now().strftime("%H.%M.%S")
        if self.image_format not in self.img_ext:
            logger.exception(f'{self.image_format} not a supported image '
                             f'file, please provide any of the following '
                             f'images {self.img_ext}', exc_info=False)
            exit()
        else:
            pass
        if self.video_format not in self.vid_ext:
            logger.exception(f'Unsupported Video extension provided, '
                             f'please provide any of the following video format: '
                             f'{self.video_format}', exc_info=False)
            exit()
        else:
            pass

        self.cap_input = int(self.cap_input)
        assert isinstance(self.cap_input, int), logger.error('Please provide an Integer value', exc_info=False)

        folder_path = os.path.join(folder_path, datetime.now().strftime("%H.%M.%S"))
        if os.path.exists(folder_path):
            logger.warning(f'OVERWRITING! Folder path {folder_path} already exists')
            pass
        else:
            os.makedirs(folder_path)
        logger.info(f'IMAGES AND VIDEO RECORDED WILL BE SAVED IN {folder_path}')
        logger.debug('YOU MAY PRESS ESC TO STOP COLLECTION ONCE YOU ARE DONE')

        if save_video:
            save_video_frames(self.cap_input, folder_path, self.image_name, self.video_format, self.view)

        else:
            save_frames_only(self.cap_input, folder_path, self.image_name, self.image_format, self.view)

    def videofile(self):
        """

        :return: used for collecting frames from videofile provided a path, return a new folder in
        a parent directory with frames from video file
        """
        self.cap_input = self.cap_input
        v_path = self.cap_input
        assert os.path.exists(self.cap_input), print(f'\033[1;31;40m {self.cap_input}  PATH does not exists'
                                                     f'Please provide an existing path to a video file'
                                                     )
        assert Path(self.cap_input).suffix in self.vid_ext, (f'\033[1;31;40m {self.cap_input} not a video file '
                                                             f'Please provide any of the following images {self.vid_ext}'
                                                             )
        if self.image_format not in self.img_ext:
            logger.exception(f'{self.image_format} not a supported image '
                             f'file please provide any of the following images {self.img_ext}', exc_info=False)
            exit()
        else:
            pass

        self.cap_input = os.path.split(self.cap_input)[1]

        video_input = str(self.cap_input)[0:-len(Path(self.cap_input).suffix)]
        image_folder = os.path.join(Path(v_path).parent, video_input)
        if os.path.exists(image_folder):
            logger.warning(f'OVERWRITING! IMage Folder {image_folder} Already exists')
            pass
        else:
            os.mkdir(image_folder)
        print(video_input)
        camera = cv2.VideoCapture(v_path)
        i = 0
        while camera.isOpened():
            ret, frame = camera.read()
            if ret == True:
                cv2.imwrite(f'{image_folder}/{self.image_name}_{i}.{self.image_format}', frame)
                if self.view:
                    cv2.imshow(f'Output {video_input} Video', frame)
                else:
                    pass
                if not i % 20 == 0:
                    pass
                else:
                    logger.info(f'Frames collected into {image_folder} : {i}')

                i += 1
                if cv2.waitKey(1) & 0xFF == 27:
                    camera.release()

                    cv2.destroyAllWindows()
                    cv2.waitKey(1)

                    # logger.critical('EXITING FRAME COLLECTION.....')

                    # done=True
                    print(Fore.RED + 'FRAME COLLECTION STOPPED ABRUPTLY!');
                    time.sleep(1.5)
                    cv2.destroyAllWindows()
                    cv2.waitKey(1)
                    break

            else:
                camera.release()

                cv2.destroyAllWindows()
                cv2.waitKey(1)
                animated_exit('EXITING FRAME COLLECTION')
                break
        # camera.release()
        msg_print = f'==========================================================================\n' \
                    f'-------------------------SAVED FRAME STATISTICS------------------------ \n' \
                    f'--------------------------------------------------------------------------\n'
        msg_image_path = f'Saved Images Folder:'
        image_folder_print = f'         {image_folder}                           \n'
        space_u = f'==========================================================================\n'
        total_msg = f'Total Number of Images saved:    '
        total_number = f'                                {i} '
        space_b = f'\n=========================================================================='
        print(Fore.CYAN, msg_print, end='')
        print(Fore.GREEN, msg_image_path, end='')
        print(Fore.RED, image_folder_print, end='')
        print(Fore.CYAN, space_u, end='')
        print(Fore.GREEN, total_msg, end='')
        print(Fore.RED, total_number, end='')
        print(Fore.CYAN, space_b)
        cv2.destroyAllWindows()
        cv2.waitKey(1)

    def videofolder(self, Image_folder='Image Folder'):
        """

        :param cap_input: path to feed cv2.VideoCapture
        :param image_format:  format of output image, refer to img_ext
        :param Image_folder: name of folder to save images to
        :return:
        """

        vid_ext = ['.avi', '.flv', '.mpg', '.mpeg', '.mpe', '.mpv', '.mp2', '.mp4', '.3gp', '.m4p', '.m4v', '.ogg',
                   '.webm', '.mov', '.wmv']
        img_ext = ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.psd', '.pdf', '.eps', '.raw', '.svg', '.bmp',
                   '.dib']
        img_ext_ = ['jpg', 'jpeg', 'png', 'gif', 'tiff', 'psd', 'pdf', 'eps', 'raw', 'svg', 'bmp',
                    'dib']

        assert os.path.isdir(self.cap_input), (f'\033[1;31;40m {self.cap_input} not a directory '
                                               f'Please provide a directory with video files')
        assert f'{self.image_format}' in img_ext, print(
            f'\033[1;31;40m {self.image_format} not a supported image file '
            f'Please provide any of the following images {img_ext_}'
        )
        new_folder = os.path.join(Path(self.cap_input).parent, Image_folder)

        if os.path.exists(new_folder):
            pass
        else:
            os.makedirs(new_folder)

        vids_path = os.listdir(self.cap_input)
        videos = []

        def returnTrue(file_in):
            if Path(file_in).suffix in vid_ext:
                return True

            return False

        assert any([returnTrue(file_in) for file_in in vids_path]) is True, print(
            (f'\033[1;31;40m {self.cap_input} contains no video file '
             f'Please provide a directory with video files'
             ))

        [videos.append(ext) for ext in vids_path if Path(ext).suffix in vid_ext]
        videos = tqdm(videos)
        total = 0
        to_log = {}
        for vid in videos:
            videos.set_description(f'{total} Images have been saved')
            time.sleep(0.05)
            tot_image = frame_capture(os.path.join(self.cap_input, vid), self.image_format, new_folder, vid, self.view)
            to_log[f'{vid}'] = f'{tot_image} Images'
            total += tot_image

            if cv2.waitKey(1) & 0xFF == 27:
                logger.critical('FRAME COLLECTION STOPPED ABRUPTLY');
                time.sleep(0.5)
                logger.critical(f'TOTAL IMAGES SAVED: {total}')
                cv2.destroyAllWindows()
                cv2.waitKey(1)
                break
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        to_log = json.dumps(to_log, indent=20, sort_keys=True, default=dict)
        total = json.dumps(total, indent=20, sort_keys=True, default=int)
        to_log = re.sub(r"^{\s*", "{", to_log)
        folder_list = os.listdir(new_folder)
        # response_text = re.sub(r"\s*}$", "}", total)
        animated_exit('EXITING FRAME COLLECTION')
        animated_exit('COMPUTING STATS')

        msg_print = f'==========================================================================\n' \
                    f'-------------------------SAVED FRAME STATISTICS------------------------ \n' \
                    f'--------------------------------------------------------------------------\n'
        folder_path_print = f'Folders'' Path:\n'

        msg_image_path = f'\n Saved Images Folder:'
        image_folder_print = f'                 {to_log}                           \n'
        space_u = f'==========================================================================\n'

        total_msg = f'Total Number of Images saved:    '
        total_number = f'                                {total} '
        space_b = f'\n=========================================================================='
        print(Fore.LIGHTBLUE_EX, msg_print, end='')
        print(Fore.LIGHTBLUE_EX, folder_path_print, end='')
        for paths_ in folder_list:
            print(Fore.MAGENTA, f'              {os.path.join(new_folder, paths_)}')

        print(Fore.LIGHTBLUE_EX, msg_image_path, )
        print(Fore.MAGENTA, image_folder_print, end='')
        print(Fore.LIGHTBLUE_EX, space_u, end='')
        print(Fore.LIGHTBLUE_EX, total_msg, end='')
        print(Fore.RED, total_number, end='')
        print(Fore.LIGHTBLUE_EX, space_b)


# video_path = '/Users/solua1/Documents/TestVideos/video.mp4'
# video_path = '/Users/solua1/Documents/TestVideos'
# collect_frames(video_path).videofolder()
# collect_frames(video_path).videofile()
# collect_frames(0).camera('/Users/solua1/Documents/', save_video=True)

# print('back to normal now')
# print('\033[31m' + 'some red text')
