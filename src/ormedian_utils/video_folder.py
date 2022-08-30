import os
import time
from pathlib import Path
import cv2
from tqdm import tqdm


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
            print(f'image{i} saved into: {frames_folder}/image_{i}.jpg')
            i += 1
        else:
            break
        cv2.waitKey(25)
    cap.release()


def video_folder(cap_input, Image_folder = 'Image Folder', image_format='jpg'):
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

    assert os.path.isdir(cap_input), (f'\033[1;31;40m {cap_input} not a directory '
                                               f'Please provide a directory with video files')
    assert f'.{image_format}' in img_ext, print(
        f'\033[1;31;40m {image_format} not a supported image file '
        f'Please provide any of the following images {img_ext_}'
    )
    new_folder = os.path.join(Path(cap_input).parent, Image_folder)

    if os.path.exists(new_folder):
        pass
    else:
        os.makedirs(new_folder)

    vids_path = os.listdir(cap_input)
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

    assert any([returnTrue(file_in) for file_in in vids_path]) is True, print((f'\033[1;31;40m {cap_input} contains no video file '
                   f'Please provide a directory with video files'
                   ))

    [videos.append(ext) for ext in vids_path if Path(ext).suffix in vid_ext]

    videos = tqdm(videos)
    for vid in videos:
        time.sleep(0.1)
        frame_capture(os.path.join(cap_input, vid), image_format, new_folder, vid)
        videos.set_description(f'Saving frames from {vid} Video')

# video_path = '/home/iamshri/Videos'
# # video_path = '/home/iamshri/new_videos/170609_E_Varanasi_010'
# images_folder = 'Images'
# video_folder(video_path)
