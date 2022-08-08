import os.path
from pathlib import Path
import cv2


def frame_capture(file, image_format, new_folder, videos):
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
            cv2.imshow('name', frame)
            cv2.imwrite(f'{frames_folder}/image_{i}.{image_format}', frame)
            i += 1
            if not i % 5 == 0:
                pass
            # print(f'image_{i} saved into: {frames_folder}/image_{i}.jpg')
            else:
                print(f'Frames collected into {frames_folder} : {i}')


        else:
            break
        cv2.waitKey(25)
    cap.release()


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
    def __init__(self, num, video_format='mp4', image_name='frame', image_format='jpg', videos_path=False):
        super(collect_frames, self).__init__()
        self.img_ext = ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.psd', '.pdf', '.eps', '.raw', '.svg', '.bmp',
                        '.dib']
        self.vid_ext = ['.avi', '.flv', '.mpg', '.mpeg', '.mpe', '.mpv', '.mp2', '.mp4', '.3gp', '.m4p', '.m4v', '.ogg',
                        '.webm', '.mov', '.wmv']
        self.videos_path = videos_path
        self.cap_input = num
        self.image_format = image_format
        self.image_name = image_name
        self.video_format = video_format

    def camera(self, folder_path, save_video=True):
        """
        Press q to stop collecting frames
        :param folder_path: Path to save images and video into
        :param save_video:
        :param num: integer values between 0 - as many cameras you have
        :return:
        """
        if os.path.exists(folder_path):
            pass
        else:
            os.makedirs(folder_path)
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
            save_video_frames(self.cap_input, folder_path, self.image_name, self.video_format)

        else:
            save_frames_only(self.cap_input, folder_path, self.image_name, self.image_format)

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
        i = 0
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

    def video_folder(self, Image_folder='Image Folder'):
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
        # vid_ext_ = ['avi', 'flv', 'mpg', 'mpeg', 'mpe', 'mpv', 'mp2', 'mp4', '3gp', 'm4p', 'm4v', 'ogg',
        #             'webm', 'mov', 'wmv']
        assert os.path.isdir(self.cap_input), (f'\033[1;31;40m {self.cap_input} not a directory '
                                               f'Please provide a directory with video files')
        assert f'.{self.image_format}' in img_ext, print(
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

        """
        prints 
        ['2.jpg', '360_360-0882_preview.mp4', '360_360-0809_preview.mp4', '1.jpg', '16.jpg', '8.jpg', '7.jpg', '9.jpg', 
        '14.jpg', '10.jpg', 'istock-887357848_preview.mp4', '170609_E_Varanasi_010.mp4', '5.jpg', '20.jpg', '17.jpg', 
        '18.jpg', '19.jpg', '15.jpg', '3.jpg', '11.jpg', '4.jpg', '13.jpg', '6.jpg', '360_360-0383_preview.mp4', '12.jpg']"""

        assert any([returnTrue(file_in) for file_in in vids_path]) is True, print(
            (f'\033[1;31;40m {self.cap_input} contains no video file '
             f'Please provide a directory with video files'
             ))

        [videos.append(ext) for ext in vids_path if Path(ext).suffix in vid_ext]

        for vid in videos:
            frame_capture(os.path.join(self.cap_input, vid), self.image_format, new_folder, vid)
        print(f'\033[1;31;40mALL COLLECTED FRAMES HAVE BEEN SAVED INTO {new_folder}')

