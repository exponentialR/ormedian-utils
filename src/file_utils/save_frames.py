import glob
import os.path
from pathlib import Path

import cv2

cap = cv2.VideoCapture(0)
i = 0


class collect_frames():
    def __init__(self, num, image_format, image_name, folder_path, videos_path=False):
        super(collect_frames, self).__init__()
        self.cam = cv2.VideoCapture(0)
        self.img_ext = ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.psd', '.pdf', '.eps', '.raw', '.svg', '.bmp',
                        '.dib']
        self.vid_ext = ['.avi', '.flv', '.mpg', '.mpeg', '.mpe', '.mpv', '.mp2', '.mp4', '.3gp', '.m4p', '.m4v', '.ogg',
                        '.webm', '.mov', '.wmv']
        self.videos_path = videos_path
        self.cap_input = num
        self.image_format = image_format
        self.image_name = image_name
        self.folder_name = folder_path
        if os.path.exists(self.folder_name):
            pass
        else:
            os.makedirs(self.folder_name)

    def camera(self):
        """
        Press q to stop collecting frames
        :param num: integer values between 0 - as many cameras you have
        :return:
        """

        assert self.image_format in self.img_ext, print(f'\033[1;31;40m {self.image_format} not a supported image file '
                                                        f'Please provide any of the following images {self.img_ext}'
                                                        )
        self.cap_input = int(self.cap_input)
        assert self.cap_input.isnumeric(), f'\033[1;36;40m Please provide an Integer value'
        cam = cv2.VideoCapture(self.cap_input)
        i = 0

        while True:
            ret, frame = cam.read()
            cv2.imshow('Output Video', frame)
            cv2.imwrite(f'{self.folder_name}/{self.image_name}_{i}', frame)
            i += 1
            if cv2.waitKey(0) & 0XFF == ord('q'):
                break
        cam.release()
        cv2.destroyAllWindows()

    def videofile(self):
        """

        :param video_path: path to the video file
        :return:
        """

        assert os.path.exists(self.cap_input), print(f'\033[1;31;40m {self.cap_input}  PATH does not exists'
                                                     f'Please provide an existing path to a video file'
                                                     )
        assert Path(self.cap_input).suffix in self.vid_ext, (f'\033[1;31;40m {self.cap_input} not a video file '
                                                             f'Please provide any of the following images {self.vid_ext}'
                                                             )
        assert self.image_format in self.img_ext, print(
            f'\033[1;31;40m {self.image_format} not a supported image file '
            f'Please provide any of the following images {self.img_ext}'
        )

        cam = cv2.VideoCapture(self.cap_input)
        assert cam.isOpened() == True, print('Error reading/opening video file')
        i = 0
        while (cam.isOpened()):
            ret, frame = cam.read()
            cv2.imshow('Video Output', frame)
            cv2.imwrite(f'{self.folder_name}/{self.image_name}_{i}', frame)
            i += 1
            if cv2.waitKey(0) & 0XFF == ord('q'):
                break
        cam.release()
        cv2.destroyAllWindows()



# import glob
# import os
cap_input = os.listdir('/home/iamshri/Downloads/UnityEyes_Linux/unityeyes_Data/Managed/')
for ext in cap_input:
    print(ext[0:-len(Path(ext).suffix)])
# ext_e = '.dll'
# print(len(glob.glob(f'{cap_input}/*{ext_e}')))
# print(len(vids_path))
# print(vids_path[0])
