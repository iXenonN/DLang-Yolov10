from ultralytics import YOLOv10
import supervision as sv
import cv2
import socket
import pickle

MODEL_PATH = 'yolov10x.pt'
cap = cv2.VideoCapture(0)

model = YOLOv10(MODEL_PATH)
bounding_box_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()

# create TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5000))
server_socket.listen(1)
print("Waiting for D app to connect...")

conn, addr = server_socket.accept()
print(f"{addr} connected!")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Video Error")
        break

    results = model(frame)[0]
    detections = sv.Detections.from_ultralytics(results)

    annotated_image = bounding_box_annotator.annotate(scene=frame, detections=detections)
    annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)

    # get information of detected objects
    data = []
    for i in range(len(detections.class_id)):
        item = {
            "class_id": detections.class_id[i],
            "confidence": detections.confidence[i],
            "bbox": detections.xyxy[i].tolist()  # bounding box coordinates
        }
        data.append(item)

    serialized_data = pickle.dumps(data)
    conn.sendall(serialized_data)

    cv2.imshow("Yolov10", annotated_image)

    k = cv2.waitKey(1)
    if k % 256 == 27:  # press ESC for exit
        print("Closing...")
        break

cap.release()
conn.close()
cv2.destroyAllWindows()
