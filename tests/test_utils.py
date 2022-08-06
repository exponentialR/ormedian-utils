import os
from pathlib import Path
import cv2
import glob


def frame_capture(file, image_format, new_folder, videos):
    print(videos[0:-len(Path(videos).suffix)])
    frames_folder = os.path.join(new_folder, videos[0:-len(Path(videos).suffix)])
    if os.path.exists(frames_folder):
        pass
    else:
        os.mkdir(frames_folder)
    print(frames_folder)

    cap = cv2.VideoCapture(file)
    i = 0
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('name', frame)
            cv2.imwrite(f'{frames_folder}/image_{i}.{image_format}', frame)
            print(f'image{i} saved into: {frames_folder}/image_{i}.jpg')
            i += 1
        else:
            break
        cv2.waitKey(25)
    cap.release()


def video(cap_input, image_format, folder_name, image_name, folder=False):
    """

    :param cap_input: path to feed cv2.VideoCapture
    :param image_format:  format of output image, refer to img_ext
    :param folder_name: name of folder to save images to
    :param image_name: name prefix for the images
    :param folder: set True if you have a folder containing more than one video
    :return:
    """
    vid_ext = ['.avi', '.flv', '.mpg', '.mpeg', '.mpe', '.mpv', '.mp2', '.mp4', '.3gp', '.m4p', '.m4v', '.ogg',
               '.webm', '.mov', '.wmv']
    img_ext = ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.psd', '.pdf', '.eps', '.raw', '.svg', '.bmp',
               '.dib']
    new_folder = os.path.join(Path(cap_input).parent, folder_name)
    if os.path.exists(new_folder):
        pass
    else:
        os.makedirs(new_folder)
    # print(new_folder)

    if folder is False:
        assert os.path.exists(cap_input), print(f'\033[1;31;40m {cap_input}  PATH does not exists'
                                                f'Please provide an existing path to a video file'
                                                )
        assert Path(cap_input).suffix in vid_ext, (f'\033[1;31;40m {cap_input} not a video file '
                                                   f'Please provide any of the following images {vid_ext}'
                                                   )
        assert image_format in img_ext, print(
            f'\033[1;31;40m {image_format} not a supported image file '
            f'Please provide any of the following images {img_ext}'
        )

        cam = cv2.VideoCapture(cap_input)
        assert cam.isOpened() is True, print('Error reading/opening video file')
        i = 0
        while (cam.isOpened()):
            ret, frame = cam.read()
            cv2.imshow('Video Output', frame)
            cv2.imwrite(f'{folder_name}/{image_name}_{i}', frame)
            i += 1
            if cv2.waitKey(0) & 0XFF == ord('q'):
                break
        cam.release()
        cv2.destroyAllWindows()

    else:

        vids_path = os.listdir(cap_input)
        videos = []
        """
        prints 
        ['2.jpg', '360_360-0882_preview.mp4', '360_360-0809_preview.mp4', '1.jpg', '16.jpg', '8.jpg', '7.jpg', '9.jpg', 
        '14.jpg', '10.jpg', 'istock-887357848_preview.mp4', '170609_E_Varanasi_010.mp4', '5.jpg', '20.jpg', '17.jpg', 
        '18.jpg', '19.jpg', '15.jpg', '3.jpg', '11.jpg', '4.jpg', '13.jpg', '6.jpg', '360_360-0383_preview.mp4', '12.jpg']"""
        [videos.append(ext) for ext in vids_path if Path(ext).suffix in vid_ext]
        print(videos)
        for i in range(len(videos) - 1):
            # print(new_folder)
            frame_capture(os.path.join(cap_input, videos[i]), image_format, new_folder, videos[i])



Vid_path = '/home/iamshri/Videos'

video(Vid_path, 'jpg', 'new_videos', 'frame', folder=True)
