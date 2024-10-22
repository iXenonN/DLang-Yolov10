<h1 align="center" id="title">Python Yolov10 With DLang</h1>

<p id="description">Runs yolov10 with Python and connects to the DLang with the socket module and passes the data to the D program.</p>

  
  
<h2 align="center">📚 Libraries</h2>
<h3>Python:</h3>

```
from ultralytics import YOLOv10
import supervision as sv
import cv2
import socket
import pickle
```

<h3>DLang:</h3>

```
import std.stdio;
import std.socket;
import std.array;
```
<h2 align="center">🛠️ Installation Steps:</h2>

<p>1. Download any yolov10 pt from the link below and put it in the same folder as your project folder.</p>


```
https://github.com/THU-MIG/yolov10
```
<p>2. Make sure you have any D compiler like dmd.</p>

<p>3. Open your D command prompt and cd to your project path.</p>

<p>4. Run the python code first then run the D code with "dub run" command in your D command prompt.</p>

```
dub run
```
