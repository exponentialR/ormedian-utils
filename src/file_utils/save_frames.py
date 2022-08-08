import glob
import os.path
from pathlib import Path

import cv2


def save_video_frames(cap_input, folder, image_name, video_format):
    video_name = os.path.join(folder, image_name)
    if not os.path.exists(video_name):
        pass
    else:
        print('Video name already exist, please choose a different name')
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
            cv2.imshow(f'{video_name}', frame)
            i += 1

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    camera.release()
    video_.release()
    cv2.destroyAllWindows()


def save_frames_only(cap_input, folder, image_name, image_format):
    video_name = os.path.join(folder, image_name)
    camera = cv2.VideoCapture(cap_input)
    i = 0
    while camera.isOpened():
        ret, frame = camera.read()
        if ret == True:
            frame = cv2.flip(frame, 1)
            cv2.imwrite(f'{video_name}_{i}.{image_format}', frame)
            cv2.imshow(f'Output {image_name} Video', frame)
            i += 1

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    camera.release()
    cv2.destroyAllWindows()


class collect_frames:
    def __init__(self, num, folder_path, video_format='mp4', image_name='frame', image_format='jpg', videos_path=False):
        super(collect_frames, self).__init__()
        self.img_ext = ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.psd', '.pdf', '.eps', '.raw', '.svg', '.bmp',
                        '.dib']
        self.vid_ext = ['.avi', '.flv', '.mpg', '.mpeg', '.mpe', '.mpv', '.mp2', '.mp4', '.3gp', '.m4p', '.m4v', '.ogg',
                        '.webm', '.mov', '.wmv']
        self.videos_path = videos_path
        self.cap_input = num
        self.image_format = image_format
        self.image_name = image_name
        self.folder_name = folder_path
        self.video_format = video_format
        if os.path.exists(self.folder_name):
            pass
        else:
            os.makedirs(self.folder_name)

    def camera(self, save_video=True):
        """
        Press q to stop collecting frames
        :param save_video:
        :param num: integer values between 0 - as many cameras you have
        :return:
        """

        assert f'.{self.image_format}' in self.img_ext, print(
            f'\033[1;31;40m {self.image_format} not a supported image file '
            f'Please provide any of the following images {self.img_ext}'
        )
        assert f'.{self.video_format}' in self.vid_ext, print(f'\033[1;31;40m Unsupported video extension provided'
                                                              f'Please provide any of the following video format {self.video_format}'
                                                              )
        self.cap_input = int(self.cap_input)
        assert isinstance(self.cap_input, (int)), f'\033[1;36;40m Please provide an Integer value'

        if save_video:
            save_video_frames(self.cap_input, self.folder_name, self.image_name, self.video_format)

        else:
            save_frames_only(self.cap_input, self.folder_name, self.image_name, self.image_format)

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
        assert f'.{self.image_format}' in self.img_ext, print(
            f'\033[1;31;40m {self.image_format} not a supported image file '
            f'Please provide any of the following images {self.img_ext}'
        )
        self.cap_input = os.path.split(self.cap_input)[1]

        video_input = str(self.cap_input)[0:-len(Path(self.cap_input).suffix)]
        image_folder = os.path.join(Path(v_path).parent, video_input)
        if os.path.exists(image_folder):
            pass
        else:
            os.mkdir(image_folder)
        print(video_input)
        camera = cv2.VideoCapture(v_path)
        i=0
        while camera.isOpened():
            ret, frame = camera.read()
            if ret == True:
                print(image_folder)
                cv2.imwrite(f'{image_folder}/{self.image_name}_{i}.{self.image_format}', frame)
                cv2.imshow(f'Output {video_input} Video', frame)
                print(f'\033[1;33;40m frame {i} collected and saved into \033[1;32;40m {image_folder}')
                i += 1
                if cv2.waitKey(45) & 0xFF == ord('q'):

                    break
            else:
                break
        camera.release()
        cv2.destroyAllWindows()



folder_path = '/home/iamshri/Videos/Webcam'
video_path = '/home/iamshri/Videos/Webcam/2022-05-13-085401.webm'
# data = collect_frames(video_path, folder_path)
# data = collect_frames(0, '/home/iamshri/Videos/Webcam')
# data.camera(save_video=False)
# data.videofile()

