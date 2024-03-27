from ultralytics import YOLO
import torch
import torchvision


# pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
# yolo predict model=runs/detect/train2/weights/best.pt source='obj_detect.v1i.yolov8/test/images/IMG_20240327_145633_jpg.rf.0891fc27d71bedc8953af7c2e19603af.jpg' imgsz=640

# Create a new YOLO model from scratch
model = YOLO('yolov8n.yaml')

# Load a pretrained YOLO model (recommended for training)
model = YOLO('yolov8n.pt')

# Train the model
results = model.train(data='D:\Programs\YoloV8\obj_detect.v1i.yolov8\data.yaml', epochs=80, imgsz=640)

# Evaluate the model's performance on the validation set
results = model.val()

# Perform object detection on an image using the model
results = model('D:/Programs/YoloV8/obj_detect.v1i.yolov8/test/images/IMG_20240327_144755_jpg.rf.99a56f506ec16ebffe197710f5a70ea1.jpg')

# Export the model to ONNX format
success = model.export(format='onnx')
