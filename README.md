https://user-images.githubusercontent.com/73752977/188218332-96f6766d-3f7f-4eb0-89f2-c2b58a08c375.mp4


This package contains the following utilities

**🚀Frame Saver** - save frames from video, folders containing videos or camera feed/livefeed.\
**🚀Image Resizer** - Resize image while retaining the quality\
**🚀File mover** - move specific file types from thousands/myriads of files.


More utility functions to be added subsequently.



I hope you find this package useful


To install:

``
pip3 install ormedian-utils
``

<br>

> ### FRAME SAVER                   ``collect_frames()``
Save frames from video, camera feed, video folder containing multiple videos.

```
collect_frames(num, video_format='mp4', image_name='frame', image_format='jpg', view=True)
```
`num`: **could be camera id, path to video, or a folder contain a number of videos**\
`video_format`: **format of output video if saving video, default format is set to mp4**\
`image_name`: **name of frame files, numbers will be appended at the back in the form of frames_1, frames_2...frames_n, could be changed to wheveter you want**\
`image_format`: **extension of image/frames to be saved, default format is 'jpg', could be any image format, e.g 'png', 'bmp' etc**

This package has 3 methods:

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
``save_video=True`` saves video from camera feed into the same folder as the collected frames. You may set ``save_video`` to ``False`` to not save video. 
<br>

> 2. **videofolder** 

for saving frames from videos in a folder(s)

**USAGE**:
````
from ormedian_utils import collect_frames
video_folder_path ='path/to/foldercontaining/videos
frames = collect_frames(video_folder_path)
Image_folder = 'Image Folder' 
frames.videofolder(video_folder_path, Image_folder=Image_folder)
````

``Image_folder``: Where Frames will be saved. defaults to ``Image Folder`` unless otherwise changed\
A new folder will be created for each video, and corresponding frames will be saved in this folder.

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

> ### IMAGE RESIZER ``image_resizer()``


Resize images in a folder or in multiple folders 


https://user-images.githubusercontent.com/73752977/187389467-3e4c8e8f-bab9-433f-9e0a-e80dca32037b.mp4


```
image_resizer (new_size: tuple,
                  image_path: str,
                  n_f=True, new_folder='ResizedImages',
                  view=True, multiple_folders=False):
```
```new_size:``` **expected New Image size e.g (224, 224)**

```image_path:``` **'/path/to/where/images/are**

```n_f: ``` **set to True if resized images be saved in new_folder, set to True by default**
NOTE: if resizing multiple folders (``multiple_folders=True``) and  ``n_f`` is set ``True`` 
This will create a separate folder for each folder (``Parent_folder of image_path/ResizedImages/subfolders``) in the parent directory of ``image_path``.
Setting ``n_f`` to ``False`` when resizing ``multiple_folders`` will override the existing ``image_path`` and overwrite the images in the subfolders.

```new_folder:``` **Name of new folder to save resized images, accepts strings, default value is set to 'ResizedImages'**

```view:``` **default value is set to True, this would display window showing resized images**

```multiple_folders:``` **Set to True if image_path contains more than one image folder, default is False**


**USAGE:**
```
from ormedian_utils import  image_resizer

new_size = (100, 100)
images_folder = '/path/to/images/folder' 
quality =100
```
In this case ``images_folder contains multiple image folders``. Hence we set ``multiple_folders`` to ``True`` below.
```
image_resizer(new_size,
              images_folder,
              n_f=True,
              quality, multiple_folders=True)
```

<br>

> ### FILE MOVER ``filemover()``


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

### Todo
- [ ] **Image Converter**
- [ ] **Video Converter**
- [ ] **Audio Parser**
