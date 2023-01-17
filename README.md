# Project: Snapchat Filter!

https://user-images.githubusercontent.com/45706760/212926329-57251e7e-d10b-467d-b02c-3c73fb6ce1f8.mp4


Who does not know about Snapchat Filters. 
But did you ever wonder how do they put the filter on live streaming video exactly at the required spot.

The idea here is to detetct the top left corner of the face and also get the height and width of the face, i.e, (x, y, w, h).

With certain adjustments in these values one can easily detect the various facial features and then with the help of opencv library overlayPNG another image is put over the live stream video.

Isn't it amazing?


The only thing that one needs to take care of in this project is that the overlaying png image must have an alpha channel.

I used some filters but you can play along with your filters as well.

Also, the other interesting part of this project is I created an API usinh Kivy which is a Pythonic GUI for
all the OS.

### STEPS:

Clone the repository

```bash
https://github.com/aibi10/snapchat-filter.git
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n snapchatfilter python=3.7.10 -y
```

```bash
conda activate snapchatfilter
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

### STEP 03- create environment specification in conda.yaml

```bash
conda env export > conda.yaml
```

### STEP 04 - run this command to genrate pickle files

```bash
python main.py
```



```bash
Author: Abhishek Singh
Data Scientist
Email: isingh.abhishek10@gmail.com

```
