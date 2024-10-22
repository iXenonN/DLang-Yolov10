<h1 align="center" id="title">Python Yolov10 With DLang</h1>

<p id="description">Runs yolov10 with Python and connects to the DLang with the socket module and passes the data to the D program.</p>

  
  
<h2 align="center">📚 Libraries Used</h2>
<h3>Python:</h3>

```
from ultralytics import YOLOv10
import supervision as sv
import cv2
import socket
import pickle
```
<h4>For Install:</h4>

```
pip install supervision
pip install ultralytics
pip install opencv-python
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
<p>3. Then copy the name of the pt you downloaded and paste it to 'YOUR YOLOV10 PT' part of python code.</p>

```
MODEL_PATH = 'YOUR YOLOV10 PT'
```

<p>3. Make sure you have any D compiler like dmd.</p>

<p>4. Open your D command prompt and cd to your project path.</p>

<p>5. Run the python code first then run the D code with "dub run" command in your D command prompt.</p>

```
dub run
```
<p>6. If everything goes right you should have seen the output.</p>

<h2 align="center"> 🚧 Troubleshooting & Common Issues </h2>

<h3> ❌ Issue: `core.exception.OutOfMemoryError@src\core\internal\gc\impl\conservative\gc.d(512): Memory allocation failed` </h3>
 <h4>- Cause:</h4> This error occurs when you try to make a memory allocation in the D language and there is not enough memory available..
  
  <h4>- Solution:</h4> Ensure that your camera is turned on and yolov10 is running.
  
