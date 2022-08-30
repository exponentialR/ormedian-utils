This package contains the following utilities
- [x] Frame Saver - save frames from video, folders containing videos or camera feed/livefeed.
- [x] Image Resizer - Resize image while retaining the quality
- [x] File mover - move specific file types from thousands/myriads of files.

More utility function to be added subsequently.
I hope you find this package useful


To install:

``
pip3 install ormedian-utils
``

<br>

> ### FRAME SAVER 

```
collect_frames(num, video_format='mp4', image_name='frame', image_format='jpg')
```
`num`: **could be camera id, path to video, or a folder contain a number of videos**

`video_format`: **format of output video if saving video, default format is set to mp4**

`image_name`: **name of frame files, numbers will be appended at the back in the form of frames_1, frames_2...frames_n**

`image_format`: **extension of image/frames to be saved, default format is 'jpg', could be any image format, e.g 'png', 'bmp' etc**

Save frames from video, camera feed, video folder containing multiple videos.
These module has 3 methods:

<br>

> 1. **camera** 
    
for saving frames from camera feed
   
 **USAGE**:

````
from ormedian_utils import collect_frames
camera_id =0
frames = collect_frames(camera_id)
frames.camera(camera_id, save_video=True)
````
<br>

> 2. **videofolder** 

for saving frames from videos in a folder(s)

**USAGE**:
````
from ormedian_utils import collect_frames
video_folder_path ='path/to/foldercontaining/videos
frames = collect_frames(video_folder_path)
Image_folder = 'CollectedFrames'    #default set to 'Image Folder'
frames.videofolder(video_folder_path, Image_folder=Image_folder)
````

<br>

> 3. **videofile** 

for saving frames from a single video file

**USAGE**:
````
from ormedian_utils import collect_frames
video_path = 'path/to/a/singlevideo'
frames = collect_frames(video_path)
frames.videofile()
````

<br>

> ### IMAGE RESIZER 


Resize images in a folder or in multiple folders 

```
image_resizer (new_size: tuple, image_path: str,
              quality: int, n_f=True, new_folder='ResizedImages',
              view=True, out_format='jpg', multiple_folders=False)
```
              
```out_format:``` **expected format of the output image e.g 'jpg', 'bmp' 'png' etc default is jpg**

```view:``` **default value is set to True, there would display window showing resized images**

```new_size:``` **expected New Image size e.g (224, 224)**

```image_path:``` **'/path/to/where/images/are**

```quality:``` **The quality of the picture resized e.g. 100**

```multiple_folders:``` **Set to True if image_path contains more than one image folder, default is False**

```n_f: ``` **set to True if resized images be saved in new_folder, set to True by default**

```new_folder:``` **Name of new folder to save resized images, accepts strings, default value is set to 'ResizedImages'**

**USAGE:**

```
from ormedian_utils import  image_resizer

new_size = (100, 100)
images_folder = '/path/to/images/folder' 
quality =100
```
```
image_resizer(new_size,
              images_folder,
              quality)
```

<br>

> ### FILE MOVER 


Move files from one folder to another 

```filemover(folder_path: str, file_ext: str, new_folder: str)```

``folder_path:`` **path to files, e.g /path/to/folder/files/**

``file_ext:`` **file extension of files to move e.g 'json'**

``new_folder:`` **folder name of where to move files to, creates directory in parent directory if it does not already exist**


**USAGE:** 
```
from ormedian_utils import filemover

folder_path = /path/to/different/files     #contains json, csv, jpg, and docs files
file_ext = 'json'
new_folder = 'MovedFiles'

filemover(folder_path, file_ext, new_folder)

```
