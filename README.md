<h1 align="center" id="title">Python Yolov10 With DLang</h1>

<p id="description">Runs yolov10 with Python and connects to the DLang with the socket module and passes the data to the D program.</p>

  
  
<h2>📚 Libraries</h2>
<h1>Python:</h1>
```
from ultralytics import YOLOv10
import supervision as sv
import cv2
import socket
import pickle
```
<h1>DLang:</h1>
```
import std.stdio;
import std.socket;
import std.array;
```
